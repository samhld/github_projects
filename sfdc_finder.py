import requests
from bs4 import BeautifulSoup
import pdb

#program takes a list of domains 

def main():
	domains = [
		"talkiq.com",
		"insidesales.com"
	]
	url_list = create_url_list(domains)
	sfdc_list = get_all_sfdc(url_list)
	print(sfdc_list)

#create url_list by pasting builtwith url to each company domain
#contained in 'domains'
#then separate with commas
def create_url_list(domains):
	url_list = []
	for domain in domains:
		url_list.append("http://builtwith.com/%s" % domain)
	#print(url_list)
	return url_list

# create_url_list(domains)

#define function that takes a list of urls
#then creates html_docs for them using BeautifulSoup
#then checks the link text for "salesforce"
#then, if contained in link text, adds company domain to 'sfdc_list'
def get_all_sfdc(url_list):
	
	#parses each url into BeautifulSoup html
	for url in url_list:
		r = requests.get(url)
		soup = BeautifulSoup(r.content, "html.parser")
		html_doc = soup.prettify()
		sfdc_list = []
		#finds 'salesforce' in link text of each url
		for link in soup.find_all("a"):
			
			if ("salesforce" in link.text):
				pdb.set_trace()
				sfdc_list += soup.find("h1").text
				#<h1 class="homeH1 profileH1">INSIDESALES.COM</h1>
	return 	sfdc_list	

if __name__ == "__main__":
	main()
