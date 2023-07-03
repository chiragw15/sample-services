# Simple Node.js App

This is a simple Node.js application that provides a `/ping` API endpoint and connects to

 a MySQL database and Redis.

## Prerequisites

Ensure that you have the following installed on your machine:

- [Node.js and npm](https://nodejs.org/en/download/)
- [Docker](https://www.docker.com/products/docker-desktop)

Also ensure that you have a MySQL and Redis instance running and accessible.

## Setup

Clone the repository and navigate into the directory:

```shell
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

Replace the placeholders in the `.env` file with your MySQL and Redis credentials:

```text
MYSQL_DATABASE_USER=user
MYSQL_DATABASE_PASSWORD=password
MYSQL_DATABASE_DB=database
MYSQL_DATABASE_HOST=host
REDIS_URL=redis://:password@localhost:6379/0
```

## Docker

### Building Docker Image

Build the Docker image from the root of the project directory:

```shell
docker build -t my-node-app .
```

This command builds the Docker image using the Dockerfile in the current directory and names the image `my-node-app`.

### Running the Docker Container

Run the Docker container:

```shell
docker run -p 5000:5000 --env-file .env my-node-app
```

This command runs the Docker container, mapping your machine's port 5000 to the container's port 5000. It also sets the environment variables using the `.env` file.

The Node.js app will be accessible at `http://localhost:5000`.

## API

The application provides the following endpoint:

### GET /ping

Checks if the MySQL and Redis connections are working.

Response codes:
- 200: MySQL and Redis are working properly.
- 500: An error occurred.

```

Remember to replace `https://github.com/yourusername/your-repo.git` with the actual URL of your repository.