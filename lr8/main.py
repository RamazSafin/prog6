import random

def guess_the_number():
    """
    Основная функция игры "Угадай число".

    В этой функции происходит основной цикл игры, включая генерацию случайного числа,
    обработку попыток пользователя, предоставление подсказок и возможность повторной игры.
    """
    print("Добро пожаловать в игру 'Угадай число'!")
    
    best_score = None
    
    while True:
        try:
            min_number = int(input("Введите минимальное число диапазона: "))
            max_number = int(input("Введите максимальное число диапазона: "))
            
            if min_number >= max_number:
                print("Минимальное число должно быть меньше максимального. Попробуйте снова.")
                continue

            number_to_guess = random.randint(min_number, max_number)
            number_of_attempts = 0
            guessed = False

            print(f"Я загадал число от {min_number} до {max_number}. Попробуй угадать его.")

            while not guessed:
                guess = input("Введи свое предположение: ")

                try:
                    guess = int(guess)
                    number_of_attempts += 1

                    if guess < number_to_guess:
                        print("Мое число больше.")
                    elif guess > number_to_guess:
                        print("Мое число меньше.")
                    else:
                        guessed = True
                        print(f"Поздравляю! Ты угадал число {number_to_guess} с {number_of_attempts} попытки!")
                        if best_score is None or number_of_attempts < best_score:
                            best_score = number_of_attempts
                            print(f"Это твой лучший результат!")
                except ValueError:
                    print("Пожалуйста, введи целое число.")
            
            print(f"Лучший результат: {best_score} попыток.")
            
            play_again = input("Хочешь сыграть еще раз? (да/нет): ").lower()
            if play_again != 'да':
                print("Спасибо за игру! До свидания!")
                break
        except ValueError:
            print("Пожалуйста, введи корректное целое число.")

if __name__ == "__main__":
    guess_the_number()
