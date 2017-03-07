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

#### Run the elasticsearch container
```bash
docker-compose up elasticsearch
```
When elasticsearch has started, populate data

```bash
cd backend/
python manage.py init_data
```
#### Run the Flask container
```bash
docker-compose up server
```

#### Run the Angular container
```bash
docker-compose up frontend
```