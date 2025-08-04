from fastapi import FastAPI, Query
from pydantic import BaseModel
from app.db import supabase

app = FastAPI(title="LeakIntel API v0")

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
    query = supabase.table("devices").select("*")
    if source:
        query = query.filter("reg_source", "in", f"({source})")
    return query.execute().data

@app.get("/v0/devices/{device_id}", response_model=Device)
def get_device(device_id: str):
    res = supabase.table("devices").select("*").eq("id", device_id).execute()
    if res.data:
        return res.data[0]
    return {"detail": "Not found"}
