import telebot
import time


TOKEN = "TOKEN DADO PELO TELEGRAM"
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['painel']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Ola, seu plano vence amanha,caso queira renovar basta enviar o comprovante do pagamento para renovarmos')

while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
