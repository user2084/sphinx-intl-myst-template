# sphinx-intl-myst-template - A Sphinx Project Template

## Features

- [MyST markdown](https://myst-parser.readthedocs.io/en/latest/)
- [sphinx-intl for internationalization](https://sphinx-intl.readthedocs.io/en/master/quickstart.html#quickstart-for-sphinx-translation)
  - [sphinx translations guide](https://docs.readthedocs.io/en/stable/guides/manage-translations-sphinx.html)

## Usage

- base language is English (`build/en` and `source/`)
- translation example is given in German (`build/de` and `locale/de`)
- add another language with: `./add-language.sh es`
  - translate in `locale/es/LC_MESSAGES/*.po` (fill corresponding `msgstr` fields)
- build: `./build.sh` (**recreates** `./build`!)
  - PDF: `./build.sh pdf`

## Requirements

- [sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html)
- Python packages:
```
pip install --user sphinx-book-theme myst-parser sphinx-intl rst2pdf
```

## Inspired by

- https://github.com/jdknight/sphinx-i8n-myst-example
- https://github.com/ThoSe1990/SphinxExample

## LICENSE

Public Domain.
