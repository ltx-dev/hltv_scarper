from bs4 import BeautifulSoup
from sys import argv
import requests
import re

#
# TODO:
# scrape list of players and their ids, find a way to save it sensibly
#

player_id = argv[1]
kill_threshold = float(argv[2])
list_of_kills = []
# url = "https://www.hltv.org/stats/players/matches/{}/JUGi?startDate=2019-08-14&endDate=2019-11-14".format(player_id)
url = "https://www.hltv.org/stats/players/matches/{}/x?startDate=2019-08-14&endDate=2019-11-14".format(player_id)

k_regex = '^[0-9]{1,2}'


source = requests.get(url)
parser = BeautifulSoup(source.text, "html.parser")

list_of_kills = parser.find_all('td', class_="statsCenterText")
list_of_kills = [int(re.match(k_regex, element.text.strip()).group()) for element in list_of_kills]

player_name = parser.find('span', class_="standard-headline")
player_name = player_name.text.split(' ')[-1] # this probably can be done better

below_threshold = [n for n in list_of_kills if n < kill_threshold]
# get the percentage of matches below given threshold
below_percentage = (len(below_threshold) / len(list_of_kills)) * 100
above_percentage = 100 - below_percentage

print(player_name)
print("Below threshold: {0:.2f}%".format(below_percentage))
print("Above threshold: {0:.2f}%".format(above_percentage))
#
# XANT 18.5, 7938
# tabseN 19.5 5794
# smooya 17.5 11271
# hunter 19.5 3972
# kennys 18.5 7167
# nexa 16.5 9618
#