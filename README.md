# MySQLDocker
For making custom [MySQL](https://www.mysql.com/) containers to run on Docker Compose.

- the data is persisted into a subdirectory
- the root password is stored in the `.env` file
- the container is run on its own [bridge network](https://docs.docker.com/network/bridge/) as is the default

Requires [Docker](https://www.docker.com/) and the [Cookiecutter](https://www.cookiecutter.io/) Python package.

## To set up the server

On the command line, run
`cookiecutter https://github.com/agentlans/MySQLDocker`

Answer the questions
```
container_name [mysql-database]: magical-db
root_password [SqueamishOssifrage]: Azkaban
port [3306]:
```
## To run the server

Go into the newly-created directory and start the container.
```bash
cd magical-db
docker compose up
```
Type `Ctrl + C` to stop the container.

## Python client

The Python client is optional. You should be able to access
the database using other MySQL clients.

To set up the dependencies for the Python client:

`sudo pip install -r client-requirements.txt`

To run the client:

`python client.py`

Shouldn't have any errors.

# Author, Licence

Creative Commons Zero by Alan Tseng
