from z3 import *
import string
import time


def get_int_input_range(prompt, minimum, maximum):
    while True:
        try:
            result = int(input(prompt))
            if result in range(minimum, maximum + 1):
                return result
        except ValueError:
            pass

        print(f'Invalid input, please provide an integer between {minimum} and {maximum}.')


def get_bool_input(prompt):
    while True:
        result = input(prompt).strip().lower()
        if result in ["yes", "y", "true"]:
            return True
        elif result in ["no", "n", "false"]:
            return False

        print('Invalid input, please write only yes or no.')


def get_choice_input(prompt, choices):
    choices_lowercase = [choice.lower() for choice in choices]
    while True:
        result = input(prompt).strip()
        if result in choices:
            return result
        elif result.lower() in choices_lowercase:
            return choices[choices_lowercase.index(result.lower())]

        print(f'Invalid input, please choose only from {", ".join(choices)}.')


def start_game():
    print("Welcome to Mastermind Solver!")
    print()
    print("Please choose options for the game.")

    number_of_numbers_in_guess = get_int_input_range("How many numbers in guess: ", 1, 50)
    number_of_possible_numbers = get_int_input_range("How many different possible numbers: ", 1, 200)

    if number_of_possible_numbers < number_of_numbers_in_guess:
        numbers_can_repeat = True
    elif number_of_numbers_in_guess == 1:
        numbers_can_repeat = False
    else:
        numbers_can_repeat = get_bool_input("Can numbers repeat (yes or no): ")
    if (
        ((number_of_possible_numbers == 2) and (number_of_numbers_in_guess > 45))
        or ((number_of_possible_numbers == 3) and (number_of_numbers_in_guess > 25))
        or ((number_of_possible_numbers > 3) and (number_of_numbers_in_guess > 20))
        or ((number_of_possible_numbers > 50) and (number_of_numbers_in_guess > 15))
        or (number_of_numbers_in_guess > 100)
    ):
        print("Warning! This game might take a very long time to complete.")
    print()

    output_formats = ["a", "b"]
    output_formats_left = ["c", "d", "e"]
    output_format_mapping = {"a": "a", "b": "b"}
    print("Please choose format for guess output from the following:")
    print("(a) 01-02-03-04  08-09-10-11")
    print("(b) 00-01-02-03  08-09-10-11")
    if (number_of_possible_numbers >= 10) and (number_of_possible_numbers <= 35):
        output_formats.append(output_formats_left[0])
        output_format_mapping[output_formats_left[0]] = "c"
        print(f"({output_formats_left[0]}) 1-2-3-4  8-9-a-b")
        output_formats_left.pop(0)
    if (number_of_possible_numbers >= 11) and (number_of_possible_numbers <= 36):
        output_formats.append(output_formats_left[0])
        output_format_mapping[output_formats_left[0]] = "d"
        print(f"({output_formats_left[0]}) 0-1-2-3  8-9-a-b")
        output_formats_left.pop(0)
    if number_of_possible_numbers <= 26:
        output_formats.append(output_formats_left[0])
        output_format_mapping[output_formats_left[0]] = "e"
        print(f"({output_formats_left[0]}) a-b-c-d  h-i-j-k")

    output_format = get_choice_input(f"Input {", ".join(output_formats[:-1])} or {output_formats[-1]}: ", output_formats)
    output_format = output_format_mapping[output_format]

    if output_format == "a":
        guess_format = "numbers"
        start_from_one = True
    elif output_format == "b":
        guess_format = "numbers"
        start_from_one = False
    elif output_format == "c":
        guess_format = "hex"
        start_from_one = True
    elif output_format == "d":
        guess_format = "hex"
        start_from_one = False
    else:
        guess_format = "letters"
        start_from_one = False

    print()
    print("The game starts!")

    return {
        "numbers_can_repeat": numbers_can_repeat,
        "number_of_possible_numbers": number_of_possible_numbers,
        "number_of_numbers_in_guess": number_of_numbers_in_guess,
        "guess_format": guess_format,
        "start_from_one": start_from_one
    }


def count_in_list(value, array):
    expression = []
    for item in array:
        expression.append(If(item == value, 1, 0))
    return Sum(expression)


def solve(options, past_guesses_data=None, stats=None):
    start_time = time.perf_counter()
    if not past_guesses_data:
        past_guesses_data = []

    solver = Solver()
    result_numbers = []
    numbers_can_repeat = options["numbers_can_repeat"]
    number_of_possible_numbers = options["number_of_possible_numbers"]
    number_of_numbers_in_guess = options["number_of_numbers_in_guess"]

    for i in range(number_of_numbers_in_guess):
        result_numbers.append(Int(f'number_{i}'))

    for result_number in result_numbers:
        solver.add(result_number >= 0)
        solver.add(result_number < number_of_possible_numbers)

    if not numbers_can_repeat:
        solver.add(Distinct(result_numbers))

    for past_guess_data in past_guesses_data:
        past_numbers = past_guess_data["guess"]
        bulls_constraint = []
        cows_constraint = []

        for past_number, result_number in zip(past_numbers, result_numbers):
            bulls_constraint.append(If(past_number == result_number, 1, 0))

        for past_number in set(past_numbers):
            past_number_count = past_numbers.count(past_number)
            result_number_count = count_in_list(past_number, result_numbers)
            cows_constraint.append(If(past_number_count <= result_number_count, past_number_count, result_number_count))

        bulls_sum = Sum(bulls_constraint)
        cows_sum = Sum(cows_constraint) - bulls_sum

        solver.add(bulls_sum == past_guess_data["bulls"])
        solver.add(cows_sum == past_guess_data["cows"])

    if solver.check() == unsat:
        return False

    model = solver.model()

    ordered_numbers = []
    for result_number in result_numbers:
        ordered_numbers.append(model[result_number].as_long())

    if stats:
        stats["number_of_guesses"] = stats["number_of_guesses"] + 1
        stats["time_per_move"].append(time.perf_counter() - start_time)

    return ordered_numbers


def format_time(total_seconds):
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = total_seconds % 60

    time_parts = []

    if hours > 0:
        time_parts.append(f"{hours} hour{'s' if hours > 1 else ''}")

    if minutes > 0:
        time_parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")

    if (
        (len(time_parts) == 0)
        or (round(seconds) > 0)
        or ((round(seconds, 1) > 0) and (round(total_seconds, 1) < 10))
    ):
        if round(total_seconds, 1) < 10:
            time_parts.append(f"{seconds:.1f} seconds")
        else:
            time_parts.append(f"{round(seconds)} second{'s' if round(seconds) != 1 else ''}")

    if len(time_parts) == 1:
        return time_parts[0]
    elif len(time_parts) == 2:
        return f"{time_parts[0]} and {time_parts[1]}"
    else:
        return f"{time_parts[0]}, {time_parts[1]} and {time_parts[2]}"


def formated_guess(guess, options):
    start_from_one = options["start_from_one"]
    guess_format = options["guess_format"]
    number_of_possible_numbers = options["number_of_possible_numbers"]
    ascii_lowercase = string.ascii_lowercase

    if start_from_one:
        guess = [x + 1 for x in guess]

    if guess_format == "letters":
        guess = [ascii_lowercase[i] for i in guess]

    elif guess_format == "hex":
        guess = [ascii_lowercase[i - 10] if i >= 10 else str(i) for i in guess]

    else:
        if start_from_one:
            pad_length = len(str(number_of_possible_numbers))
        else:
            pad_length = len(str(number_of_possible_numbers - 1))
        guess = [str(i).zfill(pad_length) for i in guess]

    length = len(guess)

    possible_chunk_lengths = [4, 5, 3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

    chunk_length = length

    for possible_chunk_length in possible_chunk_lengths:
        if length % possible_chunk_length == 0:
            chunk_length = possible_chunk_length
            break

    chunks = [guess[i:i + chunk_length] for i in range(0, length, chunk_length)]

    result = ''
    for i, chunk in enumerate(chunks):
        chunk_string = '-'.join(chunk)

        if i > 0:
            result += '  '
        result += chunk_string

    return result


def get_guess_data_input(guess, options, past_guesses_data=None, stats=None):
    if not past_guesses_data:
        past_guesses_data = []

    number_of_numbers_in_guess = options["number_of_numbers_in_guess"]
    number_of_possible_numbers = options["number_of_possible_numbers"]
    numbers_can_repeat = options["numbers_can_repeat"]

    if stats:
        print(f"Found a valid guess {stats["number_of_guesses"]} in {format_time(stats["time_per_move"][-1])}.")
    print("Use guess:")
    print(formated_guess(guess, options))

    if numbers_can_repeat and (len(past_guesses_data) > 0):
        minimum_sum = past_guesses_data[-1]["bulls"] + past_guesses_data[-1]["cows"]
    else:
        minimum_sum = 0

    if not numbers_can_repeat:
        max_missing = number_of_possible_numbers - number_of_numbers_in_guess
    else:
        max_missing = number_of_numbers_in_guess

    if numbers_can_repeat or (number_of_numbers_in_guess == 1):
        only_bulls = True
    else:
        only_bulls = False

    for past_guess_data in past_guesses_data:
        if (past_guess_data["bulls"] > 0) or (past_guess_data["cows"] > 0):
            only_bulls = False
            break

    if only_bulls and (len(past_guesses_data) >= number_of_possible_numbers - 1):
        all_bulls = True
    else:
        all_bulls = False

    while True:
        if all_bulls:
            bulls = number_of_numbers_in_guess
            cows = 0
            print(f"Number of bulls: {number_of_numbers_in_guess}")
            print(f"Number of cows: 0")
            break
        else:
            bulls = get_int_input_range("Input number of bulls: ", 0, number_of_numbers_in_guess)

        if only_bulls:
            cows = 0
            print("Number of cows: 0")
            break
        elif (
            (
                (len(past_guesses_data) > 0)
                and (past_guesses_data[-1]["bulls"] + past_guesses_data[-1]["cows"] == number_of_numbers_in_guess)
            )
            or (len(past_guesses_data) >= number_of_possible_numbers - 1)
            or (max_missing == 0)
        ):
            cows = number_of_numbers_in_guess - bulls
            print(f"Number of cows: {cows}")
            break

        cows = get_int_input_range("Input number of cows: ", 0, number_of_numbers_in_guess)

        if bulls + cows < minimum_sum:
            print(f"Sum of bulls and cows must not be less than after previous guess ({minimum_sum}).")
            continue
        if bulls + cows > number_of_numbers_in_guess:
            print(f"Sum of bulls and cows must not be more than there are numbers in code ({number_of_numbers_in_guess}).")
            continue
        if bulls == number_of_numbers_in_guess - 1 and cows == 1:
            print(f"It is impossible that only one number is in wrong position.")
            continue
        if number_of_numbers_in_guess - bulls - cows > max_missing:
            print(f"No more than {max_missing} numbers can be missing.")
            continue

        break
    print()

    return {"guess": guess[:], "bulls": bulls, "cows": cows}


def play():
    options = start_game()
    stats = {"number_of_guesses": 0, "time_per_move": []}
    past_guesses_data = []

    while True:
        current_guess = solve(options, past_guesses_data, stats)
        if not current_guess:
            print("No valid solutions exist.")
            print("Did you make a mistake?")
            break
        guess_data = get_guess_data_input(current_guess, options, past_guesses_data, stats)
        past_guesses_data.append(guess_data)
        if guess_data["bulls"] == options["number_of_numbers_in_guess"]:
            print("Congratulations, game won!")
            print(f"Total guesses: {stats["number_of_guesses"]}. Processing time: {format_time(sum(stats["time_per_move"]))}.")
            break


if __name__ == "__main__":
    play()
