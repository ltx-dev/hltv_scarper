from bs4 import BeautifulSoup
from sys import argv
import requests
import re
import json


# TODO:
# clean this bloody mess up, considering creating a method which
# finds out what date is it today so we can put it in the url start and end date string
#
# make it so you can type the name and threshold instead of id
# type team name and get thresholds for team members
#

# f = open("player_id_names.json")
# player_ids = json.load(f)

player_id = argv[1]

# if player name exists, assign id

kill_threshold = float(argv[2])
list_of_kills = []
url = "https://www.hltv.org/stats/players/matches/{}/x?startDate=2019-08-15&endDate=2019-11-15".format(player_id)

k_regex = '^[0-9]{1,2}'
time_frame_filter_regex = 'startDate.*[0-9]{2}'

source = requests.get(url)
parser = BeautifulSoup(source.text, "html.parser")

#
# List of elements we find
#
list_of_kills = parser.find_all('td', class_="statsCenterText")
list_of_kills = [int(re.match(k_regex, element.text.strip()).group()) for element in list_of_kills]
time_filter_date = parser.select('select > option')

for node in time_filter_date:
	if node.text == "Last 3 months":
		time_filter_date = str(node['data-link'])
		# print(str(node['data-link']))
		break

#
# startDate=2019-08-15&endDate=2019-11-15 format
#
# time_filter_date = str(time_filter_date)
time_filter_date = re.search(time_frame_filter_regex, time_filter_date).group()
print(time_filter_date)

player_name = parser.find('span', class_="standard-headline")
player_name = player_name.text.split(' ')[-1] # this probably can be done better

below_threshold = [n for n in list_of_kills if n < kill_threshold]
below_percentage = (len(below_threshold) / len(list_of_kills)) * 100
above_percentage = 100 - below_percentage

print(player_name)
print("Below threshold: {0:.2f}%".format(below_percentage))
print("Above threshold: {0:.2f}%".format(above_percentage))