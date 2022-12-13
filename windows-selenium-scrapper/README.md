# Selenium Allegro Price Scrapper


`WARNING! CREATOR OF THIS PROGRAM DO NOT GIVE ANY WARRANTY ON THE SCRIPT! THIS IS JUST A PROOF OF CONEPT OF DATA GATHERING SCRIPT, USED FOR RESEARCH AND EDUCATIONAL PURPOSE! PLEASE USE OFFICIAL ALLEGRO API!`


## How to use it?
1. Make sure you have Python 3.9 or newer, pip and 
2. Execute `pip install -r requirements.txt`
3. Download chromedriver https://chromedriver.chromium.org/downloads for your chrome version
4. `python selenium_scrapper.py`
5. App won't probably work, so you have to fix it by hand according to changes in Allegro
6. You can also specify your own use profiles in line 19, 20
   
   ` options.add_argument(r"--user-data-dir="+os.path.abspath("./ChromeProfile"))
    options.add_argument(r'--profile-directory=Profile 17')`
7. Good luck :)