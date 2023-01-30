FROM node:19.5.0

RUN npm install -g npm@9.4.0
RUN npm install -g @vue/cli
RUN npm install -g create-vite
# RUN npm install -g nuxi@3.1.1
RUN npm install -g pnpm
RUN mkdir /app && chown node:node /app

USER node

WORKDIR /app

# ENTRYPOINT ["npm"]
# CMD ["run dev"]
