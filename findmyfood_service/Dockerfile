FROM tiangolo/uvicorn-gunicorn:python3.7

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE 80
COPY ./app /app