# leak_intel

This is for testing purpose only.

## Slack Bot

### Install
1. Create a new Slack App using the manifest at `bot/manifest.yml`.
2. Install dependencies:
   ```bash
   pip install slack_bolt
   ```
3. Set the following environment variables with your app credentials:
   * `SLACK_BOT_TOKEN`
   * `SLACK_APP_TOKEN`
4. Run the bot:
   ```bash
   python bot/app.py
   ```


## Crawler

### Install
1. Install dependencies:
   ```bash
   pip install scrapy
   ```
2. Run the FCC spider and output JSON lines to stdout:
   ```bash
   scrapy crawl fcc -O -:jsonlines
   ```

