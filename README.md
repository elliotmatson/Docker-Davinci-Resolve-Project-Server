# Davinci Resolve Project Server
Simple Resolve project server with automatic backups

## Table of Contents
- [Davinci Resolve Project Server](#davinci-resolve-project-server)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Features](#features)
  - [Backup Configuration](#backup-configuration)
  - [Installation](#installation)
    - [QNAP](#qnap)
    - [Synology](#synology)
    - [Linux](#linux)
  - [The Different PostgreSQL versions](#the-different-postgresql-versions)
    - [Using PostgreSQL 11 on Windows](#using-postgresql-11-on-windows)
    - [Using PostgreSQL on Mac](#using-postgresql-on-mac)

## Introduction

There are a lot of ways to host a Resolve project server, but each of them has their own set of issues. 

### Features
- **Lightweight** - Docker based, so doesn't require a full MacOS or Windows machine or VM.
- **Platform Independant** - can be installed on Windows, Mac, Linux, QNAP, Synology, RPi, really anything that can run Docker.
- **Compatible with Resolve's existing backup/restore functions** - All backup files use the standard *.backup file syntax that Resolve uses, unlike many of the PostgreSQL backup solutions that exist now.

## Backup Configuration

## Installation

### QNAP
(to be continued)

### Synology
(to be continued)

### Linux
(to be continued)


## The Different PostgreSQL versions
Generally, Resolve is not very tolerant of mismatched PostgreSQL verions. The Windows version of Resolve installs 9.5.4, and the Mac version installs 9.5.19. Unfortunately version 9.5 is EOL, and 9.5.4 in particular has a lot of vulnerabilities that make it insecure. Since most people are still using the default Resolve credentials for their server, security generally isn't the biggest concern, but if you are trying to secure your project server, you will want to move to a supported version of PostgreSQL.

Resolve still uses a legacy feature that has been removed in PostgreSQL 12, so the latest major version that is useable is 11, which will be maintained until November 9, 2023. 

### Using PostgreSQL 11 on Windows
1. **Uninstall PostgreSQL 9.5.4** - In your Windows application settings find PostgreSQL 9.5.4 and uninstall it.
2. **Download PostgreSQL 11** - Download the latest Windows version of PostgreSQL 11 from [the EDB Downloads Page](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and install it.
3. **Link Resolve to the new version** - Open Resolve, and connect to/open a PostgreSQL database. Start to run a database command (optimize, backup, restore) and Resolve will ask you to point it to PostgreSQL bin folder. This is inside the folder you picked in the PostgreSQL 11 installation, likely "C:\Program Files\PostgreSQL\11\bin"

### Using PostgreSQL on Mac
Unfortunately, Resolve on a Mac doesn't have a way to point to a different version of PostgreSQL. From my limited tests, it seems that you can still connect to a PostgreSQL 11 server from a Mac, you just won't be able to optimize, backup, or restore your database.