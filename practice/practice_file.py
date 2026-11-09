def sum_hand(hand):
    sum = 0
    for card in hand:
        rank = card["rank"]
        if rank > 10:
            rank = 10
        sum += rank
    return sum