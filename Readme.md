## Run with docker

```
# build docker container and tag it with task1
docker build . -f Dockerfile -t task1

# run docker container
docker run task1 <mac_address>

# example 
docker run --env-file=.env task1 44:38:39:ff:ef:57

```


## Please use below commands to run locally

```

1. Please add API key in environment after installing enviromnet with required packages using "pip install -r requirements.txt" command.
2. Run task using "python task1.py <mac_address>"

```