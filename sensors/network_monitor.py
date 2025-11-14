#!/usr/bin/env python3
"""
Thamer Immortal Protocol - Network Monitoring Sensor
Copyright © 2025 Thamer Aljadaan (CyberX). All Rights Reserved.
Contact: frankly.sa@gmail.com | +966597778968

This module monitors network traffic for suspicious activities.
"""

import asyncio
import logging
import socket
from datetime import datetime
from typing import Dict, List
import psutil

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("NetworkMonitor")


class NetworkMonitor:
    """Monitors network traffic and detects anomalies"""
    
    def __init__(self):
        self.suspicious_ips = set()
        self.connection_count = {}
        self.alert_threshold = 100
        
    async def start(self):
        """Start network monitoring"""
        logger.info("🌐 Network Monitor - Starting...")
        logger.info(f"📊 Alert Threshold: {self.alert_threshold} connections")
        
        while True:
            await self.scan_connections()
            await asyncio.sleep(5)
    
    async def scan_connections(self):
        """Scan active network connections"""
        try:
            connections = psutil.net_connections(kind='inet')
            active_ips = {}
            
            for conn in connections:
                if conn.raddr:
                    ip = conn.raddr.ip
                    active_ips[ip] = active_ips.get(ip, 0) + 1
            
            # Check for suspicious activity
            for ip, count in active_ips.items():
                if count > self.alert_threshold:
                    self.report_suspicious(ip, count)
            
            if len(active_ips) > 0:
                logger.debug(f"📡 Active connections: {len(connections)} from {len(active_ips)} IPs")
                
        except Exception as e:
            logger.error(f"❌ Error scanning connections: {e}")
    
    def report_suspicious(self, ip: str, count: int):
        """Report suspicious IP activity"""
        if ip not in self.suspicious_ips:
            self.suspicious_ips.add(ip)
            logger.warning(f"⚠️ SUSPICIOUS: {ip} with {count} connections!")
            logger.warning(f"🚨 Total suspicious IPs: {len(self.suspicious_ips)}")
    
    def get_network_stats(self) -> Dict:
        """Get current network statistics"""
        net_io = psutil.net_io_counters()
        return {
            "bytes_sent": net_io.bytes_sent,
            "bytes_recv": net_io.bytes_recv,
            "packets_sent": net_io.packets_sent,
            "packets_recv": net_io.packets_recv,
            "suspicious_ips": len(self.suspicious_ips)
        }


async def main():
    """Main entry point"""
    monitor = NetworkMonitor()
    
    try:
        await monitor.start()
    except KeyboardInterrupt:
        logger.info("\n⚠️ Shutting down Network Monitor...")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
