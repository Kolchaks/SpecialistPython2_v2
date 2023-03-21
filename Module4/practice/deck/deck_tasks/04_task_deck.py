from deck_total import Card, Deck

# TODO: Создайте две колоды, в каждой должно быть 36 карт(старшинство карт начинается с 6-ки). Перемешайте их.
#   Вытягивайте карты парами - одну из первой колоды, вторую из второй.
#   Если карта из первой колоды окажется больше(старше), то записываем 1:0(условно начисляем победное очко
#   первой колоде), если карты одинаковые, то не учитываем очко никуда.
#   Выведите итоговый счет, сравнив попарно все карты в колодах.

deck1 = Deck()
deck1.shuffle()

deck2 = Deck()

deck1.shuffle()
deck2.shuffle()
count_deck1 = 0
count_deck2 = 0

for i in range(len(deck1)):
    card1 = deck1.draw(1)
    card2 = deck2.draw(1)
    if card1 == card2:
        print('карты совпали')
    elif card1 > card2:
        count_deck1 += 1
    else:
        card1 < card2
        count_deck2 += 1

    print(*card1, *card2)
    print(f"счёт: {count_deck1}:{count_deck2}")


print(f"{count_deck1}:{count_deck2}")
