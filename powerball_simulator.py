from random import choice

def get_winning_ticket(possibilities, power):
    winning_ticket = []

    while len(winning_ticket) < 5:
        pulled_item = choice(possibilities)
        pulled_power = choice(power)


        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)
        winning_ticket.append(pulled_power)

    return winning_ticket


def get_my_ticket(possibilities, power):
    my_ticket = []

    while len(my_ticket) < 5:
        pulled_item = choice(possibilities)
        pulled_power = choice(power)


        if pulled_item not in my_ticket:
            my_ticket.append(pulled_item)
        my_ticket.append(pulled_power)

    return my_ticket


def check_ticket(mine, winner):
    mine_power = []

    pulled_mine_power = mine.pop()
    mine_power.append(pulled_mine_power)

    for element in mine:
        if element not in winner:
            return False

    for powerball in mine_power:
        if powerball not in winner_power:
            return False

    return True


possibilities = [x for x in range(1, 69)]
power = [x for x in range(1, 26)]

winner = get_winning_ticket(possibilities, power)
winner_power = []
pulled_winner_power = winner.pop()
winner_power.append(pulled_winner_power)

plays = 0
won = False

max_attempts = 1_000_000

while not won:
    mine = get_my_ticket(possibilities, power)
    won = check_ticket(mine[:], winner)

    mine_power = []
    pulled_mine_power = mine.pop()
    mine_power.append(pulled_mine_power)

    plays += 1

    if plays >= max_attempts:
        print("Reached max attempts...")
        break

    if won:
        print("WINNER!!!!")
        print(f"Your ticket: {mine}:{mine_power}")
        print(f"Winning ticket: {winner}:{winner_power}")
        print(f"It took {plays} tries.")
    else:
        print(f"Your ticket: {mine}:{mine_power}")
        print(f"Winning ticket: {winner}:{winner_power}")