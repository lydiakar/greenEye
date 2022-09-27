FROM node:16

WORKDIR /app
COPY package*.json ./
COPY . .

# Node app port
EXPOSE 3000

RUN npm install

CMD [ "npm", "run", "start" ]