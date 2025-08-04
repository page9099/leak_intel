from fastapi import FastAPI, Query
from pydantic import BaseModel
from pathlib import Path
import json

app = FastAPI(title="LeakIntel API v0")

# --- mock data ---------------------------------
DATA_PATH = Path(__file__).parent / "devices_mock.json"
MOCK = json.loads(DATA_PATH.read_text())

class Device(BaseModel):
    id: str
    brand: str
    model: str
    reg_source: str
    first_seen: str | None = None
    ai: dict | None = None
    attributes: dict | None = None

@app.get("/v0/devices", response_model=list[Device])
def list_devices(source: str | None = Query(None, description="Comma-separated reg_source filter")):
    if source:
        allowed = set(source.split(","))
        return [d for d in MOCK if d["reg_source"] in allowed]
    return MOCK

@app.get("/v0/devices/{device_id}", response_model=Device)
def get_device(device_id: str):
    for d in MOCK:
        if d["id"] == device_id:
            return d
    return {"detail": "Not found"}
