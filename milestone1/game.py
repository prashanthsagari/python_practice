def display_game(game_list):
    print(f'Here is the current List : {game_list}')

def postion_choice():
    choice = 'wrong'
    
    while choice not in range(0,3):
        try:
            choice = int(input("Pick a positin (0,1,2) : "))
        except:
            print('Only numbers are allowed')
            continue
        if choice not in range(0,3):
            print('Sorry, invalid choice! ')
    return choice

def replace_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice = 'wrong'
    
    while choice not in ['Y', 'N']:
        
        choice = input("Keep playing ? (Y or N) : ")

        if choice not in ['Y', 'N']:
            print('Sorry, invalid choice! ')
    return choice == 'Y'
        
game_list = [0,1,2]
game_on = True

while game_on:
    display_game(game_list)
    
    position = postion_choice()
    
    game_list = replace_choice(game_list, position)
    
    display_game(game_list)
    
    game_on = gameon_choice()

print('EXITED !!! ')
    