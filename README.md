# ParcelGate

This API project manages offers & brokers on a list of parcels (Parcel of Land). It includes functionality to create, read, update, and delete offers associated with parcels. Additionally, it features a background job that monitors the count of parcels in each combination of block number and subdivision number, triggering notifications when all parcels in a combination have active offers. Unit tests and authentication mechanisms are also implemented for security and quality assurance.

# Tech Stack

- Python
- Django
- Postgresql
- Celery
- RabbitMQ
- Docker

# Modular Monolith Architecture

The application is built using a modular monolith architecture approach. While it is a monolithic application, it is structured in a modular way, allowing for better organization and separation of concerns within the codebase. Each module encapsulates related functionality, promoting code reusability and maintainability while still benefiting from the simplicity of a monolithic deployment.

# Application Directory Hierarchy

```
modular-monolith
    ├── backend                      # primary backend service
    │   ├── land_broker_hub          # land_broker_hub root namespace
    │   │   ├── broker               # broker application/module 
    │   │   ├── data                 # fixtures container
    │   │   ├── offer                # offer application/module 
    │   │   ├── parcel               # parcel application/module 
    │   │   ├── settings             # application settings
    │   │   └── tests                # application tests
    │   ├── scripts                  # application scripts
    └── webserver                    # application webserver
```

# Dockerized Flavor

The application is available in a Dockerized flavor, allowing for easy deployment and management in containerized environments.

# Infrastructure Setup & Installation

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
foo@bar:~$ docker compose exec backend ./scripts/bootstrap.sh
```
5. You can also run the tests via:

```console
foo@bar:~$ docker compose exec backend python manage.py tests
```
   
# JWT Authentication for API Security

API resources are protected with JWT (JSON Web Token) authentication scheme, ensuring secure access to the endpoints.

# Swagger UI for API Documentation

The application includes Swagger UI for API documentation, providing an interactive interface to explore and test the API endpoints.

-  You can access the Swagger UI by navigating to `http://localhost:8060/api/schema/swagger-ui/` for desired API documentation
-  Use the interactive interface to explore and test the API endpoints
-  Complete Open API specification is available at `modular-monolith/backend/api_spec.yaml`

# Consume / Invoke API endpoints

After setting up the application, you can access the all the endpoints using Swagger UI OR any API client. Below is the API response for the Offers endpoint which supports the filters and pagination options:

API Target: `http://localhost:8060/offers/?expand=broker,parcels`

![image](https://github.com/asifpy/ParcelGate/assets/6741984/d384edeb-d5b2-428e-9f4d-74dd8a51e4b9)

# High-Level Architecture

![image](https://github.com/asifpy/ParcelGate/assets/6741984/e2963d14-2f32-4f60-b7db-8803c7e765ee)







