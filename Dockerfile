FROM python:3.13-slim

COPY requirements.txt /build/requirements.txt

RUN apt update && \
    apt install --no-install-recommends -y git wget && \
    pip install --no-cache-dir -r /build/requirements.txt && \
    apt clean && apt autoclean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY . /code

CMD python main.py