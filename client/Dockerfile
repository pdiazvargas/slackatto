FROM node:14.15.0-alpine3.11

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update && apk add bash

COPY package.json /usr/src/app/package.json
# RUN npm install .
# ENV PATH /usr/src/app/node_module/.bin:$PATH