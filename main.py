import telebot
import config

from telebot import types


bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет" or message.text == "/start" or message.text == 'привет':
        keyboard_TeaFerm = types.InlineKeyboardMarkup()
        TeaFerm_simple = types.InlineKeyboardButton("Ферментированный", callback_data= 'Ferm')
        TeaFerm_post = types.InlineKeyboardButton("Постферментированный", callback_data= 'Postferm')
        keyboard_TeaFerm.add(TeaFerm_simple, TeaFerm_post)
        bot.send_message(message.from_user.id, "Привет, какой чай вы хотите выбрать?", reply_markup=keyboard_TeaFerm)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.callback_query_handler(func= lambda callback: True)
def callback_1(callback): #Ферментация
    if callback.data == 'Ferm':
        keyboard_SimpleTea = types.InlineKeyboardMarkup()
        SimpleTea_strongly = types.InlineKeyboardButton("Сильно ферм.", callback_data='Strongly')
        SimpleTea_weakly = types.InlineKeyboardButton("Слабо ферм.", callback_data='Weakly')
        SimpleTea_minimal = types.InlineKeyboardButton("Минимально ферм.", callback_data='Minimal')
        SimpleTea_semi = types.InlineKeyboardButton("Полу-ферм.", callback_data='Semi')
        keyboard_SimpleTea.add(SimpleTea_semi, SimpleTea_minimal, SimpleTea_weakly, SimpleTea_strongly)
        bot.send_message(callback.from_user.id, "Есть 4 вида ферментированного чая:", reply_markup=keyboard_SimpleTea)
    elif callback.data == 'Postferm':
        keyboard_TeaPuer = types.InlineKeyboardMarkup()
        TeaPuer_light = types.InlineKeyboardButton("Шэн пуэр (Светлый)", callback_data='Light')
        TeaPuer_dark = types.InlineKeyboardButton("Шу пуэр(Тёмный)", callback_data='Dark')
        TeaPuer_palace = types.InlineKeyboardButton("Гунтин пуэр (дворцовый императорский)", callback_data='The_palace')
        keyboard_TeaPuer.add(TeaPuer_palace, TeaPuer_dark, TeaPuer_light)
        bot.send_message(callback.from_user.id, "Пуэр", reply_markup=keyboard_TeaPuer)

@bot.callback_query_handler(func= lambda callback: True)
def callback_2(callback): #4 вида ферментации чая
    if callback.data == 'Strongly':
        bot.send_message(callback.from_user.id, "Чёрный чай: Самый популярный в России и в Европе. Производится путём сильной ферментации (окисления). Как правило, имеет терпкий насыщенный вкус.")
    elif callback.data == 'Weakly':
        keyboard_white_and_yellow = types.InlineKeyboardMarkup()
        Weakly_Tea_white = types.InlineKeyboardButton('Белый', callback_data='White')
        Weakly_Tea_yellow = types.InlineKeyboardButton('Желтый', callback_data='Yellow')
        keyboard_white_and_yellow.add(Weakly_Tea_yellow, Weakly_Tea_white)
        bot.send_message(callback.from_user.id, 'Белый или Желтый', reply_markup=keyboard_white_and_yellow)
    elif callback.data == 'Minimal':
        bot.send_message(callback.from_user.id, 'Зелёный чай: Подвергается минимальной ферментации. Такой тип обработки позволяет сохранить высокий уровень антиоксидантов, витаминов и минералов. Чай имеет настой золотисто-жёлтого цвета, а также лёгкий и травянистый вкус.')
    elif callback.data == 'Semi':
        bot.send_message(callback.from_user.id, 'Улун чай: Полуферментированный чай, занимающий среднее положение между чёрным и зелёным. По степени окисления делится на сильноферментированные (ближе к чёрному чаю) и слабоферментированные (ближе к зелёному) сорта. Улуны дают настой от светло-жёлтого до светло-коричневого цвета, вкус насыщенный и яркий.')


@bot.callback_query_handler(func=lambda callback: True)
def callback_2_1(callback): # w y
    if callback.data == 'White':
        bot.send_message(callback.from_user.id, 'Белый чай: Слабоферментированный чай, содержащий типсы (чайные почки). Особенно популярен в Китае, считается максимально полезным. Белый чай имеет светло-жёлтый цвет и нежный аромат.')
    elif callback.data == 'Yellow':
        bot.send_message(callback.from_user.id, 'Жёлтый чай: Слабоферментированный чай из сырья высокого качества. По степени окисления находится между белым и зелёным. Считается очень редким и чаще всего может быть приобретён только в Китае.')


@bot.callback_query_handler(func= lambda callback: True)
def callback_3(callback): #Пуэр
    if callback.data == 'Light':
        bot.send_message(callback.from_user.id,'Шэн пуэр (светлый): Переводится как «сырой, свежий». При обработке не проходит процесс ферментации, а дозревает потом. С каждым годом шэн темнеет, его вкус становится более мягким и цельным.')
    elif callback.data == 'Dark':
        bot.send_message(callback.from_user.id,'Шу пуэр (тёмный): При обработке листья подвергают ускоренной ферментации, которая имитирует старение чая в более короткие сроки — в течение 45–65 дней. У молодого чая вкус резкий и древесный, а со временем развивается, становится сложным и глубоким.')
    elif callback.data == 'The_palace':
        bot.send_message(callback.from_user.id,'Гунтин пуэр (дворцовый или императорский): Для его производства используют только типсы (верхнюю почку и два маленьких листочка). На финальном этапе его не прессуют, а аккуратно высушивают.')

bot.polling(none_stop=True, interval=0)