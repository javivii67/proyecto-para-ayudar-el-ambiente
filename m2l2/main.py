import discord
from bot_logic import *

intents = discord.Intents.default()
#
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('?hello'):
        await message.channel.send('¡Hola! Soy un bot que ayuda a mejor un poco mas el planeta, o bueno aporto mi granito de arena, empecemos con algo basico como un consejo, escribe "?consejo".')
    elif message.content.startswith('?consejo'):
         await message.channel.send(consejo_uno())

    
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")

client.run ("toket aqui")