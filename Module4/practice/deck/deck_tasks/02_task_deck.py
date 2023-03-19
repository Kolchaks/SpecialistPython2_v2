from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
deck = Deck()
deck.shuffle()
print(deck)
hand = deck.draw(20)
print(*hand)

# TODO: посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
suits_count = {"Hearts": 0, "Diamonds": 0, "Clubs": 0, "Spades": 0}

for card in hand:
    for key in suits_count:
        if card.suit == key:
            suits_count[key] += 1

print(suits_count)
max_number_suits = max(suits_count.values())

for key, val in suits_count.items():
    if max_number_suits == suits_count[key]:
        print(f"{key}: {val}")
