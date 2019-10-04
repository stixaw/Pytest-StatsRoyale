from typing import List

import requests

from royale.models.card import Card


def get_all_cards() -> List[Card]:
    response = requests.get('https://statsroyale.com/api/cards')
    if response.ok:
        card_list = [Card(**card) for card in
                     response.json()]  # for card in response make new card by unpacking the card in the list
        return card_list
    else:
        raise Exception('Response was not ok. Status Code: ' + response.status_code)


def get_a_card(card_name: str) -> Card:
    cards = get_all_cards()
    card = next(card for card in cards if card.name == card_name)
    return card
