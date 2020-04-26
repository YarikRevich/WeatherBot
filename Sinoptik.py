import requests,bs4
from bs4 import BeautifulSoup

URL = "https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B7%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B6%D0%B6%D1%8F/10-%D0%B4%D0%BD%D1%96%D0%B2"
HEADERS = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.100 Chrome/80.0.3987.100 Safari/537.36",
 "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}

def get_html(url,params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r



def get_content(html):
	soup = BeautifulSoup(html, "html.parser")
	items = soup.find_all("tbody")
	items1 = soup.find_all('div', class_="lSide")
	items2 = soup.find_all("div", class_="wDescription clearfix")

	
	for item in items:

		# 2:00

		temp1 = item.find("tr", class_="temperature").find_next("td", class_="p1").get_text()
		temp1_icon = item.find("tr", class_="img weatherIcoS").find_next("td", class_="p1").find_next("div", class_="weatherIco").get("title") 
		

		# 5:00

		temp2 = item.find("tr", class_="temperature").find_next("td", class_="p2").get_text()
		temp2_icon = item.find("tr", class_="img weatherIcoS").find_next("td", class_="p2").find_next("div", class_="weatherIco").get("title")
	
		# 8:00

		temp3 = item.find("tr", class_="temperature").find_next("td", class_="p3").get_text()
		temp3_icon = item.find("tr", class_="img weatherIcoS").find_next("td", class_="p3").find_next("div", class_="weatherIco").get("title")
		
		# 11:00

		temp4 = item.find("tr", class_="temperature").find_next("td", class_="p4").get_text()
		temp4_icon = item.find("tr", class_="img weatherIcoS").find_next("td", class_="p4").find_next("div", class_="weatherIco").get("title")
	

		# 14:00

		temp5 = item.find("tr", class_="temperature").find_next("td", class_="p5").get_text()
		temp5_icon = item.find("tr", class_="img weatherIcoS").find_next("td", class_="p5").find_next("div", class_="weatherIco").get("title")
		

		# 17:00

		temp6 =	item.find("tr", class_="temperature").find_next("td", class_="p6").get_text()
		temp6_icon = item.find("tr", class_="img weatherIcoS").find_next("td", class_="p6").find_next("div", class_="weatherIco").get("title")
	

		# 20:00

		temp7 =	item.find("tr", class_="temperature").find_next("td", class_="p7").get_text()
		temp7_icon = item.find("tr", class_="img weatherIcoS").find_next("td", class_="p7").find_next("div", class_="weatherIco").get("title")
	

		# 23:00

		temp8 =	item.find("tr", class_="temperature").find_next("td", class_="p8").get_text()
		temp8_icon = item.find("tr", class_="img weatherIcoS").find_next("td", class_="p8").find_next("div", class_="weatherIco").get("title")
	

	for item in items2:
		description = item.find("div", class_="description").get_text()


	
############################################################################################################################################################

	#Отримання стану вітру

	r = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B7%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B6%D0%B6%D1%8F/10-%D0%B4%D0%BD%D1%96%D0%B2")
	html = bs4.BeautifulSoup(r.text, "html.parser")
	
	#Стан вітру на 2:00

	wind1 = html.select(".gray  .p1 .Tooltip")
	wind1_1 = wind1[0].get("data-tooltip")

	#Стан вітру на 5:00

	wind2 = html.select(".gray  .p2 .Tooltip")
	wind2_2 = wind2[0].get("data-tooltip")

	#Стан вітру на 8:00

	wind3 = html.select(".gray  .p3 .Tooltip")
	wind3_3 = wind3[0].get("data-tooltip")

	#Стан вітру на 11:00

	wind4 = html.select(".gray  .p4 .Tooltip")
	wind4_4 = wind4[0].get("data-tooltip")

	#Стан вітру на 14:00

	wind5 = html.select(".gray  .p5 .Tooltip")
	wind5_5 = wind5[0].get("data-tooltip")

	#Стан вітру на 17:00

	wind6 = html.select(".gray  .p6 .Tooltip")
	wind6_6 = wind6[0].get("data-tooltip")

	#Стан вітру на 20:00

	wind7 = html.select(".gray  .p7 .Tooltip")
	wind7_7 = wind7[0].get("data-tooltip")

	#Стан вітру на 23:00

	wind8 = html.select(".gray  .p8 .Tooltip")
	wind8_8 = wind8[0].get("data-tooltip")

###############################################################################################################################################################	

	
###############################################################################################################################################################
	r = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B7%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B6%D0%B6%D1%8F/10-%D0%B4%D0%BD%D1%96%D0%B2")
	html = bs4.BeautifulSoup(r.text, "html.parser")

	#Вероїдність опадів на 2:00
	#soup = BeautifulSoup(html, "html.parser")
	probability1 = html.select(".weatherDetails .p1")
	probability1_1 = probability1[7].get_text() + "%"

	#Вероїдність опадів на 5:00

	probability2 = html.select(".weatherDetails .p2")
	probability2_2 = probability2[7].get_text() + "%"

	#Вероїдність опадів на 8:00

	probability3 = html.select(".weatherDetails .p3")
	probability3_3 = probability3[7].get_text() + "%"

	#Вероїдність опадів на 11:00

	probability4 = html.select(".weatherDetails .p4")
	probability4_4 = probability4[7].get_text() + "%"

	#Вероїдність опадів на 14:00

	probability5 = html.select(".weatherDetails .p5")
	probability5_5 = probability5[7].get_text() + "%"

	#Вероїдність опадів на 17:00

	probability6 = html.select(".weatherDetails .p6")
	probability6_6 = probability6[7].get_text() + "%"
 
	#Вероїдність опадів на 20:00

	probability7 = html.select(".weatherDetails .p7")
	probability7_7 = probability7[7].get_text() + "%"

	#Вероїдність опадів на 23:00

	probability8 = html.select(".weatherDetails .p8")
	probability8_8 = probability8[7].get_text() + "%"

###############################################################################################################################################################

###############################################################################################################################################################

	#Запис інформації в документи

	#Запис інформації в файл "2:00"

	with open("2:00.txt", "w") as file:
		file.write(" 👇👉Погода на 2:00👈👇 " +"\n" + "🌡Температура:" + " " +  temp1 + "\n" + "☀️Прогноз:" + " " +  temp1_icon + "\n" + "💨Швидкість вітру:" + " " + wind1_1  + "\n" + "❓Вероїдність опадів:" + " " + probability1_1 + "\n" + "-------------------------------" )

	#Запис інформації в файл "5:00"

	with open("5:00.txt", "w") as file1:
		file1.write(" 👇👉Погода на 5:00👈👇 " +"\n" + "🌡Температура:" + " " +  temp2 + "\n" + "☀️Прогноз:" + " " +  temp2_icon + "\n" + "💨Швидкість вітру:" + " " + wind2_2 + "\n" + "❓Вероїдність опадів:" + " " + probability2_2 + "\n" + "-------------------------------")

	#Запис інформації в файл "8:00"

	with open("8:00.txt", "w") as file2:
		file2.write(" 👇👉Погода на 8:00👈👇 " +"\n" + "🌡Температура:" + " " +  temp3 + "\n" + "☀️Прогноз:" + " " +  temp3_icon + "\n" + "💨Швидкість вітру:" + " " + wind3_3 + "\n" + "❓Вероїдність опадів:" + " " + probability3_3 + "\n" + "-------------------------------")

	#Запис інформації в файл "11:00"

	with open("11:00.txt", "w") as file3:
		file3.write(" 👇👉Погода на 11:00👈👇 " +"\n" + "🌡Температура:" + " " +  temp4 + "\n" + "☀️Прогноз:" + " " +  temp4_icon + "\n" + "💨Швидкість вітру:" + " " + wind4_4 + "\n" + "❓Вероїдність опадів:" + " " + probability4_4 + "\n" + "-------------------------------")

	#Запис інформації в файл "14:00"

	with open("14:00.txt", "w") as file4:
		file4.write(" 👇👉Погода на 14:00👈👇 " +"\n" + "🌡Температура:" + " " +  temp5 + "\n" + "☀️Прогноз:" + " " +  temp5_icon + "\n" + "💨Швидкість вітру:" + " " + wind5_5 + "\n" + "❓Вероїдність опадів:" + " " + probability5_5 + "\n" + "-------------------------------")

	#Запис інформації в файл "17:00"

	with open("17:00.txt", "w") as file5:
		file5.write(" 👇👉Погода на 17:00👈👇 " +"\n" + "🌡Температура:" + " " +  temp6 + "\n" + "☀️Прогноз:" + " " +  temp6_icon + "\n" + "💨Швидкість вітру:" + " " + wind6_6 + "\n" + "❓Вероїдність опадів:" + " " + probability6_6 + "\n" + "-------------------------------")

	#Запис інформації в файл "20:00"

	with open("20:00.txt", "w") as file6:
		file6.write(" 👇👉Погода на 20:00👈👇 " +"\n" + "🌡Температура:" + " " +  temp7 + "\n" + "☀️Прогноз:" + " " +  temp7_icon + "\n" + "💨Швидкість вітру:" + " " + wind7_7 + "\n" + "❓Вероїдність опадів:" + " " + probability7_7 + "\n" + "-------------------------------")

	#Запис інформації в файл "23:00"

	with open("23:00.txt", "w") as file7:
		file7.write(" 👇👉Погода на 23:00👈👇 " +"\n" + "🌡Температура:" + " " +  temp8 + "\n" + "☀️Прогноз:" + " " +  temp8_icon + "\n" + "💨Швидкість вітру:" + " " + wind8_8 + "\n" + "❓Вероїдність опадів:" + " " + probability8_8 + "\n" + "\n" + "    "  + "👇💥Загальний опис💥👇" + "\n"+ "\n" + "❗️" + description)
	
		


###################################################################################################################################################################################

###################################################################################################################################################################################

#Погода на данний момент

def get_content1(html):

	soup = BeautifulSoup(html, "html.parser") 
	items = soup.find_all("tbody")
	items1 = soup.find_all('div', class_="imgBlock")
	
#Отримання температури на данний момент

	for item in items1:
		temp_cur = item.find("p", class_="today-temp").get_text()
	

#Отримання стану погоди на жанний момент

	for item in items:
		temp_cur_icon = item.find("tr", class_="img weatherIcoS").find_next("td", class_="cur").find_next("div", class_="weatherIco").get("title")
	
		temp_cur_wind = item.find("tr", class_="gray").find_next("td", class_="cur").find_next("div", class_="Tooltip").get_text()

#Отримання стану вітру на данний момент

	r = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B7%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B6%D0%B6%D1%8F/10-%D0%B4%D0%BD%D1%96%D0%B2")
	html = bs4.BeautifulSoup(r.text, "html.parser")
	wind_cur = html.select(".gray  .cur .Tooltip")
	wind_cur_cur = wind_cur[0].get("data-tooltip")

#Отримання вероїдності опадів 

	r = requests.get("https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B7%D0%B0%D0%BF%D0%BE%D1%80%D1%96%D0%B6%D0%B6%D1%8F/10-%D0%B4%D0%BD%D1%96%D0%B2")
	html = bs4.BeautifulSoup(r.text, "html.parser")
	probability_cur = html.select(".weatherDetails .cur")
	probability_cur_cur = probability_cur[7].get_text() + "%"
	
#Збереження поданої інформації у файл "Current.txt"

	with open("current.txt", "w") as file8:
		file8.write("         " +  " ✅Погода на данний момент✅  " +"\n" + "🌡Температура:" + " " +  temp_cur + "\n" + "☀️Прогноз:" + " " +  temp_cur_icon + "\n" + "💨Швидкість вітру:" + " " + wind_cur_cur + "\n" + "❓Вероїдність опадів:" + " " + probability_cur_cur)

#####################################################################################################################################################################################
	

def parse():
	html = get_html(URL)
	if html.status_code == 200:
		#temp = []
		get_content(html.text)
		get_content1(html.text)
		
		#get_content(html.text)
		#saving(temp)
	else:
		print("Unknown page")


parse()
