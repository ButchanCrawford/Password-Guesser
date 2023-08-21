# import random
game_on = True
code = ""
hint1 = ""
hint2 = ""
hint3 = ""
lives = 100
current_level = -1
failed_attempt = True


#user guesses code
def guess_code():
    guess_code = input("Enter Password: ")
    
    return guess_code

#validate guess against actual code
def validate_code(guess, actual):
    if guess == actual:
       print("Correct Code. Access Granted.")
    else:
        global lives
        lives -= 1
        print(f"Wrong Code. {lives} Tries Remaining.")
        
# run_lvl  functions changes the state of the password, owner and hint information
def run_lvl0():
    global code
    code = "password1"
    global hint1
    global hint2
    global hint3
    hint1 = "A common passsword for first time password setters."
    hint2 = "Letters: Y | Numbers: Y | Special Characters: N | Upper And Lower: N | Spaces: N"
    hint3 = "9 Characters"

    print("Name: Tim Brown \n DOB: 08/15/2010 \n Occupation: Learner \n")

def run_lvl1():
    global code
    global hint1
    global hint2
    global hint3
    code = "oprahWIN$1954"
    hint1 = "A combination of personal information with a slight twist."
    hint2 = "Letters: Y | Numbers: Y | Special Characters: Y | Upper And Lower: Y | Spaces: N"
    hint3 = "13 Characters"

    print("Name: Oprah Winfrey \n DOB: 01/29/1954 \n Occupation:Talk-show Host \n")

def run_lvl2():
    global code
    code = "BUTwaitTHEREisMORE!"
    global hint1
    global hint2
    global hint3
    hint1 = "Think a typical mprning infomercial slogan."
    hint2 = "Letters: Y | Numbers: N | Special Characters: Y | Upper And Lower: Y | Spaces: N"
    hint3 = "18 Characters"

    print("Name: Billey Mays \n DOB:6/20/1958 \n Occupation: Salesman \n")

#select the game stage / level
def level_selector():
    continue_play = input("Attempt to crack a password? Y or Yes to Continue, any other input to Stop. ").upper()
    global failed_attempt
    if  True == failed_attempt and continue_play == "Y" or continue_play == "YES":
        print(f"Level up \nfail attempt state {failed_attempt}")
        global current_level
        current_level += 1
    
    if current_level == 0:
        run_lvl0()
    elif current_level == 1:
        run_lvl1()
    elif current_level == 2:
        run_lvl2()
    else:
        global game_on
        game_on = False

def game_state():
    gaming = input("Play Again? Y or Yes to Continue, any other input to Stop.")
    if gaming == "Y" or "Yes":
        game_on = True
    else:
        game_on = False

def game():
    print(f"Welcome to Password Guesser \nYou have {lives} tries to guess the password.")
    
    while game_on:
        level_selector()
        guess = guess_code()
        validate_code(guess, code)
        if guess != code:
           global failed_attempt
           failed_attempt = False
           print("failed_attempt at password")
           
        else:
         failed_attempt = True
         level_selector()
        

if __name__ == "__main__":
    game()