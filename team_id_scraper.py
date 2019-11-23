import requests
from bs4 import BeautifulSoup
import re
#
# class="teamCol-teams-overview" 
# /stats/teams/7092/5POWER?startDate=2019-08-23&endDate=2019-11-23"
#

# regex variables
#
#
regex_id = "(\d{4,5})"
# test = "/stats/teams/8008/Grayhound?startDate=2019-08-23&endDate=2019-11-23"

# print(re.search(regex_id, test).group())


# Insert proper dates (date.now - 3months)
url = "https://www.hltv.org/stats/teams?startDate=2019-08-23&endDate=2019-11-23"

# Parsing stuff
source = requests.get(url)
parser = BeautifulSoup(source.text, "html.parser")
team_source = parser.find_all('td', class_="teamCol-teams-overview")
team_dict = {}
href = []

for element in team_source:
	for a in element:
		print(re.match(regex_id, str(a.get('href'))))
	# print(element.text)

	# for a in data.find_all('a'):
	# 	href.append(a.get('href'))	

