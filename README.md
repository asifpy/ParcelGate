# ParcelGate

This API project manages offers & brokers on a list of parcels (Parcel of Land). It includes functionality to create, read, update, and delete offers associated with parcels. Additionally, it features a background job that monitors the count of parcels in each combination of block number and subdivision number, triggering notifications when all parcels in a combination have active offers. Unit tests and authentication mechanisms are also implemented for security and quality assurance.

# Tech Stack

- Python
- Django
- Postgresql
- Celery
- RabbitMQ
- Docker

# Modular Architecture

The application follows a modular architecture, allowing for better organization and scalability of code. Each component of the application, such as models, views, serializers, and tasks, is organized into separate modules or packages, promoting code reusability and maintainability.

# Dockerized Flavor

The application is available in a Dockerized flavor, allowing for easy deployment and management in containerized environments.

# Infrastructre Setup & Installation

1. Clone the repository:
```console
foo@bar:~$ git clone https://github.com/asifpy/ParcelGate.git
```

2. Navigate to the project directory:
```console
foo@bar:~$ cd ParcelGate/modular-monolith
```

3. Run the Docker Compose command to build and start the services:
```console
foo@bar:~$ docker compose up --build
````

4. Application boostraping to setup the DB and load the initial fixtures
```console
foo@bar:~$ docker-compose exec backend ./scripts/bootstrap.sh
```



