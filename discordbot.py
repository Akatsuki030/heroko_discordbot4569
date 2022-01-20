    if message.author.bot:
        return
    
    if client.user in message.mentions: # @判定
        translator = googletrans.Translator()
        robotName = client.user.name
        first, space, language, content = message.clean_content.partition('@'+robotName+'tw: '+'') 

        
        if content == '':
            content = first
        
      

        if translator.detect(content).lang == SRCLanguage or SRCLanguage == '':
            remessage = translator.translate(content, dest= 'zh_TW').text
            await message.reply(remessage) 

    
# Bot起動
client.run(TOKEN)
