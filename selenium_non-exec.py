from selenium import webdriver

import requests
from bs4 import BeautifulSoup
import string
import pdb
from urllib.request import urlopen
import re



def main():
	letters = list(string.ascii_lowercase)
	top_url_list = get_top_urls(letters)
	player_urls = get_player_urls(top_url_list)

	#print(main_url_list)
	print(player_urls)

def get_top_urls(letters):
	top_url_list = []
	for letter in letters:
		top_url_list.append("http://www.basketball-reference.com/players/%s" % letter)

	return top_url_list

for i in top_url_list:
	driver = webdriver.Firefox()
	driver.get(top_url_list[i])	
	driver.find_element_by_xpath('//*[@id="players"]/tbody/tr[%s]/td[1]/a' % (i+1)
	return 