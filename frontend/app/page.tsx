'use client';

import useSWR from 'swr';

type Device = {
  id: string;
  brand: string;
  model: string;
  reg_source: string;
  first_seen?: string;
};

const fetcher = (url: string) => fetch(url).then((r) => r.json());

export default function Home() {
  const { data, error } = useSWR<Device[]>('/api/devices', fetcher);

  if (error) return <p className="text-red-600 p-4">failed to load</p>;
  if (!data) return <p className="text-gray-500 p-4">loading…</p>;

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">LeakIntel – Device List</h1>

      <table className="w-full border text-sm">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2 text-left">ID</th>
            <th className="p-2 text-left">Brand</th>
            <th className="p-2 text-left">Model</th>
            <th className="p-2 text-left">Source</th>
          </tr>
        </thead>
        <tbody>
          {data.map((d) => (
            <tr key={d.id} className="border-b hover:bg-gray-50">
              <td className="p-2">{d.id}</td>
              <td className="p-2">{d.brand}</td>
              <td className="p-2">{d.model}</td>
              <td className="p-2 uppercase">{d.reg_source}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}
