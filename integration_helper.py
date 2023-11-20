import requests
from bs4 import BeautifulSoup


def get_swedish_fake_personal_data():
    fejk_se_response = BeautifulSoup(requests.get("https://fejk.se/").content)
    full_name = fejk_se_response.find(string="Namn:").parent.findNextSibling().text.split(" ")
    phone = fejk_se_response.find(string="Telefon:").parent.findNextSibling().text
    return {"first_name": full_name[0], "last_name": full_name[1], "phone": phone}
