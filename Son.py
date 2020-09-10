import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.game("테스트봇")
    await client.change_presence(status=discord.status.offline)


@client.event
async def on_message(message):
    if message.content.startswith("할말"):
        await message.channel.send("대답")
        if message.content.startswith("할말"):
            await message.channel.send("대답")


client.run("NzUzMjI2MTcyOTA4Njk5NzI5.X1jGiQ.IQXSazUQfKUHTyCPt1yyVivKhbU")
