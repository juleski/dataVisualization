# Data visualization app 

This app uses Flask, Elasticsearch and Angular 2

## Setup
Clone the repository
```bash
git clone git@github.com:juleski/dataVisualization.git
cd dataVisualization
```

### Running using docker
Install docker first. You can find how [here](https://docs.docker.com/engine/installation/)

You can run them all at once using docker-compose
```bash
docker-compose up -d
```

or run them individually:

#### Run the elasticsearch container
```bash
docker-compose up elasticsearch -d
```
#### Run the Flask container
```bash
docker-compose up server -d
```

#### Run the Angular container
```bash
docker-compose up frontend -d
```

When the servers are up, populate the data in Elasticsearch

```bash
cd backend/
python manage.py init_data
```