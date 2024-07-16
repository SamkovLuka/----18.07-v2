import random


#1

#done

# def printNSK(a, b):
#     if b == 0:
#         return a
#     else:
#         return printNSK(b, a % b)
    

#2

#done

# def genNum():
#     return random.randint(1000, 9999)

# def counting(secret, guess):
#     secret_str = str(secret)
#     guess_str = str(guess)
#     bulls = sum(secret_str[i] == guess_str[i] for i in range(4))
    
#     secret_digits = [secret_str.count(digit) for digit in set(secret_str)]
#     guess_digits = [guess_str.count(digit) for digit in set(secret_str)]
#     cows = sum(min(secret_digits[i], guess_digits[i]) for i in range(len(secret_digits))) - bulls
    
#     return bulls, cows

# def game(secret, attempts=1):
#     guess = int(input("Введіть чотиризначне число -  "))
    
#     if guess == secret:
#         print(f"Ви вгадали число {secret} за {attempts} спроб.")
#         return
#     else:
#         bulls, cows = counting(secret, guess)
#         print(f"Бики: {bulls}, Корови: {cows}")
#         game(secret, attempts + 1)


# if __name__ == "__main__":
#     secret_number = genNum()
#     game(secret_number)


#3




#4

#done

# def generate_puzzle():
#     numbers = list(range(1, 16))
#     random.shuffle(numbers)
#     puzzle = [numbers[i:i+4] for i in range(0, 16, 4)]
#     return puzzle

# def print_puzzle(puzzle):
#     for row in puzzle:
#         print(row)

# def find_empty_position(puzzle):
#     for i in range(4):
#         for j in range(4):
#             if puzzle[i][j] == 15:
#                 return (i, j)

# def play_game():
#     puzzle = generate_puzzle()
#     empty_pos = find_empty_position(puzzle)
    
#     print("П'ятнашки")
#     print("Для переміщення цифр використовуйте WASD")
    
#     while True:
#         print_puzzle(puzzle)
#         move = input("Ваш хід: ").lower()
        
#         if move == 'W' and empty_pos[0] > 0:
#             puzzle[empty_pos[0]][empty_pos[1]], puzzle[empty_pos[0] - 1][empty_pos[1]] = \
#                 puzzle[empty_pos[0] - 1][empty_pos[1]], puzzle[empty_pos[0]][empty_pos[1]]
#             empty_pos = (empty_pos[0] - 1, empty_pos[1])
#         elif move == 'S' and empty_pos[0] < 3:
#             puzzle[empty_pos[0]][empty_pos[1]], puzzle[empty_pos[0] + 1][empty_pos[1]] = \
#                 puzzle[empty_pos[0] + 1][empty_pos[1]], puzzle[empty_pos[0]][empty_pos[1]]
#             empty_pos = (empty_pos[0] + 1, empty_pos[1])
#         elif move == 'A' and empty_pos[1] > 0:
#             puzzle[empty_pos[0]][empty_pos[1]], puzzle[empty_pos[0]][empty_pos[1] - 1] = \
#                 puzzle[empty_pos[0]][empty_pos[1] - 1], puzzle[empty_pos[0]][empty_pos[1]]
#             empty_pos = (empty_pos[0], empty_pos[1] - 1)
#         elif move == 'D' and empty_pos[1] < 3:
#             puzzle[empty_pos[0]][empty_pos[1]], puzzle[empty_pos[0]][empty_pos[1] + 1] = \
#                 puzzle[empty_pos[0]][empty_pos[1] + 1], puzzle[empty_pos[0]][empty_pos[1]]
#             empty_pos = (empty_pos[0], empty_pos[1] + 1)
#         elif move == 'exit':
#             print("gg")
#             break
#         else:
#             print("Неправильний ввід")

#         if check_win(puzzle):
#             print_puzzle(puzzle)
#             print("You win")
#             break

# def check_win(puzzle):
#     return puzzle == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]


# if __name__ == "__main__":
#     play_game()
