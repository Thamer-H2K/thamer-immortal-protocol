# Thamer Immortal Protocol - Sensors Dockerfile
# Copyright © 2025 Thamer Aljadaan (CyberX). All Rights Reserved.
# Contact: frankly.sa@gmail.com | +966597778968

FROM python:3.11-slim

LABEL maintainer="Thamer Aljadaan (CyberX) <frankly.sa@gmail.com>"
LABEL description="Thamer Immortal Protocol - Sensors Module"
LABEL version="1.0.0"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpcap-dev \
    net-tools \
    procps \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY network_monitor.py .
COPY system_monitor.py .

RUN echo '#!/bin/bash\n\
echo "🔍 Thamer Immortal Protocol - Sensors"\n\
echo "👤 Creator: Thamer Aljadaan (CyberX)"\n\
echo "📧 Contact: frankly.sa@gmail.com"\n\
echo "📱 Phone: +966597778968"\n\
echo ""\n\
echo "🌐 Starting Network Monitor..."\n\
python network_monitor.py &\n\
echo "🖥️ Starting System Monitor..."\n\
python system_monitor.py &\n\
wait' > /app/start.sh && chmod +x /app/start.sh

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \ 
    CMD ps aux | grep -E "network_monitor|system_monitor" || exit 1

CMD ["/app/start.sh"]