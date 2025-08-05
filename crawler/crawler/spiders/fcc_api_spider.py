import scrapy
import json
from datetime import datetime

API_BASE = "https://api.fcc.gov/oet/ea/fccid/"


def build_url(grantee: str, product: str) -> str:
    return f"{API_BASE}{grantee}/{product}"


class FccApiSpider(scrapy.Spider):
    name = "fcc_api"
    custom_settings = {"DOWNLOAD_DELAY": 0.3}

    # 直近 24h に登録された可能性が高いグランティコードのみを例示
    start_grantees = ["UXD", "2AQM", "2AB8"]

    def start_requests(self):
        for grantee in self.start_grantees:
            url = f"https://api.fcc.gov/oet/ea/fccid?q={grantee}&size=5"
            yield scrapy.Request(url, callback=self.parse_search, meta={"grantee": grantee})

    def parse_search(self, response):
        data = json.loads(response.text)
        for hit in data.get("results", []):
            fid = hit["fcc_id"]  # e.g., "UXD25003"
            grantee, product = fid[:3], fid[3:]
            yield scrapy.Request(build_url(grantee, product), callback=self.parse_detail)

    def parse_detail(self, response):
        info = json.loads(response.text)
        yield {
            "id": info["fcc_id"],
            "brand": info.get("applicant"),
            "model": info.get("model"),
            "reg_source": "fcc",
            "first_seen": datetime.utcnow().date().isoformat(),
            "attributes": {
                "frequency": info.get("frequency_range"),
                "power": info.get("rf_output_power"),
            },
            "ai": None,
        }
