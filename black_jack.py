# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
import random


def first_hit_deck(deck):
    cards = [random.choice(deck) for _ in range(2)]
    return cards


def hit_deck(deck):
    card = random.choice(deck)
    return card


if __name__ == '__main__':
    is_play_flag = True


    while is_play_flag:
        is_play = input('Do you want to play? (y/n): \n').lower()
        if is_play == 'n':
            is_play_flag = False
            break
        else:
            flag = True
            deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
            user_hand = first_hit_deck(deck)
            print(user_hand)
            computer_hand = first_hit_deck(deck)
            print(computer_hand[0])
            while flag:
                if sum(user_hand) <= 21:
                    i = input("Press 'y' for another hand and 'n' for pass: '\n")
                    if i == 'y':
                        new_card = hit_deck(deck)
                        user_hand.append(new_card)
                        if new_card == 11 and sum(user_hand) > 21:
                            user_hand.pop()
                            user_hand.append(1)
                        print(user_hand)
                        print('Total: ', sum(user_hand))
                        continue
                    else:
                        print(computer_hand)
                        if sum(user_hand) == sum(computer_hand):
                            print("Drawn!")
                            print("User Hand", user_hand)
                            print("Computer Hand", computer_hand)
                            flag = False
                            break

                        if 17 <= sum(computer_hand) <= 21 and sum(computer_hand) > sum(user_hand):
                            print("Computer Won")
                            print(computer_hand)
                            print('Total: ', sum(computer_hand))
                            flag = False
                            break
                        while sum(computer_hand) < 17:
                            new_card = hit_deck(deck)
                            computer_hand.append(new_card)
                            if new_card == 11 and sum(computer_hand) > 21:
                                computer_hand.pop()
                                computer_hand.append(1)
                            print(computer_hand)
                            if (sum(computer_hand) > 21) or 17 <= sum(computer_hand) <= 21 and sum(computer_hand) < sum(user_hand):
                                print("User Won")
                                print(user_hand)
                                print('Total: ', sum(user_hand))
                                flag = False
                                break
                            elif 17 <= sum(computer_hand) <= 21 and sum(computer_hand) > sum(user_hand):
                                print("Computer Won")
                                print(computer_hand)
                                print('Total: ', sum(computer_hand))
                                flag = False
                                break
                        else:
                            print("User Won ", user_hand)
                            print('Total: ', sum(user_hand))
                            print("Computer Busted", computer_hand)
                            flag = False

                else:
                    print("User Busted ", user_hand)
                    print("Computer Won ", computer_hand)
                    print('Total: ', sum(computer_hand))
                    flag = False
