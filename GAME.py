print("Добро пожаловать в игру!")

field = list(range(1, 10))

def draw_field(field):
    print("-------------")
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("-------------")

def users_input(player):
    while True:
        player_answer = input("Ход игрока " + player + ":  ")
        if not (player_answer.isdigit()):
            print("Введите числа без пробелов.")
            continue
        player_answer = int(player_answer)
        if 1 <= player_answer <= 9:
            if str(field[player_answer - 1]) not in "XO":
                field[player_answer - 1] = player
            else:
                print("Это поле уже занято")
                continue
        else:
            print("Ошибка! Введите число от 1 до 9")
            continue
        break
    return player_answer


def check_win(field):
    count = 0
    while True:
        if count == 9:
            print("Ничья")
            break
        if count % 2 == 0:
            player = "X"
        else:
            player = "O"
        draw_field(field)
        UI = users_input(player)
        count += 1

check_win(field)