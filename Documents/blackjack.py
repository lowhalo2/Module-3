from random import randint

class hand():
    ''' Creates a player hand and stores their cards drawn and the total value held.
        checks after first two drawn for blackjack bust or push.
        hit() removes a random card from the deck and calls addToHand().
        addToHand() takes the card drawn from held and adds a card to hand.
        stand() checks to see if the dealer is under the value of 17 if so he draws untill over 16 or bust then displayes the results.
        check() runs after every hit() to see if anyone busted pushed or won'''
    def __init__(self):
        self.hand = {'line1': '',
                     'line2': '',
                     'line3': '',
                     'line4': '',
                     'line5': ''}
        self.held = []
        self.value = 0
        self.cards = []
    
    def blackjack(self):
        if player.value == 21 and dealer.value == 21:
            print("\n\nIt's a Push no one wins")
            return True
        elif player.value == 21:
            print('\n\nPlayer blackjack! You win!')
            return True
        elif dealer.value == 21:
            print('\n\nDealer Blackjack! You lose!')
            return True
        elif player.value > 21:
            print('\n\nBreak! Your lose!')
            return True
        elif dealer.value > 21:
            print('\n\nDealer Break! You win!')
            return True
        else: 
            pass
    
    def hit(self):
        index = randint(0, len(deck) - 1)
        self.held = deck[index]
        deck.remove(self.held)
        self.cards.append(self.held)
        self.addToHand()

    def addToHand(self):
        suit = self.held[0]
        temp_count = int(self.held[1:])
        if temp_count <=9:
            count = str(temp_count) + ' '
        else:
            count = str(temp_count)
        self.hand['line1'] += f'  ╔══════╗'
        self.hand['line2'] += f'  ║ {suit}    ║'
        self.hand['line3'] += f'  ║  {count}  ║'
        self.hand['line4'] += f'  ║    {suit} ║'
        self.hand['line5'] += f'  ╚══════╝'
        if self.value != 0:
            print(' Players Hand ')
            for x in self.hand:
                print(self.hand[x])
        else:
            pass
        self.value += temp_count

    def stand(self):
        x = False
        while dealer.value < 17:
            dealer.hit()
            x = dealer.check()
        if x == True:
            return True
        elif self.value == dealer.value:
            print("\n\nIt's a push!")
            return True
        elif self.value > dealer.value:
            print(f'\n\nYou win with a value of {self.value}!')
            return True
        elif dealer.value > self.value:
            print(f"\n\nYou lose with a value of {self.value}!")
            return True
        

    def check(self):
        if self.value > 21:
            print(f'\n\nBust! You hit a total of {self.value}! Better luck next time.')
            return True
        elif self.value == 21 and dealer.value == 21:
            print(f"\n\nYou both hit 21 it's a push")
            return True
        elif self.value == 21:
            print(f'\n\nYou hit a {self.value}! You Win!')
            return True
    
    def showHand(self):
        print(' Players Hand ')
        for x in self.hand:
            print(self.hand[x])


class house(hand):
    '''Creates the dealers hand and reuses some of the Hand class functions.
       addToHand() adds any card from held to hand and value but only print the first card to the player.
       check() checks for a bust push or win.
       showHand() shows the dealers hand entirly at the end of the game.'''
    def __init__(self):
        self.value = 0
        self.cards = []
        self.hand = {'line1': '',
                     'line2': '',
                     'line3': '',
                     'line4': '',
                     'line5': ''}

    def addToHand(self):
        if self.hand['line1'] == '':  
            suit = self.held[0]
            temp_count = int(self.held[1:])
            if temp_count <=9:
                count = str(temp_count) + ' '
            else:
                count = str(temp_count)
        else:
            temp_count = int(self.held[1:])
            count = int(self.held[1:])
            suit = '?'
            count = '??'
        self.hand['line1'] += f'  ╔══════╗'
        self.hand['line2'] += f'  ║ {suit}    ║'
        self.hand['line3'] += f'  ║  {count}  ║'
        self.hand['line4'] += f'  ║    {suit} ║'
        self.hand['line5'] += f'  ╚══════╝'
        if self.value != 0:
            print(' Dealers Hand ')
            for x in self.hand:
                print(self.hand[x])
        else:
            pass
        self.value += int(temp_count)

    def check(self):
        if self.value > 21:
            print(f'\n\nBust! Dealer hit a total of {self.value}! You win!')
            return True
        elif self.value == 21 and dealer.value == 21:
            print(f"\n\nYou both hit 21 it's a push")
            return True
        elif self.value == 21:
            print(f'\n\nDealer hit a {self.value}! You lose!')
            return True
        
    def showHand(self):
        self.hand = {'line1': '',
                     'line2': '',
                     'line3': '',
                     'line4': '',
                     'line5': ''}
        print(' Dealers Hand ')
        for x in self.cards:
            y = x[1:]
            if int(y) < 10:
                y = f'{y} '
            self.hand['line1'] += f'  ╔══════╗'
            self.hand['line2'] += f'  ║ {x[0]}    ║'
            self.hand['line3'] += f'  ║  {y}  ║'
            self.hand['line4'] += f'  ║    {x[0]} ║'
            self.hand['line5'] += f'  ╚══════╝'
        for x in self.hand:
            print(self.hand[x])

# The deck of 52 cards with [0] as the suite and [1:] and the card value
deck = ['♠1','♠2','♠3','♠4','♠5','♠6','♠7','♠8','♠9','♠10','♠11','♠12',
        '♣1','♣2','♣3','♣4','♣5','♣6','♣7','♣8','♣9','♣10','♣11','♣12',
        '♥1','♥2','♥3','♥4','♥5','♥6','♥7','♥8','♥9','♥10','♥11','♥12',
        '♦1','♦2','♦3','♦4','♦5','♦6','♦7','♦8','♦9','♦10','♦11','♦12',]

player = hand()
dealer = house()
winner = False
while winner != True:
    if player.value == 0:
        # Start of the game and checks for a blackjack push or break
        print("Ready to start a game of BlackJack?")
        print(input('Press enter to start.'))
        player.hit()
        player.hit()
        dealer.hit()
        dealer.hit()
        x =  player.blackjack()
        if x == True:
            winner = True
            break
    else:
        action = input('hit or stand:  ')
        # Hit will make player hit but dealer will only hit if value under 17
        if action.lower() == 'hit':
            player.hit()
            x = player.check()
            if x == True:
                    winner = True
                    break
            if dealer.value >= 17:
                print(' Dealers Hand ')
                for x in dealer.hand:
                    print(dealer.hand[x])
                print(dealer.cards)
            else:
                dealer.hit()
                x = dealer.check()
                if x == True:
                    winner = True
                    break
        # Stand will end your hits but dealer will continue to hit untill value over 16
        elif action.lower() == 'stand':
            x = player.stand()
            if x == True:
                winner = True
                break
# Prints both plays hand for the last visual to show that the house didn't lie
# Visuals are pretty intense in this game make sure you have at least a 4090 Ti before playing
player.showHand()
dealer.showHand()
print('See You later!')