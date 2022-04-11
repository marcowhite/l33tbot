from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# main menu

btnUse = KeyboardButton ('/translate')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnUse)

btnFirst = KeyboardButton ('PyCCkUu')
btnSecond = KeyboardButton ('AnGLIySKIy')
btnThird = KeyboardButton ('l33t')
btnFourth = KeyboardButton ('zalgo')
btnCancel = KeyboardButton ('/cancel')
dictionarySelector = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFirst,btnSecond,btnThird,btnFourth)

cancelMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCancel)

