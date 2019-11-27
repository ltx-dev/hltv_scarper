import re

regex_id = "(\d{4,5})"
regex_id_team_name = "\/teams\/(.*)\?"

test = "/stats/teams/8008/Grayhound?startDate=2019-08-23&endDate=2019-11-23"

match_find = re.findall(regex_id_team_name, test) works

print(match_find)