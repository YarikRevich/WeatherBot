import telebot
from telebot import types
from parcer import Parcer
import schedule
import time
import threading
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError





bot = telebot.TeleBot("920298783:AAF81tClAxEpaXDlFLkRvZwb4oqnqSNVl0U")


db = MongoClient("localhost",27017)
database = db["weatherbot"]
collection = database["user_settings"]



@bot.message_handler(func=lambda message: True, commands=["start"])

    

def welcome(message):
    
        if collection.find_one({"_id":"{0.id}".format(message.from_user)}) == None:
            
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True,
            one_time_keyboard=True)
        
        
            stuff1 = types.KeyboardButton("🇺🇦Українська")
            stuff2 = types.KeyboardButton("🇷🇺Русский")
        


        

            markup.add(stuff1, stuff2)

            bot.send_message(message.chat.id, "🔥Вітаю,{0.first_name},у боті \"Погода в Україні(Синоптик)\"🔥\n\n✅Що може цей бот?:\n\n1️⃣Надсилати прогноз погоди на сьогодні;\n\n2️⃣Стан погоди на данний момент;\n\n3️⃣Відсилати прогноз погоди по розкладу;\n--------------------------\n⚠️Бот наразі знаходиться у розробці,тож можуть бути баги та відсутність важливих функцій⚠️\nА зараз треба зробити пару налаштувань!".format(message.from_user,bot.get_me()),
                parse_mode = "html")
            msg = bot.send_message(message.chat.id,"Оберіть мову на якій Ви хочете отримувати прогнози погоди",reply_markup=markup)
            bot.register_next_step_handler(msg,language)
        else:
            info = collection.find({"_id":"{0.id}".format(message.from_user)})
            for inf in info:
                main_lang = inf["lang"]
            if main_lang == "ua.":
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
                stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
                stuff3 = types.KeyboardButton("📖Інформація про бота")
                stuff4 = types.KeyboardButton("📪Підписатися на розсилку")
                markup.add(stuff1, stuff2,stuff3,stuff4)
                msg = bot.send_message(message.chat.id, "🔥Вітаю,{0.first_name},у боті \"Погода в Україні(Синоптик)\"🔥\n\n✅Що може цей бот?:\n\n1️⃣Надсилати прогноз погоди на сьогодні;\n\n2️⃣Надсилати стан погоди на данний момент;\n\n3️⃣Відсилати прогноз погоди по розкладу".format(message.from_user,bot.get_me()),
                    parse_mode = "html",reply_markup=markup)
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
                stuff1 = types.KeyboardButton("⛅️Прогноз на сегодня")
                stuff2 = types.KeyboardButton("🔥Какая сейчас погода?")
                stuff3 = types.KeyboardButton("📖Информация про бота")
                stuff4 = types.KeyboardButton("📪Подписаться на розсылку")
                markup.add(stuff1, stuff2,stuff3,stuff4)
                msg = bot.send_message(message.chat.id, "🔥Приветсвую,{0.first_name},в боте \"Погода в Украине(Синоптик)\"🔥\n\n✅Что может этот бот?:\n\n1️⃣Отсылать прогноз погоди на сегодня;\n\n2️⃣Показывать состояние погоды на данный момент;\n\n3️⃣Отсылать прогноз погоды по розписанию".format(message.from_user,bot.get_me()),
                    parse_mode = "html",reply_markup=markup)

            
@bot.message_handler(content_types=["text"])
def func(message):
    info = collection.find({"_id":"{0.id}".format(message.from_user)})
    for inf in info:
        main_city = inf["city_ua"]
        global main_lang
        main_lang = inf["lang"]
        
    global parcer
    parcer = Parcer(lang=main_lang,url=main_city,user_id_bot="{0.id}".format(message.from_user))
    
    

    if message.text == "⛅️Прогноз на сьогодні" or message.text == "⛅️Прогноз на сегодня":
        parcer.get_data()
        full_info = parcer.full_info()
        if main_lang == "ua.":
            
            bot.send_message(message.chat.id,
                " 👇👉Погода на 3:00👈👇\n🌡Температура:" + full_info.get(1)[1] +"\n☀️Прогноз:" + full_info.get(1)[0] + "\n💨Швидкість вітру:" + full_info.get(1)[3] +"\n❓Вероїдність опадів:" + full_info.get(1)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 6:00👈👇\n🌡Температура:" + full_info.get(2)[1] +"\n☀️Прогноз:" + full_info.get(2)[0] + "\n💨Швидкість вітру:" + full_info.get(2)[3] +"\n❓Вероїдність опадів:" + full_info.get(2)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 9:00👈👇\n🌡Температура:" + full_info.get(3)[1] +"\n☀️Прогноз:" + full_info.get(3)[0] + "\n💨Швидкість вітру:" + full_info.get(3)[3] +"\n❓Вероїдність опадів:" + full_info.get(3)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 12:00👈👇\n🌡Температура:" + full_info.get(4)[1] +"\n☀️Прогноз:" + full_info.get(4)[0] + "\n💨Швидкість вітру:" + full_info.get(4)[3] +"\n❓Вероїдність опадів:" + full_info.get(4)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 15:00👈👇\n🌡Температура:" + full_info.get(5)[1] +"\n☀️Прогноз:" + full_info.get(5)[0] + "\n💨Швидкість вітру:" + full_info.get(5)[3] +"\n❓Вероїдність опадів:" + full_info.get(5)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 18:00👈👇\n🌡Температура:" + full_info.get(6)[1] +"\n☀️Прогноз:" + full_info.get(6)[0] + "\n💨Швидкість вітру:" + full_info.get(6)[3] +"\n❓Вероїдність опадів:" + full_info.get(6)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 21:00👈👇\n🌡Температура:" + full_info.get(7)[1] +"\n☀️Прогноз:" + full_info.get(7)[0] + "\n💨Швидкість вітру:" + full_info.get(7)[3] +"\n❓Вероїдність опадів:" + full_info.get(7)[2]
                        
                        
                )
        else:
            bot.send_message(message.chat.id,
                " 👇👉Погода на 3:00👈👇\n🌡Температура:" + full_info.get(1)[1] +"\n☀️Прогноз:" + full_info.get(1)[0] + "\n💨Скорость ветра:" + full_info.get(1)[3] +"\n❓Вероятность осадков:" + full_info.get(1)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 6:00👈👇\n🌡Температура:" + full_info.get(2)[1] +"\n☀️Прогноз:" + full_info.get(2)[0] + "\n💨Скорость ветра:" + full_info.get(2)[3] +"\n❓Вероятность осадков:" + full_info.get(2)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 9:00👈👇\n🌡Температура:" + full_info.get(3)[1] +"\n☀️Прогноз:" + full_info.get(3)[0] + "\n💨Скорость ветра:" + full_info.get(3)[3] +"\n❓Вероятность осадков:" + full_info.get(3)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 12:00👈👇\n🌡Температура:" + full_info.get(4)[1] +"\n☀️Прогноз:" + full_info.get(4)[0] + "\n💨Скорость ветра:" + full_info.get(4)[3] +"\n❓Вероятность осадков:" + full_info.get(4)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 15:00👈👇\n🌡Температура:" + full_info.get(5)[1] +"\n☀️Прогноз:" + full_info.get(5)[0] + "\n💨Скорость ветра:" + full_info.get(5)[3] +"\n❓Вероятность осадков:" + full_info.get(5)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 18:00👈👇\n🌡Температура:" + full_info.get(6)[1] +"\n☀️Прогноз:" + full_info.get(6)[0] + "\n💨Скорость ветра:" + full_info.get(6)[3] +"\n❓Вероятность осадков:" + full_info.get(6)[2] +
                "\n" + "-"*40 + "\n" + "👇👉Погода на 21:00👈👇\n🌡Температура:" + full_info.get(7)[1] +"\n☀️Прогноз:" + full_info.get(7)[0] + "\n💨Скорость ветра:" + full_info.get(7)[3] +"\n❓Вероятность осадков:" + full_info.get(7)[2]
                        
                        
                )

        







    elif message.text == "📖Інформація про бота" or message.text == "📖Информация про бота":
            if main_lang == "ua.":
                lang = "Українська"
            if main_lang == "":
                lang = "Русский"
            markup = types.InlineKeyboardMarkup()
            if lang == "Українська":
                button = types.InlineKeyboardButton("Змінити данні",callback_data="Change")
                markup.add(button)
                bot.send_message(message.chat.id,
                    "❗️Цей бот був створенний Світлицьким Ярославом для полегшення життя простих Запорожців\n"+ 
                    "Обрана мова:" + " " + lang +
                    "\nОбране місто для показу погоди:" + " " + main_city.capitalize(),
                    reply_markup=markup
                    )      
            else:
                button = types.InlineKeyboardButton("Изменить данные",callback_data="Change")
                markup.add(button)
                bot.send_message(message.chat.id,
                    "❗️Этот бот был создан Светлицким Ярослав для облегчения жизни простых запорожцев\n"+ 
                    "Выбраный язик:" + " " + lang +
                    "\nВыбраный город для показа погоды:" + " " + main_city.capitalize(),
                    reply_markup=markup
                )   

            


    


    elif message.text == "🔥Яка зараз погода?" or message.text == "🔥Какая сейчас погода?":
        parcer.get_data()
        current = parcer.current()    
        if main_lang == "ua.":
            bot.send_message(message.chat.id,
            "👇👉Погода на зараз👈👇\n🌡Температура:" + current.get("curr")[0] +"\n☀️Прогноз:" + current.get("curr")[1]  + "\n💨Швидкість вітру:" + current.get("curr")[3]  +"\n❓Вероїдність опадів:" + current.get("curr")[2] ,
            parse_mode = "html")
        else:
            bot.send_message(message.chat.id,
            "👇👉Погода на cейчас👈👇\n🌡Температура:" + current.get("curr")[0] +"\n☀️Прогноз:" + current.get("curr")[1]  + "\n💨Скорость ветра:" + current.get("curr")[3]  +"\n❓Вероятность осадков:" + current.get("curr")[2] ,
            parse_mode = "html")

        

    
        


    elif message.text == "📪Підписатися на розсилку" or message.text == "📪Подписаться на розсылку":
        if main_lang == "ua.":       
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
            stuff1 = types.KeyboardButton("🕖Кожні 15 хвилин")
            stuff2 = types.KeyboardButton("🕕Кожну годину")
            stuff3 = types.KeyboardButton("🕔Кожні 3 години")
            stuff4 = types.KeyboardButton("🕓Кожні 6 годин")
            markup.add(stuff1)
            markup.add(stuff2)
            markup.add(stuff3)
            markup.add(stuff4)
            msg = bot.send_message(message.chat.id,"👇Оберіть час коли буде приходити прогноз погоди",reply_markup=markup)
            bot.register_next_step_handler(msg,mailing_setting)
        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
            stuff1 = types.KeyboardButton("🕖Каждые  15 минут")
            stuff2 = types.KeyboardButton("🕕Каждый час")
            stuff3 = types.KeyboardButton("🕔Каждые 3 часа")
            stuff4 = types.KeyboardButton("🕓Каждые 6 часов")
            markup.add(stuff1)
            markup.add(stuff2)
            markup.add(stuff3)
            markup.add(stuff4)
            msg = bot.send_message(message.chat.id,"👇Выберете наиболее подходящее время",reply_markup=markup)
            bot.register_next_step_handler(msg,mailing_setting)
    


    elif message.text == "✂️Відписатися від розсилки" or message.text == "✂️Отписаться от розсылки":
        if main_lang == "ua.":    
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
            stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
            stuff3 = types.KeyboardButton("📖Інформація про бота")
            stuff4 = types.KeyboardButton("📪Підписатися на розсилку")
            markup.add(stuff1, stuff2, stuff3,stuff4)   
            bot.send_message(message.chat.id,"😿Ви відписалися від розсилки погоди!",reply_markup=markup) 
            schedule.clear(tag="weather")
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            stuff1 = types.KeyboardButton("⛅️Прогноз на сегодня")
            stuff2 = types.KeyboardButton("🔥Какая сейчас погода?")
            stuff3 = types.KeyboardButton("📖Информация про бота")
            stuff4 = types.KeyboardButton("📪Подписаться на розсылку")
            markup.add(stuff1, stuff2,stuff3,stuff4)
            bot.send_message(message.chat.id,"😿Ви отписались от розсылки на погоду!",reply_markup=markup)
            schedule.clear(tag="weather")
    
    else:
        if main_lang == "ua.":
            bot.send_message(message.chat.id,"Виберіть пункт на клавіатурі")     
        else:
            bot.send_message(message.chat.id,"Выберете пункт на клавиатуре") 



def language(message):

    if message.text == "🇺🇦Українська":
        try:
            collection.insert_one({"_id":"{0.id}".format(message.from_user)})
        except DuplicateKeyError:
            pass
        collection.update_many({"_id":"{0.id}".format(message.from_user)},{"$set":{"lang":"ua."}})
        
        markup = types.InlineKeyboardMarkup(row_width=1)
        stuff = types.InlineKeyboardButton("Київ",callback_data="Київ")
        stuff1 = types.InlineKeyboardButton("Запоріжжя",callback_data="Запоріжжя")
        stuff2 = types.InlineKeyboardButton("Львів",callback_data="Львів")
        stuff3 = types.InlineKeyboardButton("Житомир",callback_data="Житомир")
        stuff4 = types.InlineKeyboardButton("Бровари",callback_data="Бровари")
        stuff5 = types.InlineKeyboardButton("Далі",callback_data="Next")
        markup.add(stuff,stuff1,stuff2,stuff3,stuff4,stuff5)
        
        msg = bot.send_message(message.chat.id,"Оберіть місто",reply_markup=markup)
        global next_id 
        next_id = msg.message_id
    


    if message.text == "🇷🇺Русский":
        try:
            collection.insert_one({"_id":"{0.id}".format(message.from_user)})
        except DuplicateKeyError:
            pass
        collection.update_many({"_id":"{0.id}".format(message.from_user)},{"$set":{"lang":""}})

        markup = types.InlineKeyboardMarkup(row_width=1)
        stuff = types.InlineKeyboardButton("Киев",callback_data="Киев")
        stuff1 = types.InlineKeyboardButton("Запорожье",callback_data="Запорожье")
        stuff2 = types.InlineKeyboardButton("Львов",callback_data="Львов")
        stuff3 = types.InlineKeyboardButton("Житомир",callback_data="Житомир")
        stuff4 = types.InlineKeyboardButton("Бровары",callback_data="Бровары")
        stuff5 = types.InlineKeyboardButton("Дальше",callback_data="Next_ru")
        markup.add(stuff,stuff1,stuff2,stuff3,stuff4,stuff5)
        msg = bot.send_message(message.chat.id,"Выберете город",reply_markup=markup)
        global next_id_ru
        next_id_ru = msg.message_id




def make_city_entry(call,city):
    info_lang = collection.find({"_id":"{0.id}".format(call.from_user)})
    for lang in info_lang:
        main_lang = lang["lang"]
    
    if main_lang == "ua.":
        collection.update_many({"_id":"{0.id}".format(call.from_user)},{"$set":{"city_ua":city}})
        bot.edit_message_text(text="Вітаю,ви вибрали місто!",chat_id=call.message.chat.id,message_id=next_id)
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
        stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
        stuff3 = types.KeyboardButton("📖Інформація про бота")
        stuff4 = types.KeyboardButton("📪Підписатися на розсилку")
        markup.add(stuff1, stuff2,stuff3,stuff4)
    
        bot.send_message(call.message.chat.id,"Тепер Вам доступні такі функції",reply_markup=markup)
    else:
        collection.update_many({"_id":"{0.id}".format(call.from_user)},{"$set":{"city_ua":city}})
        bot.edit_message_text(text="Поздравляю,Вы выбрали город",chat_id=call.message.chat.id,message_id=next_id_ru)
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        stuff1 = types.KeyboardButton("⛅️Прогноз на сегодня")
        stuff2 = types.KeyboardButton("🔥Какая сейчас погода?")
        stuff3 = types.KeyboardButton("📖Информация про бота")
        stuff4 = types.KeyboardButton("📪Подписаться на розсылку")
        markup.add(stuff1, stuff2,stuff3,stuff4)
    
        bot.send_message(call.message.chat.id,"Тепер Вам доступны такие функции",reply_markup=markup)
        
    


"""
 
Ukrainian inline keyboard

"""



@bot.callback_query_handler(func=lambda call: True)






def cities(call):

    """
    Controller for ukrainian inline keyboard

    """

    if call.data == "Київ":
        make_city_entry(call,"київ")
    if call.data == "Запоріжжя":
        make_city_entry(call,"запоріжжя")
    if call.data == "Львів":
        make_city_entry(call,"львів")
    if call.data == "Житомир":
        make_city_entry(call,"житомир")
    if call.data == "Бровари":
        make_city_entry(call,"бровари")
    if call.data == "Луганськ":
        make_city_entry(call,"луганськ")
    if call.data == "Донецьк":
        make_city_entry(call,"донецьк")
    if call.data == "Вінниця":
        make_city_entry(call,"вінниця")
    if call.data == "Кривий-Ріг":
        make_city_entry(call,"кривий-ріг")
    if call.data == "Кропивницький":
        make_city_entry(call,"кропивницький")




    if call.data == "Next":
        markup = types.InlineKeyboardMarkup(row_width=1)
        stuff1 = types.InlineKeyboardButton("Луганськ",callback_data="Луганськ")
        stuff2 = types.InlineKeyboardButton("Донецьк",callback_data="Донецьк")
        stuff3 = types.InlineKeyboardButton("Вінниця",callback_data="Вінниця")
        stuff4 = types.InlineKeyboardButton("Кривий-Ріг",callback_data="Кривий-Ріг")
        stuff5 = types.InlineKeyboardButton("Кропивницький",callback_data="Кропивницький")
        stuff6 = types.InlineKeyboardButton("Назад",callback_data="Previous")
        markup.add(stuff1,stuff2,stuff3,stuff4,stuff5,stuff6)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=next_id,reply_markup=markup)


    if call.data == "Previous":
        markup = types.InlineKeyboardMarkup(row_width=1)
        stuff = types.InlineKeyboardButton("Київ",callback_data="Київ")
        stuff1 = types.InlineKeyboardButton("Запоріжжя",callback_data="Запоріжжя")
        stuff2 = types.InlineKeyboardButton("Львів",callback_data="Львів")
        stuff3 = types.InlineKeyboardButton("Житомир",callback_data="Житомир")
        stuff4 = types.InlineKeyboardButton("Бровари",callback_data="Бровари")
        stuff5 = types.InlineKeyboardButton("Далі",callback_data="Next")
        markup.add(stuff,stuff1,stuff2,stuff3,stuff4,stuff5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=next_id,reply_markup=markup)




    """
    Controllers for russian inline keyboard

    """

    if call.data == "Киев":
        make_city_entry(call,"киев")
    if call.data == "Запорожье":
        make_city_entry(call,"запорожье")
    if call.data == "Львов":
        make_city_entry(call,"львів")
    if call.data == "Житомир":
        make_city_entry(call,"житомир")
    if call.data == "Бровары":
        make_city_entry(call,"бровары")
    if call.data == "Луганск":
        make_city_entry(call,"луганск")
    if call.data == "Донецк":
        make_city_entry(call,"донецк")
    if call.data == "Винниця":
        make_city_entry(call,"винниця")
    if call.data == "Кривой-Рог":
        make_city_entry(call,"кривой-рог")
    if call.data == "Кропивницкий":
        make_city_entry(call,"кропивницкий")




    if call.data == "Next_ru":
        markup = types.InlineKeyboardMarkup(row_width=1)
        stuff1 = types.InlineKeyboardButton("Луганск",callback_data="Луганск")
        stuff2 = types.InlineKeyboardButton("Донецк",callback_data="Донецк")
        stuff3 = types.InlineKeyboardButton("Винниця",callback_data="Винниця")
        stuff4 = types.InlineKeyboardButton("Кривой-Рог",callback_data="Кривой-Рог")
        stuff5 = types.InlineKeyboardButton("Кропивницкий",callback_data="Кропивницкий")
        stuff6 = types.InlineKeyboardButton("Назад",callback_data="Previous_ru")
        markup.add(stuff1,stuff2,stuff3,stuff4,stuff5,stuff6)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=next_id_ru,reply_markup=markup)


    if call.data == "Previous_ru":
        markup = types.InlineKeyboardMarkup(row_width=1)
        stuff = types.InlineKeyboardButton("Киев",callback_data="Киев")
        stuff1 = types.InlineKeyboardButton("Запорожье",callback_data="Запорожье")
        stuff2 = types.InlineKeyboardButton("Львов",callback_data="Львов")
        stuff3 = types.InlineKeyboardButton("Житомир",callback_data="Житомир")
        stuff4 = types.InlineKeyboardButton("Бровари",callback_data="Бровары")
        stuff5 = types.InlineKeyboardButton("Дальше",callback_data="Next_ru")
        markup.add(stuff,stuff1,stuff2,stuff3,stuff4,stuff5)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id,message_id=next_id_ru,reply_markup=markup)


    """
    Controller to change your work-language

    """

    if call.data == "Change":
        if main_lang == "ua.":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True,
                one_time_keyboard=True)
            stuff1 = types.KeyboardButton("🇺🇦Українська")
            stuff2 = types.KeyboardButton("🇷🇺Русский")
            markup.add(stuff1, stuff2)
            msg = bot.send_message(call.message.chat.id,"Оберіть мову на якій Ви хочете отримувати прогнози погоди",reply_markup=markup)
            bot.register_next_step_handler(msg,language)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True,
                one_time_keyboard=True)
            stuff1 = types.KeyboardButton("🇺🇦Українська")
            stuff2 = types.KeyboardButton("🇷🇺Русский")
            markup.add(stuff1, stuff2)
            msg = bot.send_message(call.message.chat.id,"Выберете язик на каком Вы хотите получать прогнозы погоды",reply_markup=markup)
            bot.register_next_step_handler(msg,language)

"""

Controller for the mailing setting

"""


def mailing_setting(message): 
    if message.text == "🕖Кожні 15 хвилин" or message.text == "🕖Каждые  15 минут":    
        if main_lang == "ua.":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
            stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
            stuff3 = types.KeyboardButton("📖Інформація про бота")
            stuff4 = types.KeyboardButton("✂️Відписатися від розсилки")
            markup.add(stuff1, stuff2, stuff3,	stuff4)
            bot.send_message(message.chat.id,"🥳Ви будете отримувати прогноз кожні 15 хвилин",reply_markup=markup)
            threading.Timer(1,scheduler,[message,2]).start()
            
            
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            stuff1 = types.KeyboardButton("⛅️Прогноз на сегодня")
            stuff2 = types.KeyboardButton("🔥Какая сейчас погода?")
            stuff3 = types.KeyboardButton("📖Информация про бота")
            stuff4 = types.KeyboardButton("✂️Отписаться от розсылки")
            markup.add(stuff1, stuff2,stuff3,stuff4)
            bot.send_message(message.chat.id,"🥳Вы будете получать прогноз каждые 15 минут",reply_markup=markup)
            threading.Timer(1,scheduler,[message,2]).start()
            

    if message.text == "🕕Кожну годину" or message.text == "🕕Каждый час":
        if main_lang == "ua.":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
            stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
            stuff3 = types.KeyboardButton("📖Інформація про бота")
            stuff4 = types.KeyboardButton("✂️Відписатися від розсилки")
            markup.add(stuff1, stuff2, stuff3,	stuff4)
            bot.send_message(message.chat.id,"🥳Ви будете отримувати прогноз кожну годину",reply_markup=markup)
            threading.Timer(1,scheduler,[message,60]).start()
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            stuff1 = types.KeyboardButton("⛅️Прогноз на сегодня")
            stuff2 = types.KeyboardButton("🔥Какая сейчас погода?")
            stuff3 = types.KeyboardButton("📖Информация про бота")
            stuff4 = types.KeyboardButton("✂️Отписаться от розсылки")
            markup.add(stuff1, stuff2,stuff3,stuff4)
            bot.send_message(message.chat.id,"🥳Вы будете получать прогноз каждый час",reply_markup=markup)
            threading.Timer(1,scheduler,[message,60]).start()

    if message.text == "🕔Кожні 3 години" or message.text == "🕔Каждые 3 часа":
        if main_lang == "ua.":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
            stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
            stuff3 = types.KeyboardButton("📖Інформація про бота")
            stuff4 = types.KeyboardButton("✂️Відписатися від розсилки")
            markup.add(stuff1, stuff2, stuff3,	stuff4)
            bot.send_message(message.chat.id,"🥳Ви будете отримувати прогноз кожні 3 години",reply_markup=markup)
            threading.Timer(1,scheduler,[message,180]).start()
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            stuff1 = types.KeyboardButton("⛅️Прогноз на сегодня")
            stuff2 = types.KeyboardButton("🔥Какая сейчас погода?")
            stuff3 = types.KeyboardButton("📖Информация про бота")
            stuff4 = types.KeyboardButton("✂️Отписаться от розсылки")
            markup.add(stuff1, stuff2,stuff3,stuff4)
            bot.send_message(message.chat.id,"🥳Вы будете получать прогноз каждые 3 часа",reply_markup=markup)
            threading.Timer(1,scheduler,[message,180]).start()

    if message.text == "🕓Кожні 6 годин" or message.text == "🕓Каждые 6 часов":
        if main_lang == "ua.":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
            stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
            stuff3 = types.KeyboardButton("📖Інформація про бота")
            stuff4 = types.KeyboardButton("✂️Відписатися від розсилки")
            markup.add(stuff1, stuff2, stuff3,	stuff4)
            bot.send_message(message.chat.id,"🥳Ви будете отримувати прогноз кожні 6 годин",reply_markup=markup)
            threading.Timer(1,scheduler,[message,360]).start()
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            stuff1 = types.KeyboardButton("⛅️Прогноз на сегодня")
            stuff2 = types.KeyboardButton("🔥Какая сейчас погода?")
            stuff3 = types.KeyboardButton("📖Информация про бота")
            stuff4 = types.KeyboardButton("✂️Отписаться от розсылки")
            markup.add(stuff1, stuff2,stuff3,stuff4)
            bot.send_message(message.chat.id,"🥳Вы будете получать прогноз каждые 6 часов",reply_markup=markup)
            threading.Timer(1,scheduler,[message,360]).start()

    

            
            
            

def scheduler(message, stime):
    
    #Func for getting the latest forecast

    def timer(message): 
        parcer.get_data()
        current = parcer.current()    
        if main_lang == "ua.":
            bot.send_message(message.chat.id,
            "👇👉Погода на зараз👈👇\n🌡Температура:" + current.get("curr")[0] +"\n☀️Прогноз:" + current.get("curr")[1]  + "\n💨Швидкість вітру:" + current.get("curr")[3]  +"\n❓Вероїдність опадів:" + current.get("curr")[2] ,
            parse_mode = "html")
        else:
            bot.send_message(message.chat.id,
            "👇👉Погода на cейчас👈👇\n🌡Температура:" + current.get("curr")[0] +"\n☀️Прогноз:" + current.get("curr")[1]  + "\n💨Скорость ветра:" + current.get("curr")[3]  +"\n❓Вероятность осадков:" + current.get("curr")[2] ,
            parse_mode = "html")

    schedule.clear(tag="weather")
    schedule.jobs = [schedule.every(stime).minutes.do(timer,message).tag("weather")]
    while True:
        schedule.run_pending()
        


bot.polling(none_stop = True,interval=1,timeout=5)