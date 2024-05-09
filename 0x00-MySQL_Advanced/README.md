# MySQL Project for Ubuntu 18.04 with MySQL 5.7.30

## Description
This project contains SQL scripts designed for a MySQL 5.7.30 server running on Ubuntu 18.04 LTS. The scripts create and manipulate data in a simple database environment.

## Prerequisites
- Ubuntu 18.04 LTS
- MySQL 5.7.30
- SSH or WebTerminal access to a container running Ubuntu 18.04

## Usage
1. Connect to your Ubuntu 18.04 container.
2. Start the MySQL server with `service mysql start`.
3. Execute SQL scripts using the provided `my_database` database or create your own.

### Running SQL Scripts
To execute an SQL script, use the following command:
```shell
$ cat <script_name>.sql | mysql -uroot -p my_database
Enter password: ""
