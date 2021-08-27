import discord
import pandas as pd
import pickle
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

name_dict = {
    0: "Alan",
    1: "Nick",
    2: "Eric",
    3: "Jason",
    4: "Jaden"
}

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = tf.keras.models.load_model("Discord Message Classifier 67%.h5")

TOKEN = 'ODc5ODQ4NjMwMDc1NDA4NDA0.YSVs5A.Tiw-kMSQv3o0xRhWwc0GjV0DWRA'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith("-"):
        cmd = message.content.split()[0].replace("-","")

        if cmd == 'guess':
            sentence = [message.content.split()[1:]]
            sentence = tokenizer.texts_to_sequences(sentence)
            sentence = pad_sequences(sentence, maxlen= 123)
            name_idx = int((model.predict(sentence).argmax(axis=1)))
            name = name_dict[name_idx]
            await message.channel.send(name)

client.run(TOKEN)




