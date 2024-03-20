import simplegui
import random

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

in_play = False
outcome = ""
score = 0

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

class Hand:
    def __init__(self):
        self.cards=[]

    def __str__(self):
        self.cards=[]
        
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value=0
        ace=False
                     
        for card in self.cards:
            rank=card.get_rank()
            value+=VALUES[rank]
            
            if(rank=='A'):
                 ace=True
                    
        if (value<11 and ace):
            value+=1
        
        return value
    
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas,pos)
            pos[0]+=80 
        
class Deck:
    def __init__(self):
        self.cards=[]
        
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)
    
    def __str__(self):
        self.cards=[]
       
def deal():
    global outcome, in_play,score,deck,player_hand,dealer_hand
    if in_play==True:
        score-=1
        outcome="Re-deal.Score-1"
    else:
        outcome="Hit or Stand ?"
        player_hand=Hand()
        dealer_hand=Hand()
        deck=Deck()
        deck.shuffle()
        i=0
                
        while i<2:
            player_hand.add_card(deck.deal_card())
            dealer_hand.add_card(deck.deal_card()) 
            i+=1

        in_play = True

def hit():
    global outcome,in_play,socre
    if in_play:
        outcome="Hit or Stand ?"
        if player_hand.get_value()<=21:
            player_hand.add_card(deck.deal_card())
        if player_hand.get_value()>21:
            global score
            outcome="Busted!t=Try again?"
            score-=1
            in_play=False 
       
def stand():
    global outcome,in_play
    if in_play:
        outcome="Hit or Stand ?"
        while dealer_hand.get_value()<17:
            dealer_hand.add_card(deck.deal_card())
            
        if dealer_hand.get_value()>21:
            global score
            score+=1
            outcome="Dealer Busted.You wins."   
            in_play=False
        else:
            if dealer_hand.get_value()>=player_hand.get_value():
                 score-=1
                 outcome="Dealer wins"
                 in_play=False
            else:
                 score+=1
                 outcome="You wins"
                 in_play=False
 
def draw(canvas):
    canvas.draw_text("BlackJack",[150,100],80,"Black")
    canvas.draw_text(str(outcome),[210,150],30,"Black")
    canvas.draw_text("Dealer",[50,200],40,"White")
    canvas.draw_text("Your",[50,400],40,"White")
    canvas.draw_text("Score:"+str(score),[450,550],30,"Black")
    
    player_hand.draw(canvas,[100,420])
    dealer_hand.draw(canvas,[100,220])
    
    if in_play:
        canvas.draw_image(card_back,CARD_CENTER,CARD_SIZE,(136,268),CARD_SIZE)
    
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

deal()
frame.start()


