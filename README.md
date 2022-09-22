# Flask Mongo

## Database setup

This repository assumes that you're running a MongoDB database on `cloud.mongodb.com`.

Make sure you've done the following:

1. Set up a project
2. Set up a cluster within that project
3. Set up a database
4. Created a user for that database, with a password
5. Allowed the database to accept connections from your specific IP

## Environment variables

In a `.env` file, ensure the following variables are present:

```zsh
DB_PASSWORD=XXXXXXXXXX
DB_USER=XXXXXXXXXX
PROJECT_NAME=XXXXXXXXXX
DB_HOST=XXXXXXXXXX
DB_NAME=XXXXXXXXXX
```

Get the `DB_HOST` value from the connection strings found by clicking 'connect' on the project page.

## Installation

`pipenv install`

## Development

`pipenv run dev`