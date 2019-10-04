import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from royale.pages.cards_page import CardsPage
from royale.pages.card_details_page import CardDetailsPage


def test_ice_spirit_stats_are_displayed():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')

    #  go to cards page
    #  got to Ice Spirit Details page
    # cards_page = CardsPage(driver)
    # cards_page.goto().get_card_by_name('Ice Spirit').click()

    CardsPage(driver).goto().get_card_by_name('Ice Spirit').click()

    # get card name, type, arena and rarity
    # details_page = CardDetailsPage(driver)
    # card_name = details_page.map.card_name
    # card_rarity = details_page.map.card_rarity
    # # card_info = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".card__rarity"))).text.split(', ')
    # card_type = details_page.map.card_type
    # card_arena = details_page.map.card_arena

    card = CardDetailsPage(driver).get_base_card()

    assert card.name == 'Ice Spirit'
    assert card.rarity == 'Common'
    assert card.type == 'Troop'
    assert card.arena == 8

    driver.quit()


def test_mirror_stats_are_displayed():
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')

    #  go to cards page
    #  got to Ice Spirit Details page
    # cards_page = CardsPage(driver)
    CardsPage(driver).goto().get_card_by_name('Mirror').click()

    # get card name, type, arena and rarity
    # details_page = CardDetailsPage(driver)
    # card_name = details_page.map.card_name.text
    # card_rarity = details_page.map.card_rarity.text
    # # card_category = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".card__rarity"))).text.split(', ')
    # card_type = details_page.map.card_category.text.split(', ')[0]
    # card_arena = details_page.map.card_category.text.split(', ')[1]

    card = CardDetailsPage(driver).get_base_card()

    assert card.name == 'Mirror'
    assert card.rarity == 'Epic'
    assert card.type == 'Spell'
    assert card.arena == 12

    driver.quit()
