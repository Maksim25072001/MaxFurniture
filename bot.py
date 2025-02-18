import telebot
from telebot import types

# Токен бота (получить через @BotFather в Telegram)
TOKEN = 'your_telegram_bot_token'

bot = telebot.TeleBot(TOKEN)

# Пример данных о мебели (в реальной жизни это будет база данных или API)
furniture_data = {
    'chair': {
        'name': 'Стул',
        'description': 'Комфортный деревянный стул.',
        'image_url': 'https://example.com/chair.jpg',  # Изображение стула
        '3d_url': 'https://example.com/chair_3d',  # Ссылка на 3D-модель
    },
    'table': {
        'name': 'Стол',
        'description': 'Большой деревянный стол.',
        'image_url': 'https://example.com/table.jpg',
        '3d_url': 'https://example.com/table_3d',
    },
}

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Посмотреть мебель")
    item2 = types.KeyboardButton("Информация о магазине")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Добро пожаловать в MaxFurniture! Выберите опцию:", reply_markup=markup)

# Обработка нажатия на "Посмотреть мебель"
@bot.message_handler(func=lambda message: message.text == "Посмотреть мебель")
def show_furniture(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Стул")
    item2 = types.KeyboardButton("Стол")
    item3 = types.KeyboardButton("Назад")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Выберите мебель для просмотра:", reply_markup=markup)

# Обработка выбора мебели
@bot.message_handler(func=lambda message: message.text in furniture_data.keys())
def show_furniture_details(message):
    furniture = furniture_data[message.text]
    bot.send_message(
        message.chat.id,
        f"Вы выбрали: {furniture['name']}\nОписание: {furniture['description']}\n",
        reply_markup=types.ReplyKeyboardRemove()
    )
    bot.send_photo(message.chat.id, furniture['image_url'])
    bot.send_message(message.chat.id, f"Для просмотра в 3D перейдите по ссылке: {furniture['3d_url']}")

# Обработка выбора "Назад"
@bot.message_handler(func=lambda message: message.text == "Назад")
def back_to_main_menu(message):
    send_welcome(message)

# Запуск бота
bot.polling(none_stop=True)
