from selenium import webdriver
import os
import sys

"""
@Author Nicolas Granados
A bot made for whattsappweb to annoy your friends
ex: python whattsapp_bot name_of_file name_of_chat
"""

class WhattsappBot():
  """
  We define a whattsappbot object
  """
  
  def __init__(self,file_name,chat):
    self.driver = webdriver.Chrome()
    self.chat = chat
    self.file_name = file_name

  def getin(self):
    self.driver.get("https://web.whatsapp.com/")
    input("Please Scan the QR then press enter: ") #wait until input

    elem = self.driver.find_element_by_xpath('//span[contains(text(),"%s")]'% self.chat)
    elem.click()

  def annoy(self):
    file = open(os.getcwd() + "/" +self.file_name)
    contents = file.read().split(" ")#change the split to " " if you wanna get even more annoying
    print(contents)

    text_in = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    enter_butt = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    
    for word in contents:
      text_in.send_keys(word)
      enter_butt.click()

if __name__ == '__main__':
  bot = WhattsappBot(sys.argv[1], sys.argv[2])

  bot.getin()

  bot.annoy()