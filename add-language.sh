#!/usr/bin/env bash

base="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

potdir="$base/pot"
mkdir -p "$potdir"
localdir="$base/locale"

# allow user to specify language
lang=$1
if [ -z "$lang" ]; then
    read -p 'Enter language to add: ' lang
    lang="${lang#"${lang%%[![:space:]]*}"}"
    lang="${lang%"${lang##*[![:space:]]}"}"
    if [ -z "$lang" ]; then
        exit 0
    fi
fi

while true; do
    read -p "Generate for language $lang? " yn

    case $yn in
    [Yy]*) break;;
    [Nn]*) exit 0;;
        *) echo "Please answer yes or no.";;
    esac
done

# fail on error
set -e

# generate language files
echo -e "\e[7mgenerating $lang...\e[0m"
python -m sphinx_intl update \
    --pot-dir "$potdir" --language $lang --locale-dir "$localdir"
