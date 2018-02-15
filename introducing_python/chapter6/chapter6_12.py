# 6.12 특수 메서드
class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()
first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))
print(first.equals(third))

class Word2():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first == second)
print(first == third)

first = Word2('ha')
first
print(first)

class Word3():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return print("Word('" + self.text + "')")

first = Word3('ha')
first
Word3("ha")
print(first)