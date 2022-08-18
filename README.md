# cine-data

### Requisitos previos

> pip install requests

## Create the React App
npx create-react-app .

# Node Scripts
## Container for Node React App Instance
## START
```
docker run -it --rm -u node -w /home/node/app -v ${PWD}:/home/node/app -p 3000:3000 node:18-bullseye npm start
```
## INSTALL
```
docker run -it --rm -u node -w /home/node/app -v ${PWD}:/home/node/app -p 3000:3000 node:18-bullseye npm install
```