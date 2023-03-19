import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self) -> str:
        suit_icons = {"Spades": '\u2660', "Clubs": '\u2663', "Diamonds": '\u2666', "Hearts": '\u2665'}
        return f"{self.value}{suit_icons[self.suit]}"

    def equal_suit(self, other_card) -> bool:
        """
        Сравнивает масти двух карт
        """
        return self.suit == other_card.suit

    def __gt__(self, other_card) -> bool:  # gt -> great than

        value_volume = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                        '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        suit_value = {"Spades": 1, "Clubs": 2, "Diamonds": 3, "Hearts": 4}

        if value_volume[self.value] == value_volume[other_card.value]:
            return suit_value[self.suit] > suit_value[other_card.suit]
        else:
            return value_volume[self.value] > value_volume[other_card.value]

    def __lt__(self, other_card):  # lt -> less than
        return not self.__gt__(other_card)


class Deck:
    SPADES = "Spades"
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds"
    HEARTS = "Hearts"

    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def __str__(self) -> str:
        str_cards = []
        for card in self.cards:
            str_cards.append(str(card))

        return f"cards[{len(self.cards)}]: " + ", ".join(str_cards)

    def draw(self, number_of_cards: int) -> list:
        """
        Сдаёт определённое число карт на "руку"
        """
        hand, self.cards = self.cards[:number_of_cards], self.cards[number_of_cards:]
        return hand


    def __getitem__(self, index):
        return self.cards[index]


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


if __name__ == "__main__":
    card_1 = Card(10, Deck.DIAMONDS)
    card_2 = Card("Q", Deck.HEARTS)
    print(card_1, card_2, 'Привет!')

# if __name__ == "__main__":
    # Тут можно разместить тесты классов
    ...
