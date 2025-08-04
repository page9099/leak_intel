import os
from supabase import create_client, Client  # type: ignore

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise RuntimeError("Supabase environment variables not set")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

