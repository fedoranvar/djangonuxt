FROM node:lts-alpine as builder

RUN npm install -g npm@9.4.0
RUN npm install -g @vue/cli
RUN npm install -g create-vite
RUN npm install -g pnpm

RUN mkdir /app && chown node:node /app
USER node
WORKDIR /app

FROM builder as frontend
COPY . /app 
ENTRYPOINT ["pnpm"]
CMD ["run dev"]
