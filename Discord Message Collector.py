import discord
import pandas as pd

# Checking if the message is a command call
def is_wanted_message (msg):
    if len(msg.content.split()) < 6:
        return False
    elif msg.content.startswith("-"):
        return False
    elif msg.content.startswith("@"):
        return False
    elif msg.content.startswith("https"):
        return False
    elif msg.author.name not in ["Alan", "nicholas", "tree.", "Jason4Hear", 'jaden']:
        return False
    else:
        return True

TOKEN = 'ODYwNjA5NTMwNzY1MjQ2NDk0.YN9vFQ.VnoRe6ODwJsTk4R2kWx4DA8Zlz8'

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.author.name != 'Alan':
        return
    elif message.content.startswith("-"):
        cmd = message.content.split()[0].replace("-","")
        
        if cmd == 'scan':
            await message.channel.send('scanning...')
            data = pd.DataFrame(columns=['content', 'author'])

            #length = 100000
            #counter = 1
            async for msg in message.channel.history(limit = None):
                #if counter == length/4:
                #    await message.channel.send("scan 25% done")
                #elif counter == length/2:
                #    await message.channel.send("scan 50% done")
                #elif counter == 3*(length/4):
                #    await message.channel.send("scan 75% done")

                if msg.author != client.user:
                    
                    if is_wanted_message(msg):
                        data = data.append({'content': msg.content,
                                'author': msg.author.name},
                                ignore_index=True)
                
                #counter += 1

        file_location = "data_long.csv"
        data.to_csv(file_location)
        await message.channel.send('scan done')
        print('scan done')

client.run(TOKEN)




