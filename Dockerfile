FROM python:latest
WORKDIR /usr/src/app
COPY . .
CMD ["python", "fizzbuzz.py"]