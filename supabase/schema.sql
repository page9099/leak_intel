-- Enable UUID generation extension
create extension if not exists "uuid-ossp";

-- User profiles
create table if not exists profiles (
  id uuid primary key default uuid_generate_v4(),
  username text unique not null,
  inserted_at timestamp with time zone default timezone('utc', now()) not null
);

-- Reported leaks
create table if not exists leaks (
  id uuid primary key default uuid_generate_v4(),
  profile_id uuid references profiles(id) on delete cascade,
  content text not null,
  inserted_at timestamp with time zone default timezone('utc', now()) not null
);

-- Files attached to leaks
create table if not exists leak_files (
  id uuid primary key default uuid_generate_v4(),
  leak_id uuid not null references leaks(id) on delete cascade,
  path text not null,
  inserted_at timestamp with time zone default timezone('utc', now()) not null
);
