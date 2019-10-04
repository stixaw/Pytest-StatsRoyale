import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from royale.pages.cards_page import CardsPage
from royale.pages.card_details_page import CardDetailsPage
from royale.services import card_service

cards = card_service.get_all_cards()

# 93 test cases with 1 method
@pytest.mark.parametrize('api_card', cards)
def test_card_is_displayed(api_card):
    driver = webdriver.Chrome()
    url = 'https://statsroyale.com'
    driver.get(url)

    # driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    # cards_page = CardsPage(driver)
    # cards_page.goto()
    cards_page = CardsPage(driver).goto()
    card_on_page = cards_page.get_card_by_name(api_card.name)

    # Assertion
    # ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    # ice_spirit_card = cards_page.get_card_by_name('Ice Spirit')

    # assert cards_page.map.ice_spirit_card.is_displayed()
    # assert cards_page.goto().map.ice_spirit_card.is_displayed()
    # assert cards_page.goto().get_card_by_name('Ice Spirit').is_displayed()
    assert card_on_page.is_displayed()

    driver.quit()

# 93 test cases with 1 method
@pytest.mark.parametrize('api_card', cards)
def test_card_stats_are_displayed(api_card):
    driver = webdriver.Chrome()
    driver.get('https://statsroyale.com')

    #  go to cards page
    #  got to Ice Spirit Details page
    # cards_page = CardsPage(driver)
    # cards_page.goto().get_card_by_name('Ice Spirit').click()

    cards_page = CardsPage(driver).goto()
    card_on_page = cards_page.get_card_by_name(api_card.name).click()

    # get card name, type, arena and rarity
    # details_page = CardDetailsPage(driver)
    # card_name = details_page.map.card_name
    # card_rarity = details_page.map.card_rarity
    # # card_info = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".card__rarity"))).text.split(', ')
    # card_type = details_page.map.card_type
    # card_arena = details_page.map.card_arena

    card = CardDetailsPage(driver).get_base_card()

    assert card.name == api_card.name
    assert card.rarity == api_card.rarity
    assert card.type == api_card.type
    assert card.arena == api_card.arena

    driver.quit()

# No longer needed as we only need two tests
# def test_mirror_stats_are_displayed():
#     driver = webdriver.Chrome()
#     driver.get('https://statsroyale.com')
#
#     #  go to cards page
#     #  got to Ice Spirit Details page
#     # cards_page = CardsPage(driver)
#     CardsPage(driver).goto().get_card_by_name('Mirror').click()
#
#     # get card name, type, arena and rarity
#     # details_page = CardDetailsPage(driver)
#     # card_name = details_page.map.card_name.text
#     # card_rarity = details_page.map.card_rarity.text
#     # # card_category = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".card__rarity"))).text.split(', ')
#     # card_type = details_page.map.card_category.text.split(', ')[0]
#     # card_arena = details_page.map.card_category.text.split(', ')[1]
#
#     card = CardDetailsPage(driver).get_base_card()
#
#     assert card.name == 'Mirror'
#     assert card.rarity == 'Epic'
#     assert card.type == 'Spell'
#     assert card.arena == 12
#
#     driver.quit()
