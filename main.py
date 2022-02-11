import re
from urllib import request
import discord
import os
import json
import random
import requests
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()


def get_greetings():
    response = requests.get('https://gdsc-rait-discord-bot-api-psych-hack.vercel.app/greetings')
    json_response = json.loads(response.text)
    print(json_response['message'])
    return json_response['message']


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

greetings = [ "hello", "hi", 'hie', "hey","good morning", "good evening"]

@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        #If the last message sent was from the bot itself, don't do anything
        return
    msg = message.content.lower()

    if any(word in msg for word in greetings):
        greeting_responses = get_greetings()
        await message.channel.send(greeting_responses)
    
    
token = os.getenv('DISCORD_TOKEN')
client.run(token)