from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from royale.pages.cards_page import CardsPage
from royale.pages.card_details_page import CardDetailsPage


def test_ice_spirit_card_is_displayed():
    driver = webdriver.Chrome()
    url = 'https://statsroyale.com'
    driver.get(url)
    # How do I click escape key after the page loads so the test will move on before 5 minutes?
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
    # doesn't work!!!! I can manually hit escape and
    # the test moves on and passes

    # driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    # cards_page = CardsPage(driver)
    # cards_page.goto()
    cards_page = CardsPage(driver).goto()

    # Assertion
    # ice_spirit_card = driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
    ice_spirit_card = cards_page.get_card_by_name('Ice Spirit')

    # assert cards_page.map.ice_spirit_card.is_displayed()
    # assert cards_page.goto().map.ice_spirit_card.is_displayed()
    # assert cards_page.goto().get_card_by_name('Ice Spirit').is_displayed()
    assert ice_spirit_card.is_displayed()

    driver.quit()


def test_ice_spirit_stats_are_displayed():
    driver = webdriver.Chrome()
    url = 'https://statsroyale.com'
    driver.get(url)

    #  go to cards page
    #  got to Ice Spirit Details page
    # cards_page = CardsPage(driver).goto()
    # cards_page.get_card_by_name('Ice Spirit').click()
    CardsPage(driver).goto().get_card_by_name('Ice Spirit').click()

    # get card name, type, arena and rarity
    details_page = CardDetailsPage(driver)

    # card_name = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "[class*='cardName']"))).text
    # card_name = driver.find_element(By.CSS_SELECTOR, ".card__cardName").text
    card_name = details_page.map.card_name

    # split = driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']").text.split(', ')
    split = details_page.map.card_category
    # card_category = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".card__rarity"))).text.split(', ')
    card_type = split[0]
    card_arena = split[1]

    # card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*='rarityCaption']").text.split('\n')[1]
    # card_rarity = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".card__count"))).text
    card_rarity = details_page.map.card_rarity

    assert card_name == 'Ice Spirit'
    assert card_rarity == 'Common'
    assert card_type == 'Troop'
    assert card_arena == 'Arena 8'

    driver.quit()


def test_mirror_stats_are_displayed():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)
    driver.get('https://statsroyale.com')

    #  go to cards page
    #  got to Ice Spirit Details page
    cards_page = CardsPage(driver)
    cards_page.goto().get_card_by_name('Mirror').click()

    # get card name, type, arena and rarity
    details_page = CardDetailsPage(driver)
    card_name = details_page.map.card_name.text
    card_rarity = details_page.map.card_rarity.text
    card_type = details_page.map.card_category.text.split(', ')[0]
    card_arena = details_page.map.card_category.text.split(', ')[1]

    assert card_name == 'Mirror'
    assert card_rarity == 'Epic'
    assert card_type == 'Spell'
    assert card_arena == 'Arena 12'

    driver.quit()
