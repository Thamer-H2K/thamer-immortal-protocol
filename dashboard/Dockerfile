# Thamer Immortal Protocol - Dashboard Dockerfile
# Copyright © 2025 Thamer Aljadaan (CyberX). All Rights Reserved.
# Contact: frankly.sa@gmail.com | +966597778968

FROM nginx:alpine

LABEL maintainer="Thamer Aljadaan (CyberX) <frankly.sa@gmail.com>"
LABEL description="Thamer Immortal Protocol - Dashboard"
LABEL version="1.0.0"

COPY index.html /usr/share/nginx/html/
COPY style.css /usr/share/nginx/html/
COPY app.js /usr/share/nginx/html/

RUN echo 'server {\n\
    listen 80;\n\
    server_name localhost;\n\
    root /usr/share/nginx/html;\n\
    index index.html;\n\
    \n\
    location / {\n\
        try_files $uri $uri/ /index.html;\n\
    }\n\
    \n\
    location /api {\n\
        proxy_pass http://api:8000;\n\
        proxy_set_header Host $host;\n\
    }\n}' > /etc/nginx/conf.d/default.conf

RUN echo '#!/bin/sh\n\
echo ""\n\
echo "╔═══════════════════════════════════════════════════════════════╗"\n\
echo "║  🎨 Thamer Immortal Protocol - Dashboard                     ║"\n\
echo "║  👤 Creator: Thamer Aljadaan (CyberX)                        ║"\n\
echo "║  📧 Email: frankly.sa@gmail.com                              ║"\n\
echo "║  📱 Phone: +966597778968                                     ║"\n\
echo "║  🇸🇦 Location: Saudi Arabia                                  ║"\n\
echo "║  📅 Date: 2025-11-14 19:17:24 UTC                            ║"\n\
echo "╚═══════════════════════════════════════════════════════════════╝"\n\
echo ""\n\
echo "🌐 Starting Dashboard on http://localhost:80"\n\
ginx -g "daemon off;"' > /start.sh && chmod +x /start.sh

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \n    CMD wget --quiet --tries=1 --spider http://localhost/ || exit 1

CMD ["/start.sh"]