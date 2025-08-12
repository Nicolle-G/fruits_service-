README
- This is a REST service built with Flask and MongoDB that performs several CRUD operations, is containerized with Docker, and runs with Docker Compose.

How does it work?

1. The client sends an HTTP request (I made it with the REST Client extension), for example, using the POST method, to insert a new fruit with all its characteristics in JSON format.

2. The application receives the request at the /fruits route using the POST method and calls the create function.

3. The create function processes the data and calls the insert_fruit function, which uses MongoDB's insert_one method to save the fruit to the database.

4. In the Docker environment, it create two containers:
- mongo_bd: runs the MongoDB database.
- fruits_app: runs the Flask application.

5. MongoDB inserts a new document into the fruits collection.

6. The application responds to the client in JSON format, returning the ID generated for the successfully saved fruit.

Run
- To start the containers (database and application), I use the Docker Compose command:
sudo docker compose up --build

Requirements

1. Install Docker Engine
- Make sure Docker Engine is installed and running on your computer.

2. Create the application image
- by creating a Dockerfile from a base Python image.
- In this file, everything necessary to install dependencies and run the Flask application was configured using Dockerfile syntax.

3. Configure Docker Compose
- Create the docker-compose.yml file to define and run multiple containers:
- mongo_bd: MongoDB container that automatically downloads the latest version from Docker Hub (a repository of already created images).
- fruits_app: Container that runs the Flask application.

Use volumes
- First, define a mongo_data volume for MongoDB data persistence.
- This ensures that the data is stored in the /data/db path and is not lost even if the container or image is deleted.