import discord
from scraper import NewsScraper
from summarizer import Summarizer

class DiscordBot:
    def __init__(self, token, api_key):
        self.token = token
        self.api_key = api_key

        intents = discord.Intents.default()
        intents.message_content = True
        
        self.client = discord.Client(intents=intents)

        self.client.event(self.on_ready)
        self.client.event(self.on_message)

    async def on_ready(self):
        print(f"Logged in as {self.client.user}")
    
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.content == "!news":
            await message.channel.send("Wait a min, preparing data...")

            scraper = NewsScraper("https://www.itvesti.info/search?max-results=1")
            news_data = scraper.scrape()

            summarizer = Summarizer(self.api_key)
            summary = summarizer.summarize(news_data)

            await message.channel.send(summary)
        
    def run(self):
        self.client.run(self.token)
