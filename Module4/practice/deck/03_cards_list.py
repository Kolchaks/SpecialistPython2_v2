class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icons = {"Spades": '\u2660', "Clubs": '\u2663', "Diamonds": '\u2666', "Hearts": '\u2665'}
        return f"{self.value}{suit_icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
hearts_cards = []

for value in values:
    hearts_cards.append(Card(value, "Hearts"))

# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards = []
reversed_values = reversed(values)

for value in reversed_values:
    diamonds_cards.append(Card(value, "Diamonds"))

# TODO-3: выведите все карты из списка hearts_cards и diamonds_cards  в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
[print(card.to_str(), end=', ') for card in hearts_cards]
print()
[print(card.to_str(), end=', ') for card in diamonds_cards]
