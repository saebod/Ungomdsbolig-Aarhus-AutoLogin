from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time 

username = "Mitbrugernavn123"
password = "Minmkode123"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://ungdomsboligaarhus.dk/")
username_textbox = driver.find_element_by_id("edit-name")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("edit-pass")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id("edit-submit")
login_button.submit()
time.sleet(5)
driver.quit()
