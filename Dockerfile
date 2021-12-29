FROM python:3.9

LABEL maintainer="lala"

RUN apt-get update

WORKDIR /app

COPY . .

CMD ["python", "pip", "install", "requests"]