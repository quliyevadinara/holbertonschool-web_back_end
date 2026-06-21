# NoSQL

## Background Context

NoSQL databases became popular as the internet grew, and traditional
relational (SQL) databases started struggling with the speed and
scale of incoming data. This project covers the basics of MongoDB,
a popular NoSQL document database, both through the `mongo` shell and
through Python using `PyMongo`.

## Requirements

### MongoDB Command File

* All files will be executed on Ubuntu 18.04 LTS using MongoDB (version 4.2)
* All files should end with a new line
* The first line of all files should be a comment: `// my comment`
* A `README.md` file at the root of the folder of the project is mandatory
* The length of the files will be tested using `wc`

### Python Scripts

* All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7) and `PyMongo` (version 3.10)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/env python3`
* A `README.md` file at the root of the folder of the project is mandatory
* Your code should use the `pycodestyle` style (version 2.5.*)
* All your modules and functions should have documentation

## Setup

### Install MongoDB 4.2 in Ubuntu 18.04

    $ sudo apt-get update
    $ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
    $ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
    $ sudo apt-get update
    $ sudo apt-get install -y mongodb-org
    $ sudo service mongod start

### Install PyMongo

    $ pip3 install pymongo

### Restoring the sample log data (for task 12)

    $ curl -o dump.zip -s "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-webstack/411/dump.zip"
    $ unzip dump.zip
    $ mongorestore dump

> Note: since MongoDB 4.4, tools like `mongorestore` are distributed
> separately as the MongoDB Database Tools. Install from
> https://www.mongodb.com/try/download/database-tools if needed.

## Tasks

| # | Task | File |
|---|------|------|
| 0 | List all databases | 0-list_databases |
| 1 | Create a database | 1-use_or_create_database |
| 2 | Insert document | 2-insert |
| 3 | All documents | 3-all |
| 4 | All matches | 4-match |
| 5 | Count | 5-count |
| 6 | Update | 6-update |
| 7 | Delete by match | 7-delete |
| 8 | List all documents in Python | 8-all.py |
| 9 | Insert a document in Python | 9-insert_school.py |
| 10 | Change school topics | 10-update_topics.py |
| 11 | Where can I learn Python? | 11-schools_by_topic.py |
| 12 | Log stats | 12-log_stats.py |

## Usage

### Mongo shell scripts (tasks 0–7)

    $ cat 0-list_databases | mongo
    $ cat 2-insert | mongo my_db

### Python scripts (tasks 8–12)

    $ ./12-log_stats.py