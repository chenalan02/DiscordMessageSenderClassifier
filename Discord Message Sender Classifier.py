import discord
import pandas as pd
import pickle
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#name mappings for tensorflow prediction output
name_dict = {
    0: "Alan",
    1: "Nick",
    2: "Eric",
    3: "Jason",
    4: "Jaden"
}
#open tokenizer and model
with open("Classifier Files/tokenizer.pickle", 'rb') as handle:
    tokenizer = pickle.load(handle)
model = tf.keras.models.load_model("Classifier Files/Discord Message Classifier 67%.h5")

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

    elif message.content.startswith("-"):
        cmd = message.content.split()[0].replace("-","")
        #initialize a prediction with keyword '-guess'
        if cmd == 'guess':
            #preprocessing
            sentence = [message.content.split()[1:]]
            sentence = tokenizer.texts_to_sequences(sentence)
            sentence = pad_sequences(sentence, maxlen= 123)

            #model prediction
            name_idx = int((model.predict(sentence).argmax(axis=1)))
            
            #output to discord
            name = name_dict[name_idx]
            msg = "Prediction: " + name
            await message.channel.send(msg)

client.run(TOKEN)




