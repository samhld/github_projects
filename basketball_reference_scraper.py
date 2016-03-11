import requests
from bs4 import BeautifulSoup
import string
import pdb



def main():
	letters = list(string.ascii_lowercase)
	main_url_list = top_url_list(letters)
	print(main_url_list)

def top_url_list(letters):
	top_url_list = []
	for letter in letters:
		top_url_list.append("http://www.basketball-reference.com/players/%s" % letter)
	return top_url_list

if __name__ == '__main__':
	main()	

#	soup = BeautifulSoup(r.content)		soup.prettify()

#searches through '/a/' then '/b'....'/z/'
#and grabs the player naming convention 
#from the 'href' tag for each player link


#def get_each_player_url(names):

