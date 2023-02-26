# docker-learning
I am using podman as an engine


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

### Stop the containers
```
docker stop nginx
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
docker build --file /home/nazmul/github/docker-learning/create_own_images/docker --tag test_flask
```