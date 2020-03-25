FROM tiangolo/uvicorn-gunicorn:python3.6

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY ./app /app