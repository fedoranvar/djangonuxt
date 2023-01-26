# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.9-alpine AS builder
EXPOSE 8000
WORKDIR /app 
COPY backend/requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir

# COPY . /app 
