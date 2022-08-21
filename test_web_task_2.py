import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


CHROME_DRIVER_PATH = r"C:\Users\alisa\Downloads\chromedriver.exe"
url = 'https://yandex.ru/'
time_to_wait = 10


def test_search_planet_for_me_by_yandex():
    target_url = 'https://planetfor.me/'
    search_query = "Planet for me"

    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    driver.get(url)

    assert "Яндекс" in driver.title

    try:
        yandex_search_input = WebDriverWait(driver, time_to_wait).until(
            EC.presence_of_element_located((By.CLASS_NAME, "mini-suggest__input")))
        yandex_search_input.clear()
        yandex_search_input.send_keys(search_query)

        yandex_search_button = WebDriverWait(driver, time_to_wait).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search2__button')))
        yandex_search_button.click()

        founded = True
        try:
            driver.find_element(By.XPATH, '//a[@href="' + target_url + '"]')
        except NoSuchElementException:
            founded = False

        assert founded

        planet_for_me_link = WebDriverWait(driver, time_to_wait).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="'+target_url+'"]')))
        planet_for_me_link.click()

        driver.switch_to.window(driver.window_handles[1])

        planet_for_me_search_input = WebDriverWait(driver, time_to_wait).until(
            EC.presence_of_element_located((By.XPATH, '//input[@data-qa="navbar-search-input"]')))

        planet_for_me_search_input.clear()
        planet_for_me_search_input.send_keys("qa")
        planet_for_me_search_input.send_keys(Keys.RETURN)

        assert "Ничего не найдено :(" not in driver.page_source

    except TimeoutException:
        driver.quit()

    driver.close()