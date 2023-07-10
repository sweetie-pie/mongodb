# Chapter 6: Install

In here we learn how to setup ```MongoDB``` cluster on local on connecto to our
cluster with ```Python``` application.

## Mongodb Cluster

In order to setup a ```MongoDB``` cluster we are using ```Docker``` images and ```docker-compose```.
First we need to pull our docker image:

```shell
docker pull mongo:6-jammy
```

Now we are creating a docker-compose file:

```yaml
services:
  mongodb:
    container_name: monogdb
    image: mongo:6-jammy
    ports:
      - '27017:27017'
    volumes:
      - dbdata6:/data/db
```

Now can access database on ```mongodb:27017``` on our host.

## Python app

First we need to install ```pymongo``` library using ```pip install pymongo```. After
that we can connect to our cluster with following command:

```python
import pymongo

# connecting to mongodb
client = pymongo.MongoClient("mongodb://mongodb:27017/")
```
