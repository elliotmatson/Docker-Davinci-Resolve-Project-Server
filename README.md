
<div align="right">
  <details>
    <summary >🌐 Language</summary>
    <div>
      <div align="center">
        <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=en">English</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=zh-CN">简体中文</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=zh-TW">繁體中文</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=ja">日本語</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=ko">한국어</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=hi">हिन्दी</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=th">ไทย</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=fr">Français</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=de">Deutsch</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=es">Español</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=it">Italiano</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=ru">Русский</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=pt">Português</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=nl">Nederlands</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=pl">Polski</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=ar">العربية</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=fa">فارسی</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=tr">Türkçe</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=vi">Tiếng Việt</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=id">Bahasa Indonesia</a>
        | <a href="https://openaitx.github.io/view.html?user=elliotmatson&project=Docker-Davinci-Resolve-Project-Server&lang=as">অসমীয়া</
      </div>
    </div>
  </details>
</div>

# Davinci Resolve Project Server

![Lint](https://github.com/elliotmatson/Docker-Davinci-Resolve-Project-Server/actions/workflows/lint.yml/badge.svg)
![Healthcheck](https://github.com/elliotmatson/Docker-Davinci-Resolve-Project-Server/actions/workflows/stack-healthcheck.yml/badge.svg)
![Docker Build](https://github.com/elliotmatson/Docker-Davinci-Resolve-Project-Server/actions/workflows/docker.yml/badge.svg)

Simple Resolve project server with automatic backups

## Table of Contents

- [Davinci Resolve Project Server](#davinci-resolve-project-server)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Features](#features)
  - [Configuration](#configuration)
    - [Database](#database)
    - [Backups](#backups)
    - [PGAdmin](#pgadmin)
    - [Volume Locations](#volume-locations)
  - [Installation](#installation)
    - [QNAP Installation](#qnap-installation)
    - [Synology](#synology)
    - [Linux](#linux)
  - [Different PostgreSQL versions](#different-postgresql-versions)
    - [Setting up a PostgreSQL 9.5 or 11 Project Server](#setting-up-a-postgresql-95-or-11-project-server)
  - [Thanks](#thanks)

## Introduction

There are a lot of ways to host a Resolve project server, but each of them has their own set of issues. The official project server requires manual backups, and other options can be complicated for those that don't have access to an IT team. Hopefully this is a more reliable and simpler solution for smaller teams!

### Features

- **Lightweight** - Docker based, so doesn't require a full macOS or Windows machine or VM.
- **Platform Independent** - can be installed on Windows, Mac, Linux, QNAP, Synology, RPi, really anything that can run Docker.
- **Compatible with Resolve's existing backup/restore functions** - All backup files use the standard Resolve \*.backup file syntax, and can be restored from the Resolve UI
- **Built-in PGAdmin Server** - PGAdmin is a tool for administering a PostgreSQL Server, and is helpful for diagnosing problems and migrating/updating entire servers

## Configuration

There are a few things we'll need to edit at the top of the docker-compose.yml file to configure our installation:

```yaml
---
version: "3.8"
x-common:
  database: &db-environment
    POSTGRES_DB: database
    POSTGRES_USER: &pg-user postgres
    POSTGRES_PASSWORD: DaVinci
    TZ: America/Chicago
    POSTGRES_LOCATION: &db-location "???:/var/lib/postgresql/data"
  backup: &backup-environment
    SCHEDULE: "@daily"
    BACKUP_KEEP_DAYS: 7
    BACKUP_KEEP_WEEKS: 4
    BACKUP_KEEP_MONTHS: 6
    BACKUP_LOCATION: &bk-location "???:/backups"
  admin: &admin-environment
    PGADMIN_DEFAULT_EMAIL: admin@admin.com
    PGADMIN_DEFAULT_PASSWORD: root
    PGADMIN_PORT: &pgadmin-port "3001:80"
```

### Database

To configure the server itself, we'll want to configure the environment variables below:
| Environment Variable |Meaning|
|---|---|
| POSTGRES_DB | Name of your database. Name it whatever you like. |
| POSTGRES_USER | Username you will use to connect to your database. The Resolve default is "postgres" |
| POSTGRES_PASSWORD | Password you will use to connect to your database. The Resolve default is "DaVinci" |
| TZ | Your timezone, here is [a list](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)|
| POSTGRES_LOCATION | Location your database will be stored. See [Volume Locations](#volume-locations) |

### Backups

To configure the backups, we'll want to configure the variables below:
| Environment Variable |Meaning|
|---|---|
| SCHEDULE | This is a [cron string](https://www.freeformatter.com/cron-expression-generator-quartz.html) for how often backups are created. can be "@daily", "@every 1h", etc |
| BACKUP_KEEP_DAYS | Number of daily backups to keep before removal. |
| BACKUP_KEEP_WEEKS | Number of weekly backups to keep before removal. |
| BACKUP_KEEP_MONTHS | Number of monthly backups to keep before removal. |
| BACKUP_LOCATION | Location your backups will be stored. See [Volume Locations](#volume-locations) |

### PGAdmin

To configure PGAdmin, we'll want to configure the variables below:
| Environment Variable |Meaning|
|---|---|
| PGADMIN_DEFAULT_EMAIL | Email used for PGAdmin login. Default is "admin@admin.com" |
| PGADMIN_DEFAULT_PASSWORD | Password used for PGAdmin login. Default is "root" |
| PGADMIN_PORT | String configuring port to expose PGAdmin on. Syntax is "YOUR_PORT:80" |

### Volume Locations

The location of your database and backups depend on what platform you are installing on. You will need the full path to the folder you want them stored in. On a QNAP NAS for example, if I wanted to use a folder called "Backups" inside a shared folder named "Videos" for my backups location, the path would be `/shares/Videos/Backups/`, and my `BACKUP_LOCATION` value would look like this:

```yaml
BACKUP_LOCATION: &bk-location "/shares/Videos/Backups/:/backups"
```

On Ubuntu, if I wanted to use a folder named "database" in the home directory of the user named "johndoe" for my database location, the path would be `/home/johndoe/database/`, and my `POSTGRES_LOCATION` value would look like this:

```yaml
POSTGRES_LOCATION: &db-location "johndoe/database/:/var/lib/postgresql/data"
```

I recommend putting your database on an SSD, your access speed will be noticeably slower on a spinning drive.

Once you have configured these settings, save your modified docker-compose.yml file and move on to installation!

## Installation

### QNAP Installation

Installing on a QNAP NAS is relatively simple. One note, please put the database files on an SSD. You will thank me later

1. If you don't already have it, install Container Station from the QNAP app store.
2. In Container Station, click "Create", then click "Create Application"
3. Name your application whatever you like (eg. ResolveServer)
4. Copy/Paste your modified docker-compose.yml file, hit "Validate YAML" to test it, and if it passes, click "Create"
5. Container Station will download the files it needs and start the app. Once it's done, you should be able to connect Resolve to the IP address of your QNAP using the database name and credentials

### Synology

See [this discussion](https://github.com/elliotmatson/Docker-Davinci-Resolve-Project-Server/discussions/15#discussioncomment-4615278)

### Linux

1. Follow the [Docker installation instructions for your Linux distribution](https://docs.docker.com/engine/install/)
2. Install [Docker Compose](https://docs.docker.com/compose/install/)
3. Move your modified docker-compose.yml file to a folder on your Linux machine, then navigate to that folder in the terminal.
4. Run:
   `docker-compose up -d`
5. Docker-compose will download the files it needs and start the app. Once it's done, you should be able to connect Resolve to the IP address of your Linux Server instance using the database name and credentials

## Different PostgreSQL versions

Generally, Resolve is not very tolerant of mismatched PostgreSQL versions. Resolve 18 uses PostgreSQL 13, which is what this repository now defaults to. Resolve 17 and below use PostgreSQL 9.5. Unfortunately the major release 9.5 is EOL, and 9.5.4 in particular has a lot of vulnerabilities that make it insecure.
Since most people are still using the default Resolve credentials for their server, security generally isn't the biggest concern, but if you are trying to secure your project server with an older version of Resolve, you will want to move to a supported version of PostgreSQL.

Resolve 17 and below still use a legacy feature that has been removed in PostgreSQL 12, so the latest major version that is useable is 11, which will be maintained until November 9, 2023.

### Setting up a PostgreSQL 9.5 or 11 Project Server

To setup a PostgreSQL 9.5 or 11 server instead of 13, there are 2 lines that need to be changed in docker_compose.yml:

```yaml
services:
  postgres:
    image: postgres:13
    ...
  pgbackups:
    image: prodrigestivill/postgres-backup-local:13
    ...
...
```

to the following:

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

## Thanks

-[prodrigestivill](https://github.com/prodrigestivill/) for his [PostgreSQL Backup docker image](https://github.com/prodrigestivill/docker-postgres-backup-local)
