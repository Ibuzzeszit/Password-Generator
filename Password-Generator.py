import random
import itertools
# The passwords generated will be 8 characters long and will have to include the following characters in any order:

#2 uppercase letters from A to Z,
#2 lowercase letters from a to z,
#2 digits from 0 to 9,
#2 punctuation signs such as !, ?, “, # etc.

uppers = [chr(random.randint(65, 90)), chr(random.randint(65, 90))]
lowers = [chr(random.randint(97, 122)), chr(random.randint(97, 122))]
digits = [chr(random.randint(48, 57)), chr(random.randint(48, 57))]
symbols = [chr(random.randint(33, 47)), chr(random.randint(33, 47))]

password = list(itertools.chain(*[uppers, lowers, digits, symbols]))

random.shuffle(password)

print(password)
