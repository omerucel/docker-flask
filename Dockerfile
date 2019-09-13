FROM python:3.6
WORKDIR /data/project
COPY requirements.txt /data/project
RUN pip install -r requirements.txt
CMD gunicorn app:app