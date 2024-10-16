import requests
impimport requests
import telebot
from telebot.types import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Mak

token = "7458990502:AAFnSDzRY6HObt2wqFHwyUlTZwiAgPe3yT4"
bot = telebot.TeleBot(token)

sent_video_messages = {}

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, '🔥 assalamo walaikum. You are welcome. You can download the following through the bot:

• Instagram - with stories, posts and IGTV + audio
• TikTok - video without watermark;
    ')

@bot.message_handler(content_types=['text'])
def Down(message):
    try:
    	link = message.text
    	json_data = {
    	    'url': link
    	}
    	response = requests.post('https://insta.savetube.me/downloadPostVideo', json=json_data).json()
    	thu = response['post_video_thumbnail']
    	video = response['post_video_url']
    	
    	sent_message = bot.send_photo(message.chat.id, thu, reply_to_message_id=message.message_id, reply_markup=Mak().add(Btn('Download video', callback_data='vid')))
    	
    	sent_video_messages[sent_message.message_id] = video
    except:
    	bot.reply_to(message,'Invalid link')

@bot.callback_query_handler(func=lambda call: call.data == 'vid')
def all(call):
    message_id = call.message.message_id
    if message_id in sent_video_messages:
        video = sent_video_messages[message_id]
        
        bot.delete_message(call.message.chat.id, call.message.message_id)
        Mn = f"[Contact](t.me/abd_khan01)"
        bot.send_video(call.message.chat.id,video,caption=Mn,parse_mode="Markdown")
        
bot.infinity_polling()
ort telebot
from telebot.types import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Mak

token = "7458990502:AAFnSDzRY6HObt2wqFHwyUlTZwiAgPe3yT4"
bot = telebot.TeleBot(token)

sent_video_messages = {}

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, '🔥 assalamo walaikum. You are welcome. You can download the following through the bot:

• Instagram - with stories, posts and IGTV + audio
• TikTok - video without watermark;
    ')

@bot.message_handler(content_types=['text'])
def Down(message):
    try:
    	link = message.text
    	json_data = {
    	    'url': link
    	}
    	response = requests.post('https://insta.savetube.me/downloadPostVideo', json=json_data).json()
    	thu = response['post_video_thumbnail']
    	video = response['post_video_url']
    	
    	sent_message = bot.send_photo(message.chat.id, thu, reply_to_message_id=message.message_id, reply_markup=Mak().add(Btn('Download video', callback_data='vid')))
    	
    	sent_video_messages[sent_message.message_id] = video
    except:
    	bot.reply_to(message,'Invalid link')

@bot.callback_query_handler(func=lambda call: call.data == 'vid')
def all(call):
    message_id = call.message.message_id
    if message_id in sent_video_messages:
        video = sent_video_messages[message_id]
        
        bot.delete_message(call.message.chat.id, call.message.message_id)
        Mn = f"[Contact](t.me/abd_khan01)"
        bot.send_video(call.message.chat.id,video,caption=Mn,parse_mode="Markdown")
        
bot.infinity_polling()
