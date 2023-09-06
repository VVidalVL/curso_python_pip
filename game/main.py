import random

def elejir_opcion():

    option = ("piedra","papel","tijera")
    user_option= input("piedra, papel o tijera > ")
    user_option=user_option.lower() #para que no altere si se escribe en mayuscula o minuscula
    

    if not user_option in option:
        print("opcion incorrecta")
        #continue
        return None, None
    
    computer_option = random.choice(option)

    print("User_option -> ", user_option)
    print("Computer_option -> ", computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Empate")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana a tijera")
            print("User gano!!!")
            user_wins +=1
        else:
            print("papel gana a piedra")
            print("computer gano")  
            computer_wins +=1  
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra")
            print("User gano!!!")
            user_wins +=1
        else:
            print("tijera gana a papel")
            print("computer gano")
            computer_wins +=1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("User gano!!!")
            user_wins +=1
        else:
            print("piedra gana a tijera")
            print("computer gano")
            computer_wins +=1
    return user_wins, computer_wins   

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        
        print("*"*10)
        print("Rounds", rounds)
        print("*"*10)
        print("Computer wins > ", computer_wins)
        print("User wins > ", user_wins)
        rounds +=1

        user_option, computer_option = elejir_opcion()
        user_wins, computer_wins = check_rules(user_option,computer_option, user_wins, computer_wins)

        if user_wins ==2:
            print("USER WINS!!!!!!")
            break
        if computer_wins==2:
            print("COMPUTER WINS!!!!!!")
            break
        
run_game()