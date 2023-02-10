FROM  python:3.9-alpine AS builder
EXPOSE 8000
WORKDIR /app 
COPY backend/requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip install httpie

FROM builder as backend
COPY . /app 
ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
