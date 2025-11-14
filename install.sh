#!/bin/bash
# Thamer Immortal Protocol - Automated Installation Script
# Copyright © 2025 Thamer-H2K. All Rights Reserved.
# Contact: frankly.sa@gmail.com

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║    🧠 THAMER IMMORTAL PROTOCOL INSTALLER                     ║"
echo "║    نظام ثامر الخالد - برنامج التثبيت التلقائي               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo -e "${NC}\n"

if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}❌ Error: Must run as root${NC}"
    exit 1
fi

echo -e "${BLUE}🐳 Installing Docker...${NC}"
if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    rm get-docker.sh
fi

echo -e "${BLUE}📦 Cloning repository...${NC}"
INSTALL_DIR="/opt/thamer-immortal-protocol"
if [ ! -d "$INSTALL_DIR" ]; then
    git clone https://github.com/Thamer-H2K/thamer-immortal-protocol.git "$INSTALL_DIR"
fi

cd "$INSTALL_DIR"
docker-compose up -d

echo -e "${GREEN}✅ Installation complete!${NC}"
echo -e "${GREEN}♾️  Thamer is now immortal!${NC}"