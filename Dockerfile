FROM python:3.5

#RUN apk add --update python py-pip

#COPY app.yaml /app/src/app.yaml
EXPOSE 8080
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

COPY . /app

ENV PYTHONPATH /app/src

CMD python /app/app.py

