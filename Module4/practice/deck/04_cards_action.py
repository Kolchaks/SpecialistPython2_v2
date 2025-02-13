class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icons = {"Spades": '\u2660', "Clubs": '\u2663', "Diamonds": '\u2666', "Hearts": '\u2665'}
        return f"{self.value}{suit_icons[self.suit]}"

    def equal_suit(self, other_card) -> bool:
        return self.suit == other_card.suit


cards = []
str_cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

for suit in suits:
    for value in values:
        cards.append(Card(value, suit))


# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards

for card in cards:
    str_cards.append(card.to_str())

print(f"cards[{len(cards)}]: " + ", ".join(str_cards))
