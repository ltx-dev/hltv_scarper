import json

#
# STS
# 
json_resp = json.loads(' {"oppty_info_number":"4171","id_odds":"595685445","odds_value":"1.42","id_opportunity":"233433056","match_name":"TyLoo - MiBR","tip_name_formated":"MiBR","oppty_type_name":"mecz","tip_name":"2"}')

print(json_resp['tip_name_formated'])
print(json_resp['odds_value'])