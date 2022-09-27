## Run the web server

1. Build the docker image, run from repo root -
    `docker build frontend -t web-app`
2. Start the server - `docker run -p 3000:3000 -d web-app`

## Run the kmean service

1. Build the docker image, run from repo root -
    `docker build kmean -t kmean-service`
2. Start the server - `docker run -t -p 3001:5000 -d kmean-service`

## open browser and go to `http://localhost:3000/`

