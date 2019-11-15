from bs4 import BeautifulSoup
from sys import argv
import json
import requests

url = "https://www.hltv.org/ranking/teams/2019/november/11"
source = requests.get(url)
parser = BeautifulSoup(source.text, "html.parser")

player_source = parser.find_all('a', class_="pointer", href=True)

players_id_and_name = [player['href'] for player in player_source]

player_dict = {}

for element in players_id_and_name:
	temp = element.split('/')
	player_dict[temp[3]] = temp[2] 

with open('player_id_names.json', 'w') as f:
	json.dump(player_dict, f)	


def bretty_brind(player_dict):
	for k, v in player_dict.items():
		print(k, v)


# bretty_brind(player_dict)

players = open('player_id_names.json')
saved_dict = json.load(players)

print(saved_dict)
