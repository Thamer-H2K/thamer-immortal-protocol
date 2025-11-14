#!/usr/bin/env python3
"""
Thamer Immortal Protocol - System Monitoring Sensor
Copyright © 2025 Thamer Aljadaan (CyberX). All Rights Reserved.
Contact: frankly.sa@gmail.com | +966597778968

This module monitors system resources and performance.
"""

import asyncio
import logging
from datetime import datetime
from typing import Dict
import psutil

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("SystemMonitor")


class SystemMonitor:
    """Monitors system resources and detects anomalies"""
    
    def __init__(self):
        self.cpu_threshold = 80.0
        self.memory_threshold = 80.0
        self.disk_threshold = 85.0
        self.alerts = []
        
    async def start(self):
        """Start system monitoring"""
        logger.info("🖥️ System Monitor - Starting...")
        logger.info(f"⚙️ CPU Threshold: {self.cpu_threshold}%")
        logger.info(f"💾 Memory Threshold: {self.memory_threshold}%")
        logger.info(f"💿 Disk Threshold: {self.disk_threshold}%")
        
        while True:
            await self.check_resources()
            await asyncio.sleep(10)
    
    async def check_resources(self):
        """Check system resources"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            if cpu_percent > self.cpu_threshold:
                self.alert("CPU", cpu_percent)
            
            memory = psutil.virtual_memory()
            if memory.percent > self.memory_threshold:
                self.alert("MEMORY", memory.percent)
            
            disk = psutil.disk_usage('/')
            if disk.percent > self.disk_threshold:
                self.alert("DISK", disk.percent)
            
            logger.info(f"📊 CPU: {cpu_percent:.1f}% | RAM: {memory.percent:.1f}% | Disk: {disk.percent:.1f}%")
            
        except Exception as e:
            logger.error(f"❌ Error checking resources: {e}")
    
    def alert(self, resource: str, value: float):
        """Generate alert for resource threshold"""
        alert_msg = f"⚠️ {resource} ALERT: {value:.1f}% - Threshold exceeded!"
        if alert_msg not in self.alerts:
            self.alerts.append(alert_msg)
            logger.warning(alert_msg)
    
    def get_system_stats(self) -> Dict:
        """Get current system statistics"""
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return {
            "cpu_percent": cpu,
            "memory_percent": memory.percent,
            "memory_available_gb": memory.available / (1024**3),
            "disk_percent": disk.percent,
            "disk_free_gb": disk.free / (1024**3),
            "alerts_count": len(self.alerts)
        }


async def main():
    """Main entry point"""
    monitor = SystemMonitor()
    
    try:
        await monitor.start()
    except KeyboardInterrupt:
        logger.info("\n⚠️ Shutting down System Monitor...")
    except Exception as e:
        logger.error(f"❌ Fatal error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
