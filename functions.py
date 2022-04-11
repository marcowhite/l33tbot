import random


def traslate(a,b):
    a = a.lower()
    for ch in b.keys():
        a = a.replace(str(ch), str(b.get(ch)))
    return a

def english_to_leetspeak(message):
    """Convert english string to leetspeak"""
    char_map = {
        "a": ["4", "@", "/-\\", "^"],
        "b": ["I3", "8", "13", "|3"],
        "c": ["[", "{", "<", "("],
        "d": [")", "|)", "[)", "|>"],
        "e": ["3", "[-"],
        "f": ["|=", "ph", "|#", "/="],
        "g": ["&", "6", "(_+]", "9", "C-", "gee"],
        "h": ["#", "/-/", "[-]", "]-[", ")-(", "(-)", ":-:", "|-|", "}{"],
        "i": ["1", "[]", "!", "|", "eye", "3y3", "]["],
        "j": [",_|", "_|", "._|", "._]", ",_]", "]"],
        "k": [">|", "|<", "/<", "1<", "|c", "|(", "|{"],
        "l": ["1", "7", "|_", "|"],
        "m": ["/\\/\\", "/V\\", "JVI", "[V]", "[]V[]", "|\\/|", "^^"],
        "n": ["^/", "|\\|", "/\\/", "[\]", "<\\>", "{\\}", "|V", "/V"],
        "o": ["0", "Q", "()", "oh", "[]"],
        "p": ["|*", "|o", "?", "|^", "[]D"],
        "q": ["(_,)", "()_", "2", "O_"],
        "r": ["12", "|`", "|~", "|?", "/2", "|^", "Iz", "|9"],
        "s": ["$", "5", "z", "ehs", "es"],
        "t": ["7", "+", "-|-", "']['", '"|"', "~|~"],
        "u": ["|_|", "(_)", "V", "L|"],
        "v": ["\\/", "|/", "\\|"],
        "w": ["\\/\\/", "VV", "\\N", "'//", "\\\\'", "\\^/", "\\X/"],
        "x": ["><", ">|<", "}{", "ecks"],
        "y": ["j", "`/", "\\|/", "\\//"],
        "z": ["2", "7_", "-/_", "%", ">_", "~/_", "-\_", "-|_"],
    }
    leetspeak = ""
    for char in message:
        if char.lower() in char_map and random.random() <= 0.70:  # 70% convert
            possible_replacements = char_map[char.lower()]
            leet_replacement = random.choice(possible_replacements)
            leetspeak = leetspeak + leet_replacement
        else:
            leetspeak = leetspeak + char
    return leetspeak


class zalgo():

    def __init__(self):
        self.numAccentsUp = (1, 3)
        self.numAccentsDown = (1, 3)
        self.numAccentsMiddle = (1, 2)
        self.maxAccentsPerLetter = 3
        # downward going diacritics
        self.dd = ['̖', ' ̗', ' ̘', ' ̙', ' ̜', ' ̝', ' ̞', ' ̟', ' ̠', ' ̤', ' ̥', ' ̦', ' ̩', ' ̪', ' ̫', ' ̬', ' ̭',
                   ' ̮', ' ̯', ' ̰', ' ̱', ' ̲', ' ̳', ' ̹', ' ̺', ' ̻', ' ̼', ' ͅ', ' ͇', ' ͈', ' ͉', ' ͍', ' ͎', ' ͓',
                   ' ͔', ' ͕', ' ͖', ' ͙', ' ͚', ' ', ]
        # upward diacritics
        self.du = [' ̍', ' ̎', ' ̄', ' ̅', ' ̿', ' ̑', ' ̆', ' ̐', ' ͒', ' ͗', ' ͑', ' ̇', ' ̈', ' ̊', ' ͂', ' ̓', ' ̈́',
                   ' ͊', ' ͋', ' ͌', ' ̃', ' ̂', ' ̌', ' ͐', ' ́', ' ̋', ' ̏', ' ̽', ' ̉', ' ͣ', ' ͤ', ' ͥ', ' ͦ', ' ͧ',
                   ' ͨ', ' ͩ', ' ͪ', ' ͫ', ' ͬ', ' ͭ', ' ͮ', ' ͯ', ' ̾', ' ͛', ' ͆', ' ̚', ]
        # middle diacritics
        self.dm = [' ̕', ' ̛', ' ̀', ' ́', ' ͘', ' ̡', ' ̢', ' ̧', ' ̨', ' ̴', ' ̵', ' ̶', ' ͜', ' ͝', ' ͞', ' ͟', ' ͠',
                   ' ͢', ' ̸', ' ̷', ' ͡', ]

    def zalgofy(self, text):
        '''
        Zalgofy a string
        '''
        # get the letters list
        letters = list(text)  # ['t','e','s','t',' ','t',...]
        # print(letters)
        newWord = ''
        newLetters = []

        # for each letter, add some diacritics of all varieties
        for letter in letters:  # 'p', etc...
            a = letter  # create a dummy letter

            # skip this letter we can't add a diacritic to it
            if not a.isalpha():
                newLetters.append(a)
                continue

            numAccents = 0
            numU = random.randint(self.numAccentsUp[0], self.numAccentsUp[1])
            numD = random.randint(self.numAccentsDown[0], self.numAccentsDown[1])
            numM = random.randint(self.numAccentsMiddle[0], self.numAccentsMiddle[1])
            # Try to add accents to the letter, will add an upper, lower, or middle accent randomly until
            # either numAccents == self.maxAccentsPerLetter or we have added the maximum upper, middle and lower accents. Denoted
            # by numU, numD, and numM
            while numAccents < self.maxAccentsPerLetter and numU + numM + numD != 0:
                randint = random.randint(0, 2)  # randomly choose what accent type to add
                if randint == 0:
                    if numU > 0:
                        a = self.combineWithDiacritic(a, self.du)
                        numAccents += 1
                        numU -= 1
                elif randint == 1:
                    if numD > 0:
                        a = self.combineWithDiacritic(a, self.dd)
                        numD -= 1
                        numAccents += 1
                else:
                    if numM > 0:
                        a = self.combineWithDiacritic(a, self.dm)
                        numM -= 1
                        numAccents += 1

            # a = a.replace(" ","") #remove any spaces, this also gives it the zalgo text look
            # print('accented a letter: ' + a)
            newLetters.append(a)

        newWord = ''.join(newLetters)
        return newWord

    def combineWithDiacritic(self, letter, diacriticList):
        '''
        Combines letter and a random character from diacriticList
        '''
        return letter.strip() + diacriticList[random.randrange(0, len(diacriticList))].strip()