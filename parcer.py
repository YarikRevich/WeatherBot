import requests,bs4
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class Parcer:


    def __init__(self,url,user_id_bot,lang="ua."):

        #The stucture of constructor

        self.url = "https://{1}sinoptik.ua/погода-{0}".format(url,lang)
        self.lang = lang
        if self.lang == "ua.":
            self.url_ten_days = "https://{1}sinoptik.ua/погода-{0}/10-днів".format(url,lang)
        else:
            self.url_ten_days = "https://{1}sinoptik.ua/погода-{0}/10-дней".format(url,lang)
        self.used_id_bot = user_id_bot
        db = MongoClient("localhost",27017)
        database = db["weatherbot"]
        self.collection = database["info"]
    def get_data(self):

        #Connect to the custom Mongo
        try:
            self.collection.insert({"_id":self.used_id_bot})
        except DuplicateKeyError:
            pass
        

        #Make request

        html = requests.get(self.url)
        html_ten_days = requests.get(self.url_ten_days)

        #Check request and make a soup

        if html.status_code == 200:
            soup = BeautifulSoup(html.text,features="html.parser")
            soup_ten_days = bs4.BeautifulSoup(html_ten_days.text,features="html.parser")
            item = soup.find_all("tbody")
            item_ten = soup_ten_days.find_all("tbody")

            #Start parsing
            
            despription = soup.find_all("div",class_="wDescription clearfix")

            list_of_temp = []
            list_of_info = []

            for number in range(1,9):
                for items in item:
                    info = items.find("tr", class_="temperature").find_next("td",class_="p{}".format(str(number))).get_text()
                    title = items.find("tr", class_="img weatherIcoS").find_next("td", class_="p{}".format(str(number))).find_next("div", class_="weatherIco").get("title")
                    list_of_temp.append(info)
                    list_of_info.append(title)

            self.collection.update({"_id":self.used_id_bot},{"$set":{"temp":list_of_temp,"info":list_of_info}})

            for despriptions in despription:   
                descpript = despriptions.find("div", class_="description").get_text()

                #Save to db

                self.collection.update({"_id":self.used_id_bot},{"$set":{"desription":descpript}})

            list_of_wind = []
            list_of_det = []
            for wind in range(1,9):
                wind_status = soup_ten_days.select(".gray .p{} .Tooltip".format(str(wind)))
                wind_main = wind_status[0].get("data-tooltip")
                details = soup_ten_days.select(".weatherDetails .p{}".format(str(wind)))
                details_main = details[7].get_text() + "%"
                list_of_wind.append(wind_main)
                list_of_det.append(details_main)
                #Save to db

            self.collection.update({"_id":self.used_id_bot},{"$set":{"wind":list_of_wind,"detail":list_of_det}})

            temperature_now = soup.find_all("div", class_="imgBlock")
            for temp in temperature_now:
                temperature = temp.find("p", class_="today-temp").get_text()

                #Save to db

                self.collection.update({"_id":self.used_id_bot},{"$set":{"curr_temp":temperature}})

            
            for item_now in item_ten:
                icon = item_now.find("tr", class_="img weatherIcoS").find_next("td", class_="cur").find_next("div", class_="weatherIco").get("title")
                now_wind = item_now.find("tr", class_="gray").find_next("td", class_="cur").find_next("div", class_="Tooltip").get_text()

                #Save to db
                self.collection.update({"_id":self.used_id_bot},{"$set":{"state_of_weather":icon,"wind_state":now_wind}})
                
            state_of_wind = soup_ten_days.select(".gray .cur .Tooltip")
            current_state_wind = state_of_wind[0].get("data-tooltip")
            probability = soup_ten_days.select(".weatherDetails .cur")
            current_probability = probability[7].get_text() + "%"

            #Save to db

            self.collection.update({"_id":self.used_id_bot},{"$set":{"curr_state_of_wind":current_state_wind,"curr_probability":current_probability}})
    
    def full_info(self):
        full = {}
        for number in range(1,8):
            for info in self.collection.find({"_id":self.used_id_bot}):
                full[number] = [info["info"][number],info["temp"][number],info["detail"][number],info["wind"][number]]
        return full
    def current(self):
        current = {}
        for curr in self.collection.find({"_id":self.used_id_bot}):
            current["curr"] = [curr["curr_temp"],curr["state_of_weather"],curr["curr_probability"],curr["curr_state_of_wind"]]
        return current



