
# Discord News Bot

A Discord bot that fetches the latest news article from [IT Vesti](https://www.itvesti.info), summarizes it using GPT-4, and delivers the summary directly to a Discord channel on demand.

---

## Features

- **`!news` command** — triggers the bot to fetch and summarize the latest news article
- **Web scraping** — automatically retrieves the most recent post from the configured news source
- **AI-powered summaries** — uses OpenAI's GPT-4 to condense articles into 2–3 concise sentences
- **Clean modular architecture** — bot, scraper, and summarizer are each in their own module

---

## Project Structure

```
discord-bot/
├── main.py          # Entry point — instantiates and runs the bot
├── bot.py           # Discord client, event handling, command logic
├── scraper.py       # Web scraper for fetching news content (BeautifulSoup)
└── summarizer.py    # OpenAI GPT-4 integration for text summarization
```

---

## Prerequisites

- Python 3.8+
- A [Discord bot token](https://discord.com/developers/applications)
- An [OpenAI API key](https://platform.openai.com/api-keys)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/petrowic-n/discord-bot.git
   cd discord-bot
   ```

2. **Install dependencies**

   ```bash
   pip install discord.py openai requests beautifulsoup4
   ```

3. **Configure your credentials**

   Open `main.py` and replace the placeholder values with your actual tokens:

   ```python
   from bot import DiscordBot

   bot = DiscordBot("YOUR_DISCORD_TOKEN", "YOUR_OPENAI_API_KEY")
   bot.run()
   ```

   > ⚠️ **Security note:** For production use, store credentials in environment variables or a `.env` file rather than hardcoding them. You can use the `python-dotenv` package for this.

---

## Usage

Start the bot by running:

```bash
python main.py
```

Once the bot is online in your Discord server, type the following command in any channel the bot has access to:

```
!news
```

The bot will respond with a brief acknowledgement, scrape the latest article, summarize it with GPT-4, and post the result.

---

## How It Works

1. A user sends `!news` in a Discord channel.
2. `bot.py` receives the message and calls `NewsScraper` with the news site URL.
3. `scraper.py` fetches the page, finds the most recent article link, retrieves its content, and returns the raw text.
4. `summarizer.py` sends the text to GPT-4 and returns a 2–3 sentence summary.
5. The bot posts the summary back to the channel.

---

## Dependencies

| Package | Purpose |
|---|---|
| `discord.py` | Discord API client |
| `openai` | GPT-4 summarization |
| `requests` | HTTP requests for scraping |
| `beautifulsoup4` | HTML parsing |

---

## License

This project is open source and available under the [MIT License](LICENSE).
