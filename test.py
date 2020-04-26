import telebot
from telebot import types
import Sinoptik
import schedule
import time
import threading
import asyncio




bot = telebot.TeleBot("920298783:AAF81tClAxEpaXDlFLkRvZwb4oqnqSNVl0U")

################################################################
                                                               #
def timer(message):                                            #
	Sinoptik.parse()                                           #
	with open("current.txt", "r") as file:                     #
			c = file.read()                                    #
                                                               #
                                                               #
	bot.send_message(message.chat.id,c, parse_mode = "html")   #
	
		
														   #
################################################################



@bot.message_handler(func=lambda message: True, commands=["start"])

	

def welcome(message):
	
		
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		
		stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
		stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
		stuff3 = types.KeyboardButton("📖Інформація про бота")
		stuff4 = types.KeyboardButton("📪Підписатися на розсилку")
	

		

		markup.add(stuff1, stuff2, stuff3,stuff4)

		bot.send_message(message.chat.id, "🔥Вітаю,{0.first_name},у боті \"Погода в Україні(Синоптик)\"🔥\n\n✅Що може цей бот?:\n\n1️⃣Надсилати прогноз погоди на сьогодні;\n\n2️⃣Стан погоди на данний момент;\n\n3️⃣Відсилати прогноз погоди по розкладу;\n--------------------------\n⚠️Бот наразі знаходиться у розробці,тож можуть бути баги та відсутність важливих функцій⚠️".format(message.from_user,bot.get_me()),
			parse_mode = "html", reply_markup=markup)
		
	


@bot.message_handler(func=lambda message: True, content_types=['text'])


	
def allweather(message):

	if message.text == ("⛅️Прогноз на сьогодні"):
		Sinoptik.parse()
		with open("2:00.txt", "r") as file:
			r = file.read()
		with open("5:00.txt", "r") as file1:
			r1 = file1.read()
		with open("8:00.txt", "r") as file2:
			r2 = file2.read()
		with open("11:00.txt", "r") as file3:
			r3 = file3.read()
		with open("14:00.txt", "r") as file4:
			r4 = file4.read()
		with open("17:00.txt", "r") as file5:
			r5 = file5.read()
		with open("20:00.txt", "r") as file6:
			r6 = file6.read()
		with open("23:00.txt", "r") as file7:
			r7 = file7.read()
		bot.send_message(message.chat.id,"\n" + r + "\n" + r1 + "\n" + r2 + "\n" + r3 + "\n" + r4 + "\n" + r5 + "\n" + r6 + "\n" + r7, parse_mode = "html")
		







	if message.text == ("📖Інформація про бота"):
			bot.send_message(message.chat.id, "❗️Цей бот був створенний Світлицьким Ярославом для полегшення життя простих Запорожців")
			


	


	if message.text == ("🔥Яка зараз погода?"):
			Sinoptik.parse()
			with open("current.txt", "r") as fil:
				c = fil.read()
			bot.send_message(message.chat.id,c, parse_mode = "html")
			 
		

	
		


	if message.text == ("📪Підписатися на розсилку"):
					
			markup = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
			stuff1 = types.KeyboardButton("🕖Кожні 15 хвилин")
			stuff2 = types.KeyboardButton("🕕Кожну годину")
			stuff3 = types.KeyboardButton("🕔Кожні 3 години")
			stuff4 = types.KeyboardButton("🕓Кожні 6 годин")

			markup.add(stuff1)
			markup.add(stuff2)
			markup.add(stuff3)
			markup.add(stuff4)
			
		
			
			
			bot.send_message(message.chat.id,"👇Оберіть час коли буде приходити прогноз погоди",reply_markup=markup)
			
			



	if message.text == ("🕖Кожні 15 хвилин"):
			

			
			
		
			
		
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
			stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
			stuff3 = types.KeyboardButton("📖Інформація про бота")
			stuff4 = types.KeyboardButton("✂️Відписатися від розсилки")
			markup.add(stuff1, stuff2, stuff3,	stuff4)
			msg = bot.send_message(message.chat.id,"🥳Ви будете отримувати прогноз кожні 15 хвилин",reply_markup=markup)
			t = threading.Thread(target=scheduler(message, 15))
			t.start()
			t.join()
			
	if message.text == ("🕕Кожну годину"):
			

			
			
		
			
		
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
			stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
			stuff3 = types.KeyboardButton("📖Інформація про бота")
			stuff4 = types.KeyboardButton("✂️Відписатися від розсилки")
			markup.add(stuff1, stuff2, stuff3,	stuff4)
			
			msg = bot.send_message(message.chat.id,"🥳Ви будете отримувати прогноз кожну годину ",reply_markup=markup)
			t = threading.Thread(target=scheduler(message, 60))
			t.start()
			t.join()

	if message.text == ("🕔Кожні 3 години"):
			

			
			
		
			
		
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
			stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
			stuff3 = types.KeyboardButton("📖Інформація про бота")
			stuff4 = types.KeyboardButton("✂️Відписатися від розсилки")
			markup.add(stuff1, stuff2, stuff3,	stuff4)
			
			msg = bot.send_message(message.chat.id,"🥳Ви будете отримувати прогноз кожні 3 години ",reply_markup=markup)
			t = threading.Thread(target=scheduler(message, 180))
			t.start()
			t.join()

	if message.text == ("🕓Кожні 6 годин"):
			

			
			
		
			
		
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
			stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
			stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
			stuff3 = types.KeyboardButton("📖Інформація про бота")
			stuff4 = types.KeyboardButton("✂️Відписатися від розсилки")
			markup.add(stuff1, stuff2, stuff3,	stuff4)
			
			msg = bot.send_message(message.chat.id,"🥳Ви будете отримувати прогноз кожні 6 годин",reply_markup=markup)
			t = threading.Thread(target=scheduler(message, 360))
			t.start()
			t.join()



			
		
	if message.text == "✂️Відписатися від розсилки":

				
			markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		
			stuff1 = types.KeyboardButton("⛅️Прогноз на сьогодні")
			stuff2 = types.KeyboardButton("🔥Яка зараз погода?")
			stuff3 = types.KeyboardButton("📖Інформація про бота")
			stuff4 = types.KeyboardButton("📪Підписатися на розсилку")
	

		

			markup.add(stuff1, stuff2, stuff3,stuff4)
				
			bot.send_message(message.chat.id,"😿Ви відписалися від розсилки погоди!",reply_markup=markup)
			
			schedule.clear("weather")
			
			
			

def scheduler(message, stime):
	schedule.clear("weather")
	schedule.jobs = [schedule.every(stime).minutes.do(timer,message).tag("weather")]
	while True:
		schedule.run_pending()
		

	


bot.polling(none_stop = True)