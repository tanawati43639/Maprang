import re

def validate_au_phone_number(phone_number):
    pattern = re.compile(r'^(\(61\)|61)0\d{9}$')
    return bool(pattern.match(phone_number))

# Example usage:
phone_numbers = ["610426123456", "(61)0426123456", "61426123456", "61042612345", "0426123456", "860426123456"]

for number in phone_numbers:
    if validate_au_phone_number(number):
        print(f"{number} is a valid AU phone number.")
    # else:
    #     print(f"{number} is not a valid AU phone number.")