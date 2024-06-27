from random import choice


class PasswordGenerator:
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET_UPPERCASE = ALPHABET.upper()
    NUMBERS = "0123456789"
    SPECIAL_CHARACTERS = "!@#$%^&*()"

    def __init__(self):
        pass

    def generate(self, pass_length):
        resulting_password = ""

        for _ in range(pass_length):
            random_letter = choice(self.ALPHABET)
            random_letter_uppercase = choice(self.ALPHABET_UPPERCASE)
            random_number = choice(self.NUMBERS)
            random_special_character = choice(self.SPECIAL_CHARACTERS)

            resulting_password += choice(
                [
                    random_letter,
                    random_number,
                    random_special_character,
                    random_letter_uppercase,
                ]
            )

        return resulting_password

    def validate(self, password):
        valid_chars = (
            self.ALPHABET
            + self.ALPHABET_UPPERCASE
            + self.NUMBERS
            + self.SPECIAL_CHARACTERS
        )
        for char in password:
            if char not in valid_chars:
                return False

        return True
