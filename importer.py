from time import sleep
from Models.Champion import Champion

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def import_data_from_lolalytics(url="https://lolalytics.com/lol/tierlist/?region=euw"):
    driver = webdriver.Edge()
    driver.get(url)
    sleep(1)
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.END)
    sleep(2)

    results = []
    items_container = driver.find_element(By.XPATH, "/html/body/main/div[6]")
    items = items_container.find_elements(By.XPATH, "./div[position() >= 3]")

    for item in items:

        name = item.find_element(By.XPATH, ".//div[3]/a").text
        position = item.find_element(By.XPATH, ".//div[5]/div/img").get_attribute("alt").replace(" lane", "")
        winrate = item.find_element(By.XPATH, ".//div[6]/div/span").text

        champion = Champion(name, position, winrate)
        results.append(champion)

    return results

