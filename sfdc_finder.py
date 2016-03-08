import requests
from bs4 import BeautifulSoup

r = requests.get("http://builtwith.com/talkiq.com")

soup = BeautifulSoup(r.content)
html_doc = soup.prettify()

#definte a function that takes an html doc (i.e. 'html_doc')
#and determines whether 'salesforce' in present anywhere in its 'links'
def get_sfdc(html_doc):
 	sfdc_list = []
    #for link in soup.find_all("a"):
    if ("salesforce" in link.text):
    	return True 


#option two is define a function that takes a list of urls
#then creates html_docs for them using BeautifulSoup
#then checks the link text for "salesforce"
#then, if contained in link text, adds company domain to 'sfdc_list'
def get_all_sfdc(url_list):
	
	#parses each url into BeautifulSoup html
	for url in url_list:
		r = requests.get(url)
		soup = BeautifulSoup(r.content)
		html_doc = soup.prettify()
		#finds 'salesforce' in link text of each url
		for link in soup.find_all("a"):
			sfdc_list = []
			if ("salesforce" in link.text):
				sfdc_list += 










        