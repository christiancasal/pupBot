import discord
import os
import yfinance as yf

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith('!stonk'):
        try:
            args = message.content.split()
            stonk = yf.Ticker(args[1]);
            converted_num = '% s' % stonk.info['regularMarketPrice']
            await message.channel.send('stonk price: ' + converted_num)
        except:
            await message.channel.send('Oh no! Something went wrong!')

client.run(os.getenv('TOKEN'))