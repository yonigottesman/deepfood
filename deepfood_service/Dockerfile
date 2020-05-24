FROM tiangolo/uvicorn-gunicorn:python3.7

WORKDIR /app
COPY requirements.txt /app

EXPOSE 80
COPY ./app /app

RUN mkdir app/models/
RUN wget --output-document=app/models/model.pt  https://deepfood.s3-us-west-2.amazonaws.com/model.pt
RUN wget --output-document=app/models/index.ann https://deepfood.s3-us-west-2.amazonaws.com/tree_5.ann
RUN pip install -r requirements.txt 