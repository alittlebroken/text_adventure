# Pokehampton Text Adventure Docker Container
FROM python:3.8-slim
MAINTAINER Paul Lockyer
WORKDIR /code
COPY src/ .
CMD ["python", "./main.py"]