#input an integer
#square its digits and find the sum of squares
#continue with this number
#repeat until either answer is 1 -> happy
#or until you get trapped in a cycle -> unhappy

number = input("Enter a number: ")
numbers_in_recursive = []

def recursive(number):
    if number in numbers_in_recursive:
        print("The number is an unhappy number!")
    else:
        digits = []
        sum_of_digits = 0

        for digit in number:
            digits.append(digit)

        print("Digits:", digits)

        for digit in digits:
            squared_digit = int(digit) ** 2
            sum_of_digits += int(squared_digit)

        print("Sum of digits:", sum_of_digits)

        if sum_of_digits == 1:
            print("The number is a happy number!")
        else:
            numbers_in_recursive.append(str(number))
            recursive(str(sum_of_digits))
        
recursive(number)
