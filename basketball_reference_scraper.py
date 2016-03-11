import requests
from bs4 import BeautifulSoup
import string
import pdb
from urllib.request import urlopen
import re



def main():
	letters = list(string.ascii_lowercase)
	player_urls = get_top_urls(letters)
	#player_urls = get_player_urls(top_url_list)

	#print(main_url_list)
	print(player_urls)

def get_top_urls(letters):
	top_url_list = []
	for letter in letters:
		top_url_list.append("http://www.basketball-reference.com/players/%s" % letter)

	#return top_url_list

#takes top_url_list and, for each item, creates another list of all the urls with player naming conventions
#pdb.set_trace()
#def get_player_urls(top_url_list):
	player_urls = []
	for i in top_url_list:
		#r = requests.get(top_url_list[i])
		#soup = BeautifulSoup(r.content)
		#url = "http://www.basketball-reference.com/players/a/"
		result = re.findall("\/([a-z]+[0-9][0-9]\W[a-z]+)", str(urlopen(i).read()))
		player_urls.append(result) 
	return player_urls


if __name__ == '__main__':
	main()	







