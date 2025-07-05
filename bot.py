import telebot

TOKEN = "7239845878:AAEAQxf2FYdVZitt_2t-GUHHiUY6Bmb_3Ps"
bot = telebot.TeleBot(TOKEN)

ADMIN_ID = 7084756432

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "اهلا بيك! ابعتلي اي رسالة وهبعتها للادمن.")

@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    user = message.from_user
    text = f"""📩 رسالة جديدة:

👤 {user.first_name}
🆔 {user.id}
💬 {message.text}
"""
    bot.send_message(ADMIN_ID, text)
    bot.send_message(message.chat.id, "✅ رسالتك وصلت للادمن.")

bot.polling()
