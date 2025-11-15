import os
import hashlib
import logging
import redis
from datetime import datetime
from typing import List, Dict, Any, Optional

# Setup logging
logging.basicConfig(level=logging.INFO)


class Evidence:
    def __init__(self, evidence_id: str, description: str, file_path: str):
        self.evidence_id = evidence_id
        self.description = description
        self.file_path = file_path
        self.md5_hash = self.compute_md5()
        self.sha256_hash = self.compute_sha256()
        
    def compute_md5(self) -> str:
        hasher = hashlib.md5()
        with open(self.file_path, 'rb') as file:
            hasher.update(file.read())
        return hasher.hexdigest()
    
    def compute_sha256(self) -> str:
        hasher = hashlib.sha256()
        with open(self.file_path, 'rb') as file:
            hasher.update(file.read())
        return hasher.hexdigest()


class Incident:
    def __init__(self, incident_id: str, description: str):
        self.incident_id = incident_id
        self.description = description
        self.evidence_list: List[Evidence] = []
        self.timeline_events: List[str] = []
        self.status = "Open"
        self.start_time = datetime.utcnow()
        

class ForensicsEngine:
    def __init__(self):
        self.incidents: Dict[str, Incident] = {}
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    def create_incident(self, incident_id: str, description: str):
        incident = Incident(incident_id, description)
        self.incidents[incident_id] = incident
        logging.info(f"Incident {incident_id} created.")
        
    def collect_evidence(self, incident_id: str, evidence_id: str, description: str, file_path: str):
        evidence = Evidence(evidence_id, description, file_path)
        self.incidents[incident_id].evidence_list.append(evidence)
        logging.info(f"Evidence {evidence_id} collected for incident {incident_id}.")

    def add_timeline_event(self, incident_id: str, event: str):
        self.incidents[incident_id].timeline_events.append(event)
        logging.info(f"Event added to timeline for incident {incident_id}: {event}")
        
    def reconstruct_attack(self, incident_id: str) -> List[str]:
        return self.incidents[incident_id].timeline_events

    def close_incident(self, incident_id: str):
        self.incidents[incident_id].status = "Closed"
        logging.info(f"Incident {incident_id} closed.")
        
    def generate_forensic_report(self, incident_id: str) -> Dict[str, Any]:
        incident = self.incidents[incident_id]
        report = {
            "Incident ID": incident.incident_id,
            "Description": incident.description,
            "Evidence": [(e.evidence_id, e.md5_hash, e.sha256_hash) for e in incident.evidence_list],
            "Timeline": incident.timeline_events,
            "Status": incident.status,
            "Start Time": incident.start_time.strftime('%Y-%m-%d %H:%M:%S'),
            "Creator": {
                "Name": "Thamer Aljadaan",
                "Email": "frankly.sa@gmail.com",
                "Phone": "+966597778968",
                "Date": "2025-11-15 06:22:33 UTC"
            }
        }
        logging.info(f"Generated report for incident {incident_id}.")
        return report


# Ensure evidence directory exists
os.makedirs('/data/evidence', exist_ok=True)

# Example usage (You can remove this in the production code)
if __name__ == "__main__":
    engine = ForensicsEngine()
    engine.create_incident("INC001", "Unauthorized access detected.")
    engine.collect_evidence("INC001", "EVID001", "Log file of the breach.", "/data/evidence/log.txt")
    engine.add_timeline_event("INC001", "Incident started.")
    report = engine.generate_forensic_report("INC001")
    print(report)