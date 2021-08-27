import discord
import pandas as pd

#message filter
def is_wanted_message (msg):
    if len(msg.content.split()) < 4:
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

#token not included on Github file for security concerns
TOKEN = ''

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #makes sure that only I can access bot
    elif message.author.name != 'Alan':
        return
    elif message.content.startswith("-"):
        cmd = message.content.split()[0].replace("-","")
        #initializes scan when keyword "-scan" used
        if cmd == 'scan':
            await message.channel.send('scanning...')
            data = pd.DataFrame(columns=['content', 'author'])

            #iterates through entire history of discord channel
            async for msg in message.channel.history(limit = None):

                if msg.author != client.user:
                    
                    if is_wanted_message(msg):
                        #adds message to dataframe if passes filter
                        data = data.append({'content': msg.content,
                                'author': msg.author.name},
                                ignore_index=True)

        #saves data to csv
        file_location = "data_long.csv"
        data.to_csv(file_location)
        await message.channel.send('scan done')
        print('scan done')

client.run(TOKEN)




