import requests #typeignore
#Lembrar de baixar o package requests - pip install requests

def telegram_bot_sendtext(bot_message):

   bot_token = 'Your token bot here' # Colocar o Token do bot obtido ao criar
   bot_chatID = 'Your chat ID'
    # Colocar o Chat ID do conversa, voce consegue obter o mesmo olhando na documentacao, mas apenas colcocar a url no browser

   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()


test = telegram_bot_sendtext("Colocar alguma mensagem") 
# Enviando mensagem
print(test)

