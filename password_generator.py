import random
import string

LENGTH_MIN = 20

class PasswordGenerator:
    lg = LENGTH_MIN
    randomizer = random.Random()

    def lower(self):
        return self.randomizer.choice(string.ascii_lowercase)

    def upper(self):
        return self.randomizer.choice(string.ascii_uppercase)

    def number(self):
        return self.randomizer.choice(string.digits)

    def punctuation(self):
        return self.randomizer.choice(string.punctuation)

    options = {
                    0: lower,
                    1: upper,
                    2: number,
                    3: punctuation
    }

    def __init__(self, beta):
        self.lg = LENGTH_MIN + beta

    def gen_pass(self):
        password = ""
        for i in range(self.lg):
            y = self.randomizer.randint(0, 3)
            password += self.options[y](self)
        return password


passGen = PasswordGenerator(10)
print("password : " + passGen.gen_pass())