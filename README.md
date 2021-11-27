# Davinci Resolve Project Server
Simple Resolve project server with automatic backups

## Table of Contents
- [Davinci Resolve Project Server](#davinci-resolve-project-server)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Features](#features)
  - [Installation](#installation)
  - [Different Postgres versions](#different-postgres-versions)

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


## Different Postgres versions
Generally, Resolve is most compatible with the latest Postgres 9.5 version (9.5.25 as of writing). The Windows version of Resolve uses 9.5.4, and the Mac version uses 9.5.19. Version 9.5 is EOL, and 9.5.4 in particular has a lot of vulnerabilities that make it insecure. Since most people are still using the default credentials (postgres:DaVinci) for their server, security  generally isn't the biggest issue, but if you are trying to secure your project server, you will want to move to a supported version of Postgres.

Resolve still uses a legacy feature that has been removed in Postgres 12, so the latest major version that is useable is 11, which will be maintained until November 9, 2023. 


