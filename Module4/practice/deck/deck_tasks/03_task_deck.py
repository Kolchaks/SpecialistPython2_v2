from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните одну карту сверху.
#   Снова перемешайте колоду и вытяните еще одну. Если вторая карта меньше первой, повторите “перемешать + вытянуть”,
#   до тех пор, пока не вытяните карту больше предыдущей карты.
#   В качестве результата выведите все вытягиваемые карты в консоль.

deck = Deck()
deck.shuffle()
card_1 = deck.draw(1)
# card_1 = Card("A", Deck.HEARTS)

if card_1 != ("A", Deck.HEARTS):
    for i in range(len(deck)):
        deck.shuffle()
        card_2 = deck.draw(1)
        if card_1 < card_2:
            print(*card_1, *card_2)
            break
        else:
            print(*card_1, *card_2)
else:
    print(f"В колоде нет карты старше чем: {card_1}")
