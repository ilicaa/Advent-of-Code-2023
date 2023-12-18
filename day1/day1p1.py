def extract_numbers(line):
    numbers = [int(char) for char in line if char.isdigit()]
    return numbers[0], numbers[-1]

def main(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    numbers_list = [f"{num1}{num2}" for line in lines for num1, num2 in [extract_numbers(line)]]

    numbers_int = [int(number) for number in numbers_list]

    total_sum = sum(numbers_int)

    print(f"Extracted numbers: {numbers_list}")
    print(f"Sum of numbers: {total_sum}")

file_path = 'C:/vscode-python/advent_of_code23/day1.txt'

main(file_path)
