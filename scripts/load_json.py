import json, sys, os, pathlib
from supabase import create_client

url  = os.getenv("SUPABASE_URL")
key  = os.getenv("SUPABASE_SERVICE_ROLE") or os.getenv("SUPABASE_ANON_KEY")
assert url and key, "Supabase env vars missing"

supabase = create_client(url, key)
path = pathlib.Path(sys.argv[1])

rows = json.loads(path.read_text())
for row in rows:
    # 最低限 id があれば upsert 可能
    supabase.table("devices").upsert(row, on_conflict="id").execute()

print(f"Upserted {len(rows)} rows.")
