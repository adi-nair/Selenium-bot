from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time
chrome_driver_path = 'D:\Python_projs\Intermediate\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
products = driver.find_elements_by_css_selector("#store div")
products.reverse()

timeout = time.time() + 5
five_min = time.time() + 60 * 5
is_game = True


def check_time():
    speed_element = driver.find_element_by_id("cps")
    speed = speed_element.text.split(" ")[-1]
    print(f"Cookies per second: {speed}")

while is_game:
    cookie.click()
    if time.time() > timeout:
        for prod in products:
            try:
                if prod.get_attribute('class') == "":
                    prod.click()
            except StaleElementReferenceException:
                products = driver.find_elements_by_css_selector("#store div")

        timeout = time.time() + 5
    if time.time() > five_min:
        check_time()
        is_game = False

driver.quit()
