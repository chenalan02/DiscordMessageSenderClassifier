# Discord-Message-Sender-Classifier
A Discord Bot that can predict with 67% accuracy who sent a discord message between 5 users. Message Data from a 6 year old discord channel used by myself and friends were used to train a recurrent neural network. Discord is a platform similar to Microsoft Teams that is used to create communities and groups. It has easily accessible tools for developers to create applications such as bots to add to servers.

![Bot In Use](https://github.com/chenalan02/Discord-Message-Sender-Classifier/blob/main/Readme%20Images/Predictor%20Bot%20in%20Use.png)

## Gathering Data
A Discord bot was added the the server used to access, filter, and save the messages to a csv file. The csv file was not included in this repository for privacy reasons. The code for this bot can be found in "Discord Message Collector.py". Links and bot commands were filtered out. Messages were also filtered to be 10 words or longer. Originally, sentences of length 3 or greater were used but achieved lesser results. This was likely due to the fact that there are many common, short phrases we all use such as "join the call" or "be on later". Longer phrases allow the bot to focus more on particular grammar structures used accross users. Even when the training data was of length 3 or greater, results were about the same, even though more data was used to train.

![Bot In Use](https://github.com/chenalan02/Discord-Message-Sender-Classifier/blob/main/Readme%20Images/Original%20Data%20Distribution.png)

The user nicholas had about twice as much message data than everyone else. To prevent this data inbalance, about 500 of his messages were removed from the data. There was not a noticible loss of accuracy from this loss in data.
