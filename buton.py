from telebot import types

def button_for_number():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    contact = types.KeyboardButton('Send your number', request_contact=True)
    keyboard.add(contact)
    return keyboard
def send_your_location():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    geo = types.KeyboardButton('Send your location', request_location=True)
    keyboard.add(geo)
    return keyboard

def get_away():
    types.ReplyKeyboardRemove()