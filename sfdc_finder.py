import requests
from bs4 import BeautifulSoup

#program takes a list of domains 

domains = #put a list of domains in here (csv?)

#create url_list by pasting builtwith url to each company domain
#contained in 'domains'
#then separate with commas
def create_url_list(domains):
	url_list = []
	for domain in domains:
		url_list += requests.get("http://builtwith.com/" + domain + ",")
 

	return url_list

create_url_list(domains)

#define function that takes a list of urls
#then creates html_docs for them using BeautifulSoup
#then checks the link text for "salesforce"
#then, if contained in link text, adds company domain to 'sfdc_list'
def get_all_sfdc(url_list):
	
	#parses each url into BeautifulSoup html
	for url in url_list:
		r = requests.get(url)
		soup = BeautifulSoup(r.content)
		html_doc = soup.prettify()
		sfdc_list = []
		#finds 'salesforce' in link text of each url
		for link in soup.find_all("a"):
			
			if ("salesforce" in link.text):
				sfdc_list += soup.find("h1").text
	return 	sfdc_list	

get_all_sfdc(url_list)








        