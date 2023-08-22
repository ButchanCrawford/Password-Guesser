# import random
game_on = True
code = ""
lives = 100
current_level = -1
successful_attempt = True


#user guesses code
def guess_code():
    guess_code = input("Enter Password: ")
    return guess_code

#validate guess against actual code
def validate_code(guess, actual):
    if guess == actual:
       print("*****Correct Code. Access Granted.*****")
    else:
        global lives
        lives -= 1
        print(f"Wrong Code. {lives} Tries Remaining.")
        
# run_lvl  functions changes the state of the password and prints user info
def run_lvl0():
    global code
    code = "password1"
    code = "1"
    print("///--Name: Tim Brown--///\n///--DOB: 08/15/2010--///\n///--Occupation: Learner--///\n")

def run_lvl1():
    global code
    code = "oprahWIN$1954"
    code = "1"
    print("///--Name: Oprah Winfrey--///\n///--DOB: 01/29/1954--///\n///--Occupation:Talk-show Host--///\n")

def run_lvl2():
    global code
    code = "BUTwaitTHEREisMORE!"
    code = "1"
    print("///--Name: Billy Mays--///\n///--DOB:6/20/1958--///\n///--Occupation: Salesman--///\n")

#changes game level and game on state
def play_again():
    continue_play = input("Attempt to crack a password? Y or Yes to Continue, any other input to Stop. ").upper()
    global successful_attempt
    if  True == successful_attempt and continue_play == "Y" or continue_play == "YES":
        global current_level
        current_level += 1
    elif False == successful_attempt and continue_play == "Y" or continue_play == "YES":
        print("Try Again") 
    elif continue_play != "Y" or continue_play != "YES":
        print("Password Guesser Stopped Running")
        global game_on
        game_on = False

#select the game stage / level
def level_selector():
    global game_on
    if current_level == 0 and game_on == True:
        run_lvl0()
    elif current_level == 1 and game_on == True:
        run_lvl1()
    elif current_level == 2 and game_on == True:
        run_lvl2()
    elif current_level > 2: 
        game_on = False
        print("*****All Levels Completed. Congrats!!*****")

#runs the game
def game():
    print("//////////////////////////////////////////////////////")
    print(f"/////     Welcome to Password Guesser - Hard    /////\n///// You have {lives} tries to guess the password. /////")
    print("///// Spaces: N  | Special Character: Y Max of 1 ////")
    print("///// Numbers: Y | Case Sensitivity Y:          ////")
    print("////////////////////////////////////////////////////")


    global game_on
    global successful_attempt
    while game_on:
        if lives < 1:
            print("++You Have Ran Out Of Tries.++")
            print("!!! System Locked !!!")
            break
        if successful_attempt == True:
           play_again()
           
        if game_on:
           level_selector()
           guess = guess_code()
           validate_code(guess, code)
        if guess != code:
           successful_attempt = False
           print("Failed Attempt At Password") 
        elif guess == code and current_level >= 2:
            game_on = False
            print("*****All Levels Completed. Congrats!!*****")
        else:
         successful_attempt = True
       
if __name__ == "__main__":
    game()