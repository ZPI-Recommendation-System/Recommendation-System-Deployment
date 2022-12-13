import random
from time import sleep
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

cookies = [
    {
        "name": "gdpr_permission_given",
        "value": "1",
        "domain": "allegro.pl",
        "path": "/"

    }
]
options = webdriver.ChromeOptions()
# options.add_argument(r"--user-data-dir="+os.path.abspath("./ChromeProfile"))
# options.add_argument(r'--profile-directory=Profile 17')
driver = webdriver.Chrome(options=options)

filter_string = 'stan=nowe&offerTypeBuyNow=1'


def get_product(article: WebElement):
    price = article.find_element(By.XPATH, ".//span[contains(text(), 'zł')]").find_element(By.XPATH, "..").text
    name_href = article.find_element(By.XPATH, ".//a[@title]")
    name = name_href.text
    url = name_href.get_attribute("href")
    return {"price": price, "name": name, "url": url}


def scrap_page(base_url, page, output):
    print(f"CURRENT PAGE {page} {base_url}")
    driver.get(f"{base_url}?{filter_string}&p={page}")
    if block_captcha():
        driver.get(f"{base_url}?{filter_string}&p={page}")

    for e in (driver.find_elements(By.TAG_NAME, "article")):
        try:
            p = (get_product(e))
            print(p)
            output.write(f"'{p['name']}'\t'{p['price']}'\t'{p['url']}'\t'{base_url}'\n")
        except:
            print("ERror with product " + e.text)


def check_captcha():
    print("Checking for captcha....")
    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    print(body_text)
    if "captcha" in body_text:
        print("CAPTCHA")
        return True
    if "potwierdź, że jesteś człowiekiem" in body_text:
        print("CAPTCHA!")
        return True
    try:
        driver.find_element(By.ID, "recaptcha-token")
        print("CAPTCHA")
        return True
    except:
        try: 
            driver.find_element(By.CLASS_NAME, "captcha-container")
            print("CAPTCHA")
            return True
        except:
            return False


def get_number_of_pages(page):
    driver.get(page + "?" + filter_string)
    nav = driver.find_element(By.XPATH, "//div[@role='navigation']/span")
    return int(nav.text)


def get_categories():
    list_cat = []
    driver.get(f"https://allegro.pl/kategoria/laptopy-491?{filter_string}")
    sleep(5)
    if block_captcha():
        driver.get(f"https://allegro.pl/kategoria/laptopy-491?{filter_string}")
    print("WTF?")
    try:
        driver.find_element(By.XPATH, "//*[@id='filters']/div[1]/div/div/div/section/div[2]/button").click()
    except BaseException as e:
        print(e)
        pass
    categories = driver.find_element(By.XPATH, "//div[@data-role='Categories']")
    for e in categories.find_elements(By.XPATH, ".//a[@href]"):
        list_cat.append(e.get_attribute("href"))
    return list_cat


def block_captcha():
    if check_captcha():
        sleep(3)
        while check_captcha():
            sleep(3)
            print("Waiting for user input...")
        return True
    else:
        return False

driver.get(f"https://allegro.pl/kategoria/laptopy-491?{filter_string}")

input("Please, solve potential captcha, accept GDPR request and make screen full screen. Then click enter")

cat = (get_categories())
# cat = ['https://allegro.pl/kategoria/laptopy-toshiba-dynabook-77924',
#        'https://allegro.pl/kategoria/laptopy-inne-marki-315455']
# cat = ['https://allegro.pl/kategoria/laptopy-hp-compaq-77919', 'https://allegro.pl/kategoria/laptopy-huawei-257180', 'https://allegro.pl/kategoria/laptopy-hyperbook-319099', 'https://allegro.pl/kategoria/laptopy-ibm-lenovo-77920', 'https://allegro.pl/kategoria/laptopy-kiano-258398', 'https://allegro.pl/kategoria/laptopy-kruger-matz-315410', 'https://allegro.pl/kategoria/laptopy-maibenben-316010', 'https://allegro.pl/kategoria/laptopy-medion-257162', 'https://allegro.pl/kategoria/laptopy-microsoft-257723', 'https://allegro.pl/kategoria/laptopy-msi-77921', 'https://allegro.pl/kategoria/laptopy-samsung-77922', 'https://allegro.pl/kategoria/laptopy-sony-77923', 'https://allegro.pl/kategoria/laptopy-toshiba-dynabook-77924', 'https://allegro.pl/kategoria/laptopy-inne-marki-315455']
print(cat)

with open("output.csv", mode="a", encoding="utf-8") as output:
    for e in cat:
        print("Scrapping", e)
        for i in range(1, get_number_of_pages(e) + 1):
            scrap_page(e, i, output)
            sleep(random.randint(1, 4))

# while True:
#     driver.get(f"https://allegro.pl/produkt/laptop-lenovo-ideapad-3-15itl6-15-6-intel-core-i5-8-gb-512-gb-szary-{random.randint(0, 100000)}-a227-482f-82e8-0e4a21839f19?bi_m=search_suggester")
