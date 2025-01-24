import random
 
def draw_card():
    card = random.randint(2, 14)
    return 11 if card == 14 else min(card, 10)
 
def hand_value(hand):
    value = sum(hand)
    return value - 10 if value > 21 and 11 in hand else value
 
def blackjack():
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card()]
 
    print(f"Din hand: {player_hand}, poäng: {hand_value(player_hand)}")
    while hand_value(player_hand) < 21 and input("Hit (h) eller Stand (s)? ") == 'h':
        player_hand.append(draw_card())
        print(f"Din hand: {player_hand}, poäng: {hand_value(player_hand)}")
       
    if hand_value(player_hand) > 21:
        print("Du blev tjock! Dealern vinner.")
        return
 
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card())
 
    print(f"Dealerns hand: {dealer_hand}, poäng: {hand_value(dealer_hand)}")
 
    if hand_value(dealer_hand) > 21 or hand_value(player_hand) > hand_value(dealer_hand):
        print("Du vinner!")
    elif hand_value(player_hand) < hand_value(dealer_hand):
        print("Dealern vinner!")
    else:
        print("Oavgjort!")
 
blackjack()