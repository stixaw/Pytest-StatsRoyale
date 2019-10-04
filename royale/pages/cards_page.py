from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from royale.models import card
from royale.pages.base.pagebase import PageBase
from royale.services import card_service


class CardsPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.map = CardsPageMap(driver)

    def goto(self):
        self.headernav.goto_cards_page()
        return self

    def get_card_by_name(self, card_name: str) -> WebElement:  # Ice Spirit => Ice+Spirit
        if ' ' in card_name:
            card_name = card_name.replace(' ', '+')
        return self.map.card(card_name)

    def get_card_name_by_id(self, card_id: int) -> WebElement:
        api_card = card_service.get_a_card_by_id(card_id)
        card.name = api_card.name
        return card.name


class CardsPageMap:
    def __init__(self, driver):
        self._driver = driver

    # @property
    # def ice_spirit_card(self):
    #     return self._driver.find_element(By.CSS_SELECTOR, "a[href*='Ice+Spirit']")

    def card(self, card_name) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, f"a[href*='{card_name}']")
