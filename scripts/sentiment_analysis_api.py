    #sentiment analysis disabled until a free api is found
    # sentiment = os.environ['sentiment']
    # #sentiment analysis
    # r = requests.post(
    #     "https://api.deepai.org/api/sentiment-analysis",
    #     data={
    #         'text': message.content,
    #     },
    #     headers={'api-key': sentiment})
    # print(str(message.content))
    # print(r.json()) #prints out id and output: formated as array of ['verypositive/positive/neutral/negative/verynegative']
    # if message.channel.id == sentiment_channel_id:
    #     sentiment = str(r.json()["output"][0]).lower()
    #     #switch to match-case (aka switch) statements for python 3.10
    #     if sentiment == "verypositive" or sentiment == "positive":
    #         await message.add_reaction(custom_map["blaheart"])
    #     elif sentiment == "neutral":
    #         await message.add_reaction(custom_map["melonBLAHAJ"])
    #     else:
    #         await message.add_reaction(custom_map["yaay"])