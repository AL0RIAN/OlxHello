import json

from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium_stealth import stealth
import time


def say_hello(link):
    link.click()

    time.sleep(7)

    user = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div[3]/div[2]/div[2]/div[2]/div/a")

    time.sleep(7)

    with open("../../../Python/SeleniumBasic/basic/result.txt", "a") as file:
        file.write(user.get_attribute("href") + "\n")

    time.sleep(3)

    try:
        pop_btn = driver.find_element(By.CLASS_NAME, "css-1l30vq6")
        pop_btn.click()
    except NoSuchElementException:
        pass

    button = driver.find_element(By.CLASS_NAME, "css-14w9s9k")
    button.click()

    time.sleep(5)
    driver.find_element(By.TAG_NAME, "textarea").send_keys("Доброго Дня!")
    driver.get("https://www.olx.ua/")


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.implicitly_wait(2)
driver.get("https://www.olx.ua/uk/myaccount/")

with open("../../../Python/SeleniumBasic/basic/YOUR_COOKIE.json", 'r') as file:
    cookies = json.load(file)

for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(2)

driver.refresh()

driver.get("https://www.olx.ua/")
time.sleep(5)

action = ActionChains(driver)

for post in range(10):
    time.sleep(5)
    block = driver.find_element(By.ID, "gallerywide")
    posts = block.find_elements(By.TAG_NAME, "li")
    link = posts[post].find_element(By.XPATH, f'//*[@id="gallerywide"]/li[{post + 1}]/div[1]/a')
    action.move_to_element(link)
    say_hello(link=link)

driver.quit()
