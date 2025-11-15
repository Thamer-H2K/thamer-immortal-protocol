# Thamer Immortal Protocol - Production Dockerfile
# Copyright © 2025 Thamer-H2K. All Rights Reserved.

FROM python:3.11-slim

# Metadata
LABEL maintainer="frankly.sa@gmail.com"
LABEL version="1.0.0"
LABEL description="Thamer Immortal Protocol - Self-Aware Cybersecurity AI"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create app directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpcap-dev \
    tcpdump \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY intelligence/requirements.txt /app/intelligence/
COPY api/requirements.txt /app/api/
COPY sensors/requirements.txt /app/sensors/

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r intelligence/requirements.txt && \
    pip install -r api/requirements.txt && \
    pip install -r sensors/requirements.txt

# Copy application code
COPY . /app/

# Create necessary directories
RUN mkdir -p /app/logs /app/data /app/models

# Set permissions
RUN chmod +x /app/main.py

# Expose ports
EXPOSE 8000 8001 9090

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# Run as non-root user
RUN useradd -m -u 1000 thamer && \
    chown -R thamer:thamer /app
USER thamer

# Start application
CMD ["python", "main.py"]