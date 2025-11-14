# Thamer Immortal Protocol - Intelligence Docker Image
# Copyright © 2025 Thamer-H2K. All Rights Reserved.
# Contact: frankly.sa@gmail.com

FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY brain.py .

RUN useradd -r -s /bin/false thamer && \
    chown -R thamer:thamer /app

USER thamer

CMD ["python", "-u", "brain.py"]