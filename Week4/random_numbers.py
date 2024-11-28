import random

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers_list=numbers,quantity=3)
    print(numbers)

def append_random_numbers(numbers_list,quantity=1):
    for x in range(0,quantity):
        numbers_list.append(round(random.uniform(0, 99.9), 1))
def append_random_words(words_list, quantity=1):
    words = ['cane', 'bane', 'laptop', 'car','bed', 'man','girl']
    for x in range(0,quantity):
        words_list.append(random.choice(words))

append_random_words()
if __name__ == '__main__':
    main()
