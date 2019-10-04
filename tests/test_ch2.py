from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_google_search():
    driver = webdriver.Chrome()
    # go to google.com
    driver.get('https://www.google.com')

    # find search input and type puppies
    driver.find_element(By.NAME, 'q').send_keys('puppies', Keys.ENTER)

    # assert puppies is on page
    assert driver.title.__contains__('puppies')

    driver.quit()
