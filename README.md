# cine-data

### Requisitos previos

> pip install requests

## Create the React App
npx create-react-app .

# Node Scripts
## Container for Node React App Instance
## START WEB
```
docker run -it --rm -u node -w /home/node/app -v ${PWD}:/home/node/app -p 8080:8080 -p 8181:8181 node:18-bullseye npm run web
```
## START SERVER
```
docker run -it --rm -u node -w /home/node/app -v ${PWD}:/home/node/app -p 8080:8080 -p 8181:8181 node:18-bullseye npm run server
```
## INSTALL
```
docker run -it --rm -u node -w /home/node/app -v ${PWD}:/home/node/app -p 8080:8080 -p 8181:8181 node:18-bullseye npm install
```
## BASH/SHELL
```
docker run -it --rm -u node -w /home/node/app -v ${PWD}:/home/node/app -p 8080:8080 -p 8181:8181 node:18-bullseye bash
```