def fizzbuzz_game(number):
    output = ""
    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    return output if output else str(number)