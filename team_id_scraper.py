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
regex_id_team_name = "\/teams\/(.*)\?"
test = "/stats/teams/8008/Grayhound?startDate=2019-08-23&endDate=2019-11-23"
# Insert proper dates (date.now - 3months)
url = "https://www.hltv.org/stats/teams?startDate=2019-08-27&endDate=2019-11-27&rankingFilter=Top50"

# Parsing stuff
source = requests.get(url)
parser = BeautifulSoup(source.text, "html.parser")
team_source = parser.find_all('td', class_="teamCol-teams-overview")
team_dict = {}
href = []

# for element in team_source:
# 	for a in element:
# 		if (a.get('href')) is not None:
# 			href.append(str(re.search(regex_id,a.get('href')).group()))

for element in team_source:
	for a in element:
		if a is not None:
		    href.append(re.findall(regex_id_team_name, str(a.get('href'))))

print(href)		    

