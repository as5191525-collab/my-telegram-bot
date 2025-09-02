import telebot
from telebot import types
import os

# आपका बॉट का नया API टोकन
API_TOKEN = '8152346184:AAGU8rU7aEc3TI9c0r3t41zKfJh0mCfs6Xs'
bot = telebot.TeleBot(API_TOKEN)

# अपने चैनलों के यूज़रनेम यहाँ डालें
CHANNEL_1_USERNAME = '@adult_gril'
CHANNEL_2_USERNAME = '@neetphysics_by_spx'

def is_member(user_id):
    """
    जांच करता है कि क्या यूज़र दोनों चैनल्स का सदस्य है।
    """
    try:
        member1 = bot.get_chat_member(chat_id=CHANNEL_1_USERNAME, user_id=user_id).status
        is_member1 = member1 in ['member', 'creator', 'administrator']
        
        member2 = bot.get_chat_member(chat_id=CHANNEL_2_USERNAME, user_id=user_id).status
        is_member2 = member2 in ['member', 'creator', 'administrator']
        
        return is_member1 and is_member2
    except Exception as e:
        print(f"Error checking membership: {e}")
        return False

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    """
    हर नए मैसेज को हैंडल करता है।
    """
    user_id = message.from_user.id
    
    if not is_member(user_id):
        try:
            # यूज़र का मैसेज डिलीट करें
            bot.delete_message(message.chat.id, message.message_id)

            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton("➡️ Channel 1", url=f"https://t.me/{CHANNEL_1_USERNAME.strip('@')}"),
                types.InlineKeyboardButton("➡️ Channel 2", url=f"https://t.me/{CHANNEL_2_USERNAME.strip('@')}")
            )
            markup.row(
                types.InlineKeyboardButton("🐦 Twitter", url="https://x.com/tradershiva1?t=QRVkNJJIYzAfppHBaUA35A&s=09")
            )
            
            welcome_text = "Hey! 👋 To chat here, you must join both our channels first. 👇"
            bot.send_message(
                message.chat.id, 
                welcome_text,
                reply_markup=markup
            )
        except Exception as e:
            print(f"Error handling message: {e}")
    else:
        # अगर यूज़र पहले से ही सदस्य है, तो कुछ न करें
        pass

bot.polling()
