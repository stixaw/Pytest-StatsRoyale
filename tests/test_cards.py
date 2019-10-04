from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_ice_spirit_card_is_displayed():
    driver = webdriver.Chrome()
    # go to statsroyale.com
    driver.get('https://statsroyale.com/cards')

    # driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()

    # get Ice Spirit card
    ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    print('ice_spirit_card', type(ice_spirit_card))

    assert ice_spirit_card.is_displayed()

    driver.quit()


def test_ice_spirit_card_is_not_displayed():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com/cards')

    common_input = driver.find_element(By.ID, 'common-cards')
    common_input.click()

    ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")

    assert not ice_spirit_card.is_displayed()

    driver.quit()


def test_ice_spirit_stats_are_displayed():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    # go to statsroyale.com
    driver.get('https://statsroyale.com/cards')

    # Assert Ice Spirit is displayed
    ice_spirit = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "[href*='Ice+Spirit']")))
    ice_spirit.click()

    card_name = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".card__cardName"))).text
    card_rarity = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".card__count"))).text
    card_info = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".card__rarity"))).text.split(', ')
    card_type = card_info[0]
    card_arena = card_info[1]

    assert card_name == 'Ice Spirit'
    assert card_rarity == 'Common'
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'

    driver.quit()


def test_lava_golem_card_is_displayed():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()

    golem_card = driver.find_element(By.CSS_SELECTOR, "[href*='Golem']")

    assert golem_card.is_displayed()

    driver.quit()
