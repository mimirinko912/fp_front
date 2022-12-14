# importing library
import eel
import numpy
from math import sqrt
# initialize

def count_special_char(name: str) -> int:
	special_char: list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@']
	special_char_count: int = 0
	for c in name:
		if c in special_char:
			special_char_count += 1

	return special_char_count

def valuation_mapping(valuation: int) -> int:
	half = sqrt(10)
	scientific: list = '{:e}'.format(valuation).split('e')
	tail: float = float(scientific[0])
	power: int = int(scientific[1])
	if tail >= half:
		power += 1

	return power

eel.init("../fp_front")

@eel.expose
# below should be our model
def pred(name,fy,city,nation,industry,founder,investory,tf,ct,os,ls):
    #frame = name,fy,city,nation,industry,founder,investory,tf,ct,os,ls
    #feature truly used:
    # name_len
    # name special char
    # city
    # country
    # industry
    # investor
    # last valuation

    # length of company name
    name_length = ("".join(name)).__len__()
    # special char counts of company name
    name_sp = count_special_char("".join(name))
    #country name
    country_n = ("".join(nation)).lower()
    country_value = 0
    if city_name == "united states":
        city_value = 0
    elif city_name == "china":
        city_value = 1

    #city
    city_name = ("".join(city)).lower()
    #default
    city_value = 0
    if city_name == "san francisco":
        city_value = 0
    elif city_name == "new york":
        city_value = 1


    #this sould be button or scroll to choose
    industry_type = ("".join(industry)).lower()
    industry: dict = {'artificial intelligence': 0, 'fintech': 1, 'internet software & services': 2, 'analytics': 3, 'biotechnology': 4, 'health care': 5, 'e-commerce & direct-to-consumer': 6}

    #this sould be button or scroll to choose
    investor_type = ("".join(investor)).lower()
    investor: dict = {'andreessen horowitz': 0, 'techstars': 1, 'alumni ventures': 2, 'y combinator': 3, 'sequoia capital': 4, '500 global': 5, 'insight partners': 6}

    #last valuation
    last_value = ls.map(valuation_mapping)

    output = "here should be prediction"
    return output

# start
eel.start('myWebpage.html')
