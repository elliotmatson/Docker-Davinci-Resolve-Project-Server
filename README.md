# Davinci Resolve Project Server
Simple Resolve project server with automatic backups and an updated Postgresql version

## Table of Contents
- [Davinci Resolve Project Server](#davinci-resolve-project-server)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

There are a lot of ways to host a Resolve project server, but each of them has their own set of issues. 

### Features
- **Lightweight** - Docker based, so doesn't require a full MacOS or Windows machine or VM
- **Platform Independant** - can be installed on Windows, Mac, Linux, QNAP, Synology, RPi, really anything that can run Docker
- **Compatible with Resolve's existing backup/restore functions** - All backup files use the standard *.backup file syntax that Resolve uses, unlike most of the Postgres backup solutions that exist now

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)