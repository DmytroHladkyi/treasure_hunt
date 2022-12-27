from math import sqrt
from random import randint

# x = int(input("Podaj wymiar boiska."))
game_width = int(input("Podaj szerokość (X): "))
game_hight = int(input("Podaj wysokość (Y): "))

key_x = randint(0, game_width)
key_y = randint(0, game_hight)
player_x = randint(0, game_width)
player_y = randint(0, game_hight)
player_found_key = False
tries = 0

distance_befor = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
# print("pozycja skarbu", key_x,key_y)
print("pozycja gracza", player_x, "X",player_y, "Y")

while not player_found_key:
    tries += 1
    print()
    move = input("Udaj się w kierunku w którym chcesz (W/S/A/D)")

    match move.lower():
        case 'w':
            player_y += 1
            if player_y > game_hight:
                print("Wychodzisz poza pole.")
                player_y = game_hight
        case 's':
            player_y -= 1
            if player_y < 0:
                print("Wychodzisz poza pole.")
                player_y = 0
        case 'a':
            player_x -= 1
            if player_x < 0:
                print("Wychodzisz poza pole.")
                player_y = 0
        case 'd':
            player_x += 1
            if player_x > game_width:
                print("Wychodzisz poza pole.")
                player_x = game_width
        case 'q':
            print("Koniec zabawy.")
            quit()
        case '_':
            print("Nie wiem, gdzie cchesz iść.")
            continue
    if player_x == key_x and player_y == key_y:
        print("Bravo! Znalazłeść skarb!")
        print(f'Podjąłeś {tries} prób. Skarb znajdował się w {key_x}(X)/{key_y}(Y)')
        quit()
        
    distance_after = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_befor > distance_after:
        print("Cieplej.")
    else:
        print("Zimniej.")
    distance_befor = distance_after
    print(player_x,player_y)