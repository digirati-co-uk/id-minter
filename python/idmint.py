import random
import string

identifier_length = 8
forbidden_letters = ['0', 'o', 'i', 'l', '1']

number_range = list(string.ascii_lowercase)
letter_range = list(string.digits)
character_set = number_range + letter_range
allowed_character_set = [x for x in character_set if x not in forbidden_letters]
first_character_set = [x for x in allowed_character_set if x not in letter_range]

first_range = len(first_character_set) - 1
allowed_range = len(allowed_character_set) - 1


def generate_id():
    random.seed()
    chars = [first_character_set[random.randint(0, first_range)]]
    counter = 1
    while counter < identifier_length:
        chars.append(allowed_character_set[random.randint(0, allowed_range)])
        counter = counter + 1
    identifier = ''.join(chars)
    return identifier


if __name__ == "__main__":
    for i in range(10):
        print(generate_id())