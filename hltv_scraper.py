from bs4 import BeautifulSoup
from sys import argv
import requests
import re

#
# TODO:
# make it so you can type the name and threshold instead of id
# type team name and get thresholds for team members
#

player_id = argv[1]
kill_threshold = float(argv[2])
list_of_kills = []
url = "https://www.hltv.org/stats/players/matches/{}/x?startDate=2019-08-14&endDate=2019-11-14".format(player_id)

k_regex = '^[0-9]{1,2}'

source = requests.get(url)
parser = BeautifulSoup(source.text, "html.parser")

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