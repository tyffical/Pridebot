    from sentimentsupport import get_sentiment
    #sentiment analysis disabled until a free api is found
    sentiment = os.environ['sentiment']
    #sentiment analysis
    
    print(str(message.content))
    get_sentiment(message.content) 
    if message.channel.id == sentiment_channel_id:
        
        #switch to match-case (aka switch) statements for python 3.10
        if score > 0:
            await message.add_reaction(custom_map["blaheart"])
        elif score == 0:
            await message.add_reaction(custom_map["melonBLAHAJ"])
        else:
            await message.add_reaction(custom_map["yaay"])









