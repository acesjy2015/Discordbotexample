import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print("디스코드 봇 로그인 성공.")
	print("봇 이름 : " + client.user.name)
	print("봇 ID : " + str(client.uwer.id))
	await
client.change_presence(status=discord.Status.online,
activit=discord.Game("서술"))

@client.event
async def on_message(message):
	content = message.content
	guild = message.guild
	author = message.author
	channel = message.channel
if content.startwith("!케를"):
	await message.channel.send("음머어ㅓ어어ㅓ어어ㅓ")
client.run('')
