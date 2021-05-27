# GLOBAL VARIABLES

import random
suits = ('Suits', 'Diamonds', 'Clubs', 'Diabmonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Joker', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'King':10, 'Queen':10, 'Joker':10, 'Ace':10}

playing = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        
        return (f'{self.rank} of {self.suit}')

class Deck():
    
    def __init__(self):
        
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # BUILDING A CARD OBJECTS AND ADDING TO THE LIST
    
    def __str__(self):
        
        pack = ''
        for card in self.deck:
            pack += '\n' + card.__str__()   # ADD EACH CARD OBJECT PRINT STRING TO PACK
        return (f'The Deck has: {pack}')
    
    def shuffle(self):
         random.shuffle(self.deck)
    
    def deal(self):
        
        single_card = self.deck.pop()
        return single_card


# TO CALCULATE THE VALUE OF THE CARDS

class Hand():
    
    def __init__(self):
        
        self.card_in_hand = []
        self.value = 0
        self.ace = 0
    
    def add_card(self, card):
        
        self.card_in_hand.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.ace += 1
    
    def adjust_for_ace(self):
        
        while self.value > 21 and self.ace:
            
            self.value -= 10
            self.ace -= 1
    

# TO ASSIGN TOTAT CHIPS AND BET AMOUNT

class chips():
    
    def __init__(self, total= 2000):
        
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        
        self.total += self.bet
    
    def lose_bet(self):
        
        self.total -= self.bet


# Func FOR TAKING BET FROM PLAYER

def place_bet(chips):
    
    while True:
        
        try:
            
            print("Chips available with you is: ", chips.total)
            chips.bet = int(input('Please enter the chips you want to bet: '))
            
        except ValueError:
            
            print('A bet must be and Interger')
    
        else:
            
            if chips.bet > chips.total:
                print('Sorry!!! you cannot bet more than what you have. Your bet cannot exceed', chips.total)
            else:

                break


# FUNC FOR HIT FOR PLAYED OR DEALER

def hit(deck, hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# FUNC FOR TAKING FRESH HIT (BET) OR STAND FROM PLAYER.

def hit_or_stand(deck, hand):
    
    global playing  
    
    while playing:
        
        place = input('Would you like to hit of stand? (h or s): ')
        
        if place[0].lower() == 'h':
            
            hit(deck, hand)
        
        elif place[0].lower() == 's':
            
            print('Player stand. Dealer Hit!!!')
            playing = False
        
        else:
            
            print('Sorry!!! please try again')
            continue
        
        break    


# FUNCTIONS FOR SHOWING CARDS. PLAYER: ALL CARDS AND DEALER: ONE CARD AND ANOTHER WILL BE HIDDEN

def show_some(player, dealer):
    
    print("\n Dealer's hand" + "< Card Hidden >" + dealer.card_in_hand[1].__str__())
    print("\n Player's hand", *player.card_in_hand, sep= '\n')
    print("Player's Hand value", player.value, sep= '\n')

def show_all(player,dealer):
    
    print("\n Dealer's Hand", *dealer.card_in_hand, sep= '\n')
    print("Dealer Hand Value", dealer.value, sep= '\n')
    print("Player's Hand", *player.card_in_hand, sep= '\n')
    print("Player's Hand value", player.value, sep= '\n')


# FUNCTION TO DECIDE THE GAME RESULT

def player_bust(player, dealer, chips):
    
    print("Player BUST!!!")
    chips.lose_bet()

def player_win(player, dealer, chips):
    
    print("Player WINS!!!")
    chips.win_bet()

def dealer_bust(player, dealer, chips):
    
    print("Dealer BUST!!!")
    chips.win_bet()

def dealer_win(player, dealer, chips):
    
    print("Dealer WINS!!!")
    chips.lose_bet()

def push(player, dealer, chips):
    
    print("The hand is Tied, It is a PUSH!!!")


player_chips=  chips()
while True:
    
    print("Welcome to Blackjack!!! Get as close to 21 as you can without going over 21!! \nDealer hit untill He/She reaches 17. Aces will count as 1 or 11")
    
    deck = Deck()
    deck.shuffle()
    
    player1_hand = Hand()
    player1_hand.add_card(deck.deal())
    player1_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    
    
    place_bet(player_chips)
    
    show_some(player1_hand, dealer_hand)
    
    while playing:
        
        hit_or_stand(deck, player1_hand)
        show_some(player1_hand, dealer_hand)
        
        if player1_hand.value > 21:
            player_bust(player1_hand, dealer_hand, player_chips)
            break
    
    if player1_hand.value <= 21:
        
        while dealer_hand.value < 17:
            
            hit(deck, dealer_hand)
        
        show_all(player1_hand, dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_bust(player1_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value > player1_hand.value:
            dealer_win(player1_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value < player1_hand.value:
            player_win(player1_hand, dealer_hand, player_chips)
        
        else:
            push(player1_hand, dealer_hand, player_chips)
    
    print("\n Player's Winnings stands at: ", player_chips.total)
    
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower() == 'y' and player_chips.total != 0:
        playing = True
        continue
    else:
        print(f"Thanks for playing!!! Your payout is: {player_chips.total}")
        break
            
        
            
