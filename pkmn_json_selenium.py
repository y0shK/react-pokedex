import selenium
import json

from selenium import webdriver
from selenium.webdriver.common.by import By

# selenium installed in conda env but not working with python test1.py
# use the following command:

# python -m pip install -U selenium 
# https://stackoverflow.com/questions/43797328/modulenotfounderror-no-module-named-selenium

# hello world selenium script written from docs example
# adapted to get json information and print it, without cache

# https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

# no cache used - this script is for learning purposes only

driver = webdriver.Chrome()

"""
get_pokemon_json_info(driver, name)

Takes a selenium webdriver for a specific browser and a Pokemon name
Writes a JSON file containing Pokemon info to the appropriate directory
"""

def get_pokemon_json_info(driver, name):

    # preprocess name
    name_lower = name.lower()

    driver.get("https://pokeapi.co/api/v2/pokemon/" + name_lower)

    # https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el 
    # use find_element by tag name

    # https://selenium-python.readthedocs.io/locating-elements.html

    pre = driver.find_element(By.TAG_NAME, "pre").text
    data = json.loads(pre)
    print(data)

    pkmn_str = name_lower + '_data.json'
    

    # https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file

    with open(pkmn_str, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

get_pokemon_json_info(driver, 'empoleon')

driver.close()
