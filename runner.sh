#!/usr/bin/env bash

# psql -U root -d mydb -a -f $1
sqlite3 base/college.db < $1
