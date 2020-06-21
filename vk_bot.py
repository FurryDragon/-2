import bs4 as bs4
import requests

u = 0
class VkBot:

    def __init__(self, user_id):
        print("\nСоздан объект бота!")
        self._USER_ID = user_id
        self._USERNAME = self._get_user_name_from_vk_id(user_id)
        self._COMMANDS = ["ПРИВЕТ", "", "ВРЕМЯ", "ПОКА", "ХОЧУ", "ДАТА", "ПОГОДА", "НОВОСТИ"]

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]

    def new_message(self, message):

        if message.upper() ==  self._COMMANDS[0]:
            return f"Привет-привет, {self._USERNAME}!"

        elif message.upper() == self._COMMANDS[1]:
            return 

        elif message.upper() == self._COMMANDS[2]:
            return self._get_time()

        elif message.upper() == self._COMMANDS[4]:
            return f"Теперь вы получаете оповещение о бесплатной еде!"

        elif message.upper() == self._COMMANDS[3]:
            return f"Пока, {self._USERNAME}!"

        elif message.upper() == self._COMMANDS[5]:
            return self._get_date()

        elif message.upper() == self._COMMANDS[6]:
            return self._get_pogoda()

        elif message.upper() == self._COMMANDS[7]:
            return self._get_food()            

        else:
            return "Повторите, я не понимаю\n Доступные команды: ПРИВЕТ, ВРЕМЯ, ПОКА, ХОЧУ, ДАТА, ПОГОДА, НОВОСТИ"

    def _get_time(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b = bs4.BeautifulSoup(request.text, "html.parser")
        return self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]

    def _get_date(self):
        request = requests.get("https://my-calend.ru/date-and-time-today")
        b1 = bs4.BeautifulSoup(request.text, "html.parser")
        return self._clean_all_tag_from_str(str(b1.select(".page")[0].findAll("h2")[0]))


    def _get_pogoda(self):
        new_news = []
        news = []
        request = requests.get("https://yandex.ru/pogoda/veliky-novgorod?utm_source=serp&utm_campaign=wizard&utm_medium=desktop&utm_content=wizard_desktop_main&utm_term=title&lat=58.544247&lon=31.228358")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        news = soup.findAll('div', class_='temp fact__temp fact__temp_size_s')
        for i in range(len(news)):
            if news[i].find('span', class_='temp__value') is not None:
                new_news.append(news[i].text)
        for i in range(len(new_news)):
            return self._clean_all_tag_from_str(new_news[i])

    def _get_food(self):
        new_news = []
        news = []
        request = requests.get("https://m.vk.com/sharingfood")
        soup = bs4.BeautifulSoup(request.text, "html.parser")
        news = soup.findAll('div', class_='wi_body')
        for i in range(len(news)):
            if news[i].find('div', class_='pi_text') is not None:
                new_news.append(news[i].text)
        for i in range(len(new_news)):
            return self._clean_all_tag_from_str(new_news[1]) + "dwdwd"

    @staticmethod
    def _clean_all_tag_from_str(string_line):

        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """

        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result