# Discord-Message-Sender-Classifier
A Discord Bot that can predict with 67% accuracy who sent a discord message between 5 users. Message Data from a 6 year old discord channel used by myself and friends were used to train a recurrent neural network. Discord is a platform similar to Microsoft Teams that is used to create communities and groups. It has easily accessible tools for developers to create applications such as bots to add to servers.

![Bot In Use](https://github.com/chenalan02/Discord-Message-Sender-Classifier/blob/main/Readme%20Images/Predictor%20Bot%20in%20Use.png)

## Gathering Data
A Discord bot was added the the server used to access, filter, and save the messages to a csv file. The code for this bot can be found in "Discord Message Collector.py". Messages were filtered to be 10 words or longer
