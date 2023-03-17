import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self) -> str:
        """
        Возвращает карту в виде строки
        """
        suit_icons = {"Spades": '\u2660', "Clubs": '\u2663', "Diamonds": '\u2666', "Hearts": '\u2665'}
        return f"{self.value}{suit_icons[self.suit]}"

    def equal_suit(self, other_card) -> bool:
        """
        Сравнивает масти двух карт
        """
        return self.suit == other_card.suit

    def more(self, other_card) -> bool:
        """
        Определяет старшую из двух карт по рангу и масти
        """

        value_volume = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                        '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        suit_value = {"Spades": 1, "Clubs": 2, "Diamonds": 3, "Hearts": 4}

        if value_volume[self.value] == value_volume[other_card.value]:
            return suit_value[self.suit] > suit_value[other_card.suit]
        else:
            return value_volume[self.value] > value_volume[other_card.value]

    def less(self, other_card):
        """
        Определяет младшую из двух карт по рангу и масти
        """
        return not self.more(other_card)


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self) -> str:
        """
        Возвращает колоду карт в виде строки
        """
        str_cards = []
        for card in self.cards:
            str_cards.append(card.to_str())

        return f"cards[{len(self.cards)}]: " + ", ".join(str_cards)

    def draw(self, number_of_cards: int) -> list:
        """
        Сдаёт определённое число карт на "руку"
        """

        hand, self.cards = self.cards[:number_of_cards], self.cards[number_of_cards:]

        return hand

    def shuffle(self) -> None:
        """
        Перемешивает колоду карт
        """
        return random.shuffle(self.cards)

    def shift(self, num_card: int) -> None:
        """
        Сдвигает определённое число карт сверху и перемещает вниз колоды
        """
        self.cards = self.cards[num_card:] + self.cards[:num_card]


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Сдвигаем 10 карт
deck.shift(2)
print(deck.show())
