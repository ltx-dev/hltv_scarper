from bs4 import BeautifulSoup
from sys import argv
from datetime import date
from dateutil.relativedelta import relativedelta
import requests
import re
import json

#
# TODO:
# type team name and get thresholds for team members
# clean this bloody mess up, considering creating a method which
# learn about tests
#

player_id = ""#argv[1]
f = open("player_id_names.json")
player_ids = json.load(f)
#
# Regex strings
#
k_regex = '^[0-9]{1,2}'
input_id_regex = '^[0-9]{2,5}'

#
# If the input matches the id regex, set variable to id
# otherwise, find the name by id key inside players_ids dictionary
#
if re.match(input_id_regex, argv[1]):
	player_id = argv[1]
else:
	player_id = player_ids[argv[1]]

date_today = date.today()
date_three_months_ago = date_today - relativedelta(months=3) # (today - 3 months)
#
# if player name exists, assign id
#
kill_threshold = float(argv[2])
list_of_kills = []
url = "https://www.hltv.org/stats/players/matches/{}/x?startDate={}&endDate={}".format(player_id, str(date_three_months_ago), str(date_today))

source = requests.get(url)
parser = BeautifulSoup(source.text, "html.parser")

#
# List of elements we find
#
list_of_kills = parser.find_all('td', class_="statsCenterText")
list_of_kills = [int(re.match(k_regex, element.text.strip()).group()) for element in list_of_kills]
player_name = parser.find('span', class_="standard-headline")
player_name = player_name.text.split(' ')[-1] # this probably can be done better

below_threshold = [n for n in list_of_kills if n < kill_threshold]
below_percentage = (len(below_threshold) / len(list_of_kills)) * 100
above_percentage = 100 - below_percentage

print(player_name)
print("Below threshold: {0:.2f}%".format(below_percentage))
print("Above threshold: {0:.2f}%".format(above_percentage))