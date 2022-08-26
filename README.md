# cine-data

### Requisitos previos

> pip install requests

## Create the React App
npx create-react-app .

## Build the container
```
docker build -t curso-bd-bi .
```

# Node Scripts
## Container for Node React App Instance
## START WEB
```
docker run -it --rm -u node -w /home/node/app -v ${PWD}:/home/node/app -p 8080:8080 curso-bd-bi npm run web
```
## START SERVER
```
docker run -it --rm -u node -w /home/node/app -v ${PWD}:/home/node/app -p 8181:8181 curso-bd-bi npm run server
```
## INSTALL
```
docker run -it --rm -u node -w /home/node/app -v ${PWD}:/home/node/app -p 8080:8080 -p 8181:8181 curso-bd-bi npm install
```
## BASH/SHELL
```
docker run -it --rm -u node -w /home/node/app -v ${PWD}:/home/node/app -p 8080:8080 -p 8181:8181 curso-bd-bi bash
```