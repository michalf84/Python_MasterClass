import random
import tkinter

def load_images(card_images):
    suits=["heart","club","diamond","spade"]
    face_cards=["jack","queen","king"]
    extension="png"
#     for each suit treive the image for the card
    for suit in suits:
#         first number is cards from 1 to 10
          for card in range(1,11):
              name="cards/{}_{}.{}".format(str(card),suit,extension)
              image=tkinter.PhotoImage(file=name)
              card_images.append((card,image,))
# next the face cards
          for card in face_cards:
              name="cards/{}_{}.{}".format(str(card),suit,extension)
              image=tkinter.PhotoImage(file=name)
              card_images.append((10,image,))

def _deal_card(frame):
    #pop the next car off teh top of the dec
    next_card=deck.pop(0) #grab from top not bottom
    # and add it to back of the pack
    deck.append(next_card)
    #add the image to a lavel and display the laberl
    tkinter.Label(frame,image=next_card[1],relief='raised').pack(side='left')
    #  now return face value
    return next_card

def score_hand(hand):
#     calculae total score of all cad in list
# only one ae can have the value 11 and this iwll be redusced toi 1 if the hand would bust
    score=0
    ace=False
    for next_card in hand:
        card_value=next_card[0]
        if card_value==1 and not ace:
            ace=True
            card_value=11
        score+=card_value
        if score>21 and ace:
            score-=10
            ace=False
    return score


# the below fucnion used as I cannot have in 'command' statement fucnion(values) as it assigns them not executes
def deal_dealer():
    dealer_score=score_hand(dealer_hand)
    while 0<dealer_score<17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score=score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score=score_hand(player_hand)
    if player_score>21:
        result_text.set("Dealer wins")
    elif dealer_score>21 or dealer_score<player_score:
        result_text.set("player winds")
    elif dealer_score>player_score:
        result_text.set("dealer wins")
    else:
        result_text.set("Draw")

def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score=score_hand(player_hand)

    players_score_label.set(player_score)
    if player_score>21:
        result_text.set("Dealer win")
#     global player_score
#     global player_ace
#     card_value= deal_card(player_card_frame)[0]
#     if card_value==1 and not player_ace:
#         player_ace=True
#         card_value=11
#     player_score+=card_value
# #     if we wouel beust check if thre is an ace and subractoct
#     if player_score>21 and player_ace:
#         player_score-=10
#         player_ace=False
#     players_score_label.set(player_score)
#     if player_score>21:
#         result_text.set("dealer winds")
#     print(locals())

def initial_deal():
    deal_player=()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player=()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
#     embeded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame=tkinter.Frame(card_frame,background="green")
    dealer_card_frame.grid(row=0,column=1,sticky='ew',rowspan=2)
#     embed frame to hold the card images
    player_card_frame.destroy()
    player_card_frame=tkinter.Frame(card_frame,background="green")
    player_card_frame.grid(row=2,column=1,sticky="ew",rowspan=2)

    result_text.set("")
# create the list of sotre the delare and player hands
    dealer_hand=[]
    player_hand=[]



def shuffle():
    random.shuffle(deck)

def play():
    initial_deal()

    mainWindow.mainloop()

mainWindow=tkinter.Tk()



# set up the screen and fares for the deale and player
mainWindow.title("black jack")
mainWindow.geometry("640x640")
mainWindow.configure(background="green")

result_text=tkinter.StringVar()
result=tkinter.Label(mainWindow,textvariable=result_text)
result.grid(row=0,column=0,columnspan=3)

card_frame=tkinter.Frame(mainWindow,relief="sunken",borderwidth=1,background="green")
card_frame.grid(row=1,column=0,sticky="ew",columnspan=3,rowspan=2)

dealer_score_label=tkinter.IntVar()
tkinter.Label(card_frame,text="Dealer",background="green",fg="white").grid(row=0,column=0)
tkinter.Label(card_frame,textvariable=dealer_score_label,background="green",fg="white").grid(row=1,column=0)
# embed framee hold the card images
dealer_card_frame=tkinter.Frame(card_frame,background="green")
dealer_card_frame.grid(row=0,column=1,sticky="ew",rowspan=2)

players_score_label=tkinter.IntVar()

tkinter.Label(card_frame,text="Player",background="green",fg="white").grid(row=2,column=0)
tkinter.Label(card_frame,textvariable=players_score_label,background="green",fg="white").grid(row=3,column=0)

# embedded frame to hold the card images
player_card_frame=tkinter.Frame(card_frame,background="green")
player_card_frame.grid(row=2,column=1,sticky="ew",rowspan=2)

button_frame=tkinter.Frame(mainWindow)
button_frame.grid(row=3,column=0,columnspan=3,sticky="w")

dealer_button=tkinter.Button(button_frame,text="dealer",command=deal_dealer)
dealer_button.grid(row=0,column=0)

player_button=tkinter.Button(button_frame,text="Player",command=deal_player)
player_button.grid(row=0,column=1)

new_game_button=tkinter.Button(button_frame,text="new game", command=new_game)
new_game_button.grid(row=0,column=2)

shuffle_button=tkinter.Button(button_frame,text="shuffle",command=shuffle)
shuffle_button.grid(row=0, column=3)

    # -------------------------
    # load cards
cards=[]
load_images(cards)
print(cards)
    # create a dnew dec of cards and shuffle them
deck=list(cards)
shuffle()

    # create the list of sotre the delare and player hands
dealer_hand=[]
player_hand=[]

# to call it from another program
if __name__=="__main__":
    play()
