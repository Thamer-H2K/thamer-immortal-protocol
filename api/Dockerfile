# Thamer Immortal Protocol - API Dockerfile.
# Copyright © 2025 Thamer Aljadaan (CyberX). All Rights Reserved.
# Contact: frankly.sa@gmail.com | +966597778968

FROM python:3.11-slim

LABEL maintainer="Thamer Aljadaan (CyberX) <frankly.sa@gmail.com>"
LABEL description="Thamer Immortal Protocol - API Module"
LABEL version="1.0.0"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY websocket.py .

RUN echo '#!/bin/bash\n\
echo "╔═══════════════════════════════════════════════════════════════╗"\n\
echo "║  🌐 Thamer Immortal Protocol - API Server                    ║"\n\
echo "║  👤 Creator: Thamer Aljadaan (CyberX)                        ║"\n\
echo "║  📧 Email: frankly.sa@gmail.com                              ║"\n\
echo "║  📱 Phone: +966597778968                                     ║"\n\
echo "║  📅 Date: 2025-11-14 19:01:17 UTC                            ║"\n\
echo "╚═══════════════════════════════════════════════════════════════╝"\n\
echo "🚀 Starting FastAPI Server..."\n\
python server.py' > /app/start.sh && chmod +x /app/start.sh

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["/app/start.sh"]
