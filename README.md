# docker-learning
I am using podman as an engine

### For Docker version
```
docker version
```

### To search for a Docker image, Ubuntu, for instance, issue the following command:
```
docker search ubuntu
```

### docker run
```
docker run nginx
```

### Show running containers
```
docker ps
```

### Show all containers
```
docker ps -a
```
### Once the container ID has been obtained, you can start the container again with the command that was used to create it, by issuing the following command:
```
docker start 923a720da57f
```

### Stop the containers
```
docker stop nginx
```
### To stop a running container from the host session issue the following command:
```
docker kill 923a720da57f
```

### Remove the container
```
docker rm nginx
```

### Show images
```
docker images
```

### Remove the images
```
docker rmi nginx
```

### Download the image
```
docker pull nginx
```

### Append a command
```
docker run nginx sleep 5
```

### Execute a commannd on a running container
```
docker exec nginx cat /etc/hosts
```

### Detach command or running the container background
```
docker run -d nginx
```

### Attach a container
```
docker attach 8ce18649156e
```

### shell login in running container
```
docker run -it centos bash
```

### Docker compose file to container
```
docker-compose up -d
```

### Stop containers which are up by compose file
```
docker compose down
```

### Link two containers
```
docker run -d --name=vote -p 5000:80 --link redis:redis voting-app
```


### docker port mapping
```
docker run -p 80:5000 kodekloud/webapp
```

### Remember !!!
_extranal port : internal port. You can't map same port on docker host more than once_

### Default data file store on 
_/var/lib/mysql_

### Volume mapping for a container
```
docker run -v /opt/datadir:/var/lib/mysql mysql
```

### Remember !!!
_extranal vol : internal vol_

### Inspect a container
```
docker inspect 8ce18649156e
```

### Container log
```
docker logs 8ce18649156e
```

### Build an image from dockerfile
```
docker build . --file /home/nazmul/github/docker-learning/create_own_images/docker --tag test_flask
```

### Push images on Docker hub
```
docker tag test-node1 nazmulalam/test-node1
docker push nazmulalam/test-node1
```

### Run with env variable
```
docker run -e APP_COLOR=blue flask-env
```

### Remember !!!
_ENTRYPOINT is a task, when the container is running_

### Docker engine build by
```
    -   Docker CLI
    -   Rest API
    -   Docker Deamon
```

### Running a container with custom CPU and RAM
```
docker run --cpu=0.5 ubuntu
docker run --memory=100m ubuntu
```

### Docker default file system
```
    -   /var/lib/docker
        -   aufs
        -   containers
        -   images
        -   volumes
```

### Remember !!!
_Docker images layer is immutable and Docker containers layer is mutable_

### Create a volume
```
docker volume create data_volume
```

### Docker volume mount
```
docker run -v data_volume:/var/lib/mysql mysql
or
docker run -v /data/mysql:/var/lib/mysql mysql
or
docker run --mount type=bind, source=/data/mysql, target=/var/lib/mysql mysql
```

### Docker default network
    -   Bridge  docker run ubuntu
    -   None    docker run ubuntu   --network=none
    -   Host    docker run ubuntu   --network=host

### Create docker network
```
docker network create --driver bridge --subnet 182.80.0.0/16 coustom-isolated
```

### Inspect docker network
```
docker inspect coustom-isolated
```

### Deploy multiple replica containers with an image
```
docker service create --replicas=3 nginx
```

### Build or rebuild services
```
docker compose build
```

### Parse, resolve and render compose file in canonical format
```
docker compose config	
```

### Copy files/folders between a service container and the local filesystem
```
docker compose cp	
```

### Creates containers for a service.
```
docker compose create
```

### Stop and remove containers, networks	
```
docker compose down	
```

### Receive real time events from containers.
```
docker compose events	
```

### Execute a command in a running container.
```
docker compose exec	
```

### List images used by the created containers
```
docker compose images	
```

### Force stop service containers.
```
docker compose kill	
```

### View output from containers
```
docker compose logs	
```

### List running compose projects
```
docker compose ls	
```

### Pause services
```
docker compose pause
```

### List containers	
```
docker compose ps	
```

### Print the public port for a port binding.
```
docker compose port	
```

### Pull service images
```
docker compose pull
```

### Push service images	
```
docker compose push	
```

### Restart service containers
```
docker compose restart	
```

### Removes stopped service containers
```
docker compose rm	
```

### Run a one-off command on a service.
```
docker compose run	
```

### Start services
```
docker compose start	
```

### Stop services
```
docker compose stop	
```

### Display the running processes
```
docker compose top	
```

### Unpause services
```
docker compose unpause	
```

### Create and start containers
```
docker compose up
```

### Show the Docker Compose version information	
```
docker compose version
```
