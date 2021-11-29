# Davinci Resolve Project Server
Simple Resolve project server with automatic backups

## Table of Contents
- [Davinci Resolve Project Server](#davinci-resolve-project-server)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Features](#features)
  - [Configuration](#configuration)
    - [PostgreSQL Server](#postgresql-server)
    - [Backup Server](#backup-server)
  - [Installation](#installation)
    - [QNAP Installation](#qnap-installation)
    - [Synology](#synology)
    - [Linux](#linux)
  - [Different PostgreSQL versions](#different-postgresql-versions)
    - [Setting up a PostgreSQL 11 Project Server](#setting-up-a-postgresql-11-project-server)
    - [Using PostgreSQL 11 on Windows](#using-postgresql-11-on-windows)
    - [Using PostgreSQL 11 on Mac](#using-postgresql-11-on-mac)
  - [Thanks](#thanks)

## Introduction

There are a lot of ways to host a Resolve project server, but each of them has their own set of issues. The official project server requires manual backups, and other options can be complicated for those that don't have access to an IT team. Hopefully this is a more reliable and simpler solution for smaller teams!

### Features
- **Lightweight** - Docker based, so doesn't require a full MacOS or Windows machine or VM.
- **Platform Independent** - can be installed on Windows, Mac, Linux, QNAP, Synology, RPi, really anything that can run Docker.
- **Compatible with Resolve's existing backup/restore functions** - All backup files use the standard Resolve *.backup file syntax, and can be restored from the Resolve UI

## Configuration
There are a few things we'll need to edit in the docker-compose.yml file to configure our installation:
### PostgreSQL Server
To configure the server itself, we'll want to configure the environment variables below:
```yaml
...
services:
  postgres:
    ...
    environment:
      - POSTGRES_DB=database
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=DaVinci
      - TZ=America/Chicago
    ...
...
```
| Environment Variable  |Meaning|
|---|---|
| POSTGRES_DB       | This is the name of your database. Name it whatever you like. |
| POSTGRES_USER     | This is the username you will use to connect to your database. The Resolve default is "postgres"  |
| POSTGRES_PASSWORD | This is the password you will use to connect to your database. The Resolve default is "DaVinci"  |
| TZ                | This is your timezone, here is [a list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)|

### Backup Server
To configure the backups, we'll want to configure the variables below:
```yaml
...
services:
  ...
  pgbackups:
    ...
    volumes:
      - "(Whatever location you want backups stored):/backups"
    ...
    environment:
      - POSTGRES_HOST=postgres
      - POSTGRES_DB=database
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=DaVinci
      - POSTGRES_EXTRA_OPTS=--blobs --format=custom --quote-all-identifiers
      - BACKUP_SUFFIX=.backup
      - SCHEDULE=@daily
      - BACKUP_KEEP_DAYS=7
      - BACKUP_KEEP_WEEKS=4
      - BACKUP_KEEP_MONTHS=6
      - HEALTHCHECK_PORT=8080
      - TZ=America/Chicago
    ...
...
```
First, we will want to decide on a backup location and edit the ```volumes:``` section. You will need the full path to the folder you want backups stored in. On a QNAP NAS for example, if I wanted to use a folder called "Backups" inside a shared folder named "Videos", the path would be ```/shares/Videos/Backups/```, and my ```volumes:``` section would look like this:
```yaml
volumes:
      - "/shares/Videos/Backups:/backups"
```
 On Ubuntu, if I wanted to use a folder named "Backups" in the home directory of the user named "johndoe", the path would be ```/home/johndoe/Backups/```, and my ```volumes:``` section would look like this:
```yaml
volumes:
      - "/home/johndoe/Backups:/backups"
```




There are also some variables in the environment section. Many of these don't need to be edited, but here are the ones you might want to change:
| Environment Variable  |Meaning|
|---|---|
| POSTGRES_DB | This is the name of the database from the previous step. Can also be a comma/space separated list of database names if you create more in the future |
| POSTGRES_USER | This is the database username from the previous step |
| POSTGRES_PASSWORD | This is the database password from the previous step |
| SCHEDULE | This is a [cron string](https://www.freeformatter.com/cron-expression-generator-quartz.html) for how often backups are created. can be "@daily", "@every 1h", etc |
| BACKUP_KEEP_DAYS | Number of daily backups to keep before removal.
| BACKUP_KEEP_WEEKS | Number of weekly backups to keep before removal.
| BACKUP_KEEP_MONTHS | Number of daily backups to keep before removal.
| TZ                | This is your timezone, here is [a list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)|

Once you have configured these settings, save your modified docker-compose.yml file and move on to installation!

## Installation

### QNAP Installation
Installing on a QNAP NAS is relatively simple:
1. If you don't already have it, install Container Station from the QNAP app store.
2. In Container Station, click "Create", then click "Create Application"
3. Name your application whatever you like (eg. ResolveServer)
4. Copy/Paste your modified docker-compose.yml file, hit "Validate YAML" to test it, and if it passes, click "Create"
5. Container Station will download the files it needs and start the app. Once it's done, you should be able to connect Resolve to the IP address of your QNAP using the database name and credentials
   

### Synology
(to be continued)

### Linux
1. Follow the [Docker installation instructions for your Linux distribution](https://docs.docker.com/engine/install/)
2. Install [Docker Compose](https://docs.docker.com/compose/install/)
3. Move your modified docker-compose.yml file to a folder on your Linux machine, then navigate to that folder in the terminal. 
4. Run: 
```docker-compose up -d```
5. Docker-compose will download the files it needs and start the app. Once it's done, you should be able to connect Resolve to the IP address of your QNAP using the database name and credentials


## Different PostgreSQL versions
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

### Using PostgreSQL 11 on Mac
Unfortunately, Resolve on a Mac doesn't have a way to point to a different version of PostgreSQL. From my limited tests, it seems that you can still connect to a PostgreSQL 11 server from a Mac, you just won't be able to optimize, backup, or restore your database.
## Thanks
-[prodrigestivill](https://github.com/prodrigestivill/) for his [PostgreSQL Backup docker image](https://github.com/prodrigestivill/docker-postgres-backup-local)