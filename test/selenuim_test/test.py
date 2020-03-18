from selenium import webdriver 
from time import sleep
from selenium.webdriver.common.keys import Keys
import unittest


class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        

    def giveElement(self, path):
        return self.driver.find_element_by_xpath(path)

    def go_to(self, webiste):
        self.driver.get(webiste)

    def showAll(self):
        show_all_button_path = '/html/body/div[2]/button[1]'
        show_all_button = self.giveElement(show_all_button_path)
        show_all_button.click()

    def topFive(self):
        top_five_button_path = '/html/body/div[2]/button[2]'
        top_five_button = self.giveElement(top_five_button_path)
        top_five_button.click()
    
    def worstFive(self):
        worst_five_button_path = '/html/body/div[2]/button[3]'
        worst_five_button = self.giveElement(worst_five_button_path)
        worst_five_button.click()

    def searchRoom(self, room):
        search_box_path = '//*[@id="query"]'
        search_box = self.giveElement(search_box_path)
        search_box.send_keys(room)

        search_button_path = '/html/body/div[2]/div/form/span/button'
        search_button = self.giveElement(search_button_path)
        search_button.click()


    def tearDown(self):
        self.driver.close()



def main():
    bot = Bot()

    # go to the website
    bot.go_to('https://radiant-sea-21897.herokuapp.com/')

    # Do the following tests 10 times 
    for i in range(10):
        # check the top 5 Rooms
        sleep(2)
        bot.topFive()

        # check the worst 5 rooms 
        sleep(2)
        bot.worstFive()

        # show all the room 
        sleep(2)
        bot.showAll()

        # search for room 14-237
        sleep(2)
        bot.searchRoom("14-237")

    bot.tearDown()

if __name__ == "__main__":
    main()

 