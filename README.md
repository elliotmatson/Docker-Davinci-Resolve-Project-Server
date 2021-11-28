# Davinci Resolve Project Server
Simple Resolve project server with automatic backups

## Table of Contents
- [Davinci Resolve Project Server](#davinci-resolve-project-server)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Features](#features)
  - [Configuration](#configuration)
  - [Installation](#installation)
    - [QNAP Installation](#qnap-installation)
    - [Synology](#synology)
    - [Linux](#linux)
  - [The Different PostgreSQL versions](#the-different-postgresql-versions)
    - [Setting up a PostgreSQL 11 Project Server](#setting-up-a-postgresql-11-project-server)
    - [Using PostgreSQL 11 on Windows](#using-postgresql-11-on-windows)
    - [Using PostgreSQL on Mac](#using-postgresql-on-mac)
  - [Thanks](#thanks)

## Introduction

There are a lot of ways to host a Resolve project server, but each of them has their own set of issues. The official project server requires manual backups, and other options can be complicated for those that don't have access to an IT team. Hopefully this is a simpler solution for smaller teams!

### Features
- **Lightweight** - Docker based, so doesn't require a full MacOS or Windows machine or VM.
- **Platform Independent** - can be installed on Windows, Mac, Linux, QNAP, Synology, RPi, really anything that can run Docker.
- **Compatible with Resolve's existing backup/restore functions** - All backup files use the standard *.backup file syntax that Resolve uses, unlike many of the PostgreSQL backup solutions that exist now.

## Configuration

## Installation

### QNAP Installation
Installing on a QNAP NAS is relatively simple:
1. If you don't already have it, install Container Station from the QNAP app store.
2. In Container Station, click "Create", then click "Create Application"
3. Name your application whatever you like (eg. ResolveServer)
4. Copy/Paste your modified docker-compose.yml file, hit "Validate YAML" to test it, and if it passes, click "Create"
5. Container Station will download the files it needs and start the app. If it doesn't autostart after ~5 minutes, try clicking the play button for your app on the Overview tab
   

### Synology
(to be continued)

### Linux
(to be continued)


## The Different PostgreSQL versions
Generally, Resolve is not very tolerant of mismatched PostgreSQL versions. The Windows version of Resolve installs 9.5.4, and the Mac version installs 9.5.19. Unfortunately the major release 9.5 is EOL, and 9.5.4 in particular has a lot of vulnerabilities that make it insecure. Since most people are still using the default Resolve credentials for their server, security generally isn't the biggest concern, but if you are trying to secure your project server, you will want to move to a supported version of PostgreSQL.

Resolve still uses a legacy feature that has been removed in PostgreSQL 12, so the latest major version that is useable is 11, which will be maintained until November 9, 2023. 

### Setting up a PostgreSQL 11 Project Server
To setup a PostgreSQL 11 server instead of 9.5, there are 2 lines that need to be changed in docker_compose.yml:
```yaml
services:
  postgres:
    image: postgres:9.5
    ...
  pgbackups:
    image: prodrigestivill/postgres-backup-local:9.5
    ...
...
```
to the following:
```yaml
services:
  postgres:
    image: postgres:11
    ...
  pgbackups:
    image: prodrigestivill/postgres-backup-local:11
    ...
...
```
### Using PostgreSQL 11 on Windows
1. **Uninstall PostgreSQL 9.5.4** - In your Windows application settings find PostgreSQL 9.5.4 and uninstall it.
2. **Download PostgreSQL 11** - Download the latest Windows version of PostgreSQL 11 from [the EDB Downloads Page](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and install it.
3. **Link Resolve to the new version** - Open Resolve, and connect to/open a PostgreSQL database. Start to run a database command (optimize, backup, restore) and Resolve will ask you to point it to PostgreSQL bin folder. This is inside the folder you picked in the PostgreSQL 11 installation, likely "C:\Program Files\PostgreSQL\11\bin"

### Using PostgreSQL on Mac
Unfortunately, Resolve on a Mac doesn't have a way to point to a different version of PostgreSQL. From my limited tests, it seems that you can still connect to a PostgreSQL 11 server from a Mac, you just won't be able to optimize, backup, or restore your database.
## Thanks
-[prodrigestivill](https://github.com/prodrigestivill/) for his [PostgreSQL Backup docker image](https://github.com/prodrigestivill/docker-postgres-backup-local)