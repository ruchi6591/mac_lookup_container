FROM python:3.7-alpine

COPY ./mac_lookup /mac_lookup
WORKDIR /mac_lookup

RUN pip install requests

ENV PYTHONPATH=/mac_lookup

ENTRYPOINT ["python3","main.py"]