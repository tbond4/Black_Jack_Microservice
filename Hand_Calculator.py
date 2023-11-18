import time


def main():
    write_score(calculate_score(read_hand()))

def read_hand():
    """Reads hand.txt file and creates hand list"""

    with open('hand.txt', 'r') as f:
        hand = f.readline().split(',')
    return hand

def calculate_score(hand):
    """Takes in hand[] and returns hand calulated score"""

    score = 0
    num_aces = 0

    # Moves Aces to the end of the array
    while 'A' in hand:
        num_aces +=1
        hand.remove('A')

    while num_aces > 0:
        hand.append('A')
        num_aces -= 1

    # Iterate through hand adding to score
    for card in hand:
        if card == 'J' or card == 'K' or card == 'Q':
            score += 10
        elif card == 'A' and score + 11 <= 21:
            score += 11
        elif card == 'A' and score + 11 >= 21:
            score += 1
        elif 2 <= int(card) <= 9:
            score += int(card)
        else:
            score = "Invalid Hand"
    return score

def  write_score(score):
    """Writes the hand score to hand_score.txt file"""

    with open('hand_score.txt', 'w') as f:
        f.write(str(score))
    

while True:
   write_score(calculate_score(read_hand()))
   time.sleep(1)
