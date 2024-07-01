# Crime Statistics in France

This repository contains several modules for downloading gendarmerie data on crime in France by department and offers a web application for visualizing various statistics. Among other features, it allows you to view the number of crimes classified by type of crime by department and by year.

## Project Overview

This project was developed as part of my studies in a group setting. It aims to provide an accessible platform for analyzing crime data in France using web technologies.

## Prerequisites

- Docker
- Unix-based OS (for non-Docker usage)
- Web browser

## Getting Started

### Using Docker

To run this application using Docker, you need to build the Docker image with the following command:

```sh
docker build -t crime_en_france .
```

Then, run the Docker container with:

```sh
docker run -p 8050:8050 crime_en_france
```

### Without Docker

If you prefer to run the application without Docker, use the scripts available at the root of the project: `install.sh` and `launch.sh`. Note that these scripts require a Unix-based OS.

First, execute the `install.sh` script to pre-install and prepare the environment:

```sh
./install.sh
```

Then, launch the application with:

```sh
./launch.sh
```

These scripts will handle data retrieval and management before starting the web application.

## Accessing the Application

After starting the container or the web platform without the container, open a web browser and navigate to the following URL: [http://localhost:8050](http://localhost:8050)



