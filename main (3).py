import telebot, registration, buton
from geopy import Nominatim

bot = telebot.TeleBot('6356825506:AAGkLOPwCrcwZns16EBI7wgh1NeNzNeBwRA')
geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
@bot.message_handler(commands=['start'])
def start(message):
    global user_id
    user_id = message.from_user.id

    check_user = registration.checker(user_id)
    if check_user:
        bot.send_message(user_id, f'Welcome back {user}', reply_markup=buton.get_away())
    else:
        bot.send_message(user_id, 'Welcome to our shop! Please registrate. Write your name', reply_markup=buton.get_away())
        bot.register_next_step_handler(message, name)
def name(message):
    global user
    user = message.text
    bot.send_message(user_id, 'Very well! Now, send your number', reply_markup=buton.button_for_number())
    bot.register_next_step_handler(message, number, user)
def number(message, user):
    if message.contact:
        user_numb = message.contact.phone_number
        bot.send_message(user_id, 'Great! Now, send your location', reply_markup=buton.send_your_location())
        bot.register_next_step_handler(message, location, user, user_numb)
    else:
        bot.send_message(user_id, 'Please, send your contact correctly')
        bot.register_next_step_handler(message, number, user)
def location(message, user_numb, user):
    if message.location:
        user_loc = geolocator.reverse(f'{message.location.longitude},'
                                      f'{message.location.latitude}')
        registration.register(user_id, user, user_numb, user_loc)
        bot.send_message(user_id, 'Congratulations!!! you are in base! WELCOME TO OUR FAMILY!<3')
    else:
        bot.send_message(user_id, 'Error, send your location through a button')
        bot.register_next_step_handler(message, location, user, user_numb)
bot.polling(non_stop=True)