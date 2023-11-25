#!/usr/bin/env bash

## This is based on scripts from jdknight:
## https://github.com/jdknight/sphinx-i8n-myst-example

set -e

builder=${1:-html}

base="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
outdir="$base/build"
srcdir="$base/source"
localedir="$base/locale"
potdir="$base/pot"

sphinx="sphinx-build"
sphinxintl="sphinx-intl"

# --- UPDATE ---
# generate translation files

echo -e "\e[7mgenerate translation files (pot)...\e[0m"
$sphinx -b gettext "$srcdir" "$potdir"
echo ""

languages=()
for ref in $(ls -d $localedir/*/LC_MESSAGES 2>/dev/null); do
    lang_dir=${ref%/*}
    lang_dir=${lang_dir%%/}
    lang=${lang_dir##*/}

    # update language files
    echo -e "\e[7mupdating language ($lang)...\e[0m"
    $sphinxintl update \
                --pot-dir "$potdir" \
                --language "$lang" \
                --locale-dir "$localedir"

    languages+=($lang)
done

# --- BUILD ---

# fresh start
rm -rf "$outdir"
mkdir -p "$outdir"

# Add English
languages+=("en")
# build outputs for each language
for lang in "${languages[@]}"; do
    lang_target_dir="$outdir/$lang"
    echo -e "\e[7mbuilding $lang ($builder)...\e[0m"

    # build documentation
    $sphinx \
        -b $builder \
        -Dlanguage=$lang \
        "$srcdir" \
        "${lang_target_dir}" \
        -Dlocale_dirs="$localedir" \
        -E -a
    #-W

    # cleanup
    rm -rf "${lang_target_dir}/.doctrees"
    rm -rf "${lang_target_dir}/.buildinfo"
done
