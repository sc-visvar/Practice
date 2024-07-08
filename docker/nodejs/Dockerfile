#Selecting the server needed from dockerhub
FROM node:19-alpine

#Copying application code to the docker container
COPY package.json /app/
COPY src/. /app/src/

#Changing to the working directory
WORKDIR /app

#Installing the dependencies in the container
RUN npm install

#Running the app
CMD [ "node", "src/index.js" ]
