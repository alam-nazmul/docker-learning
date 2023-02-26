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

