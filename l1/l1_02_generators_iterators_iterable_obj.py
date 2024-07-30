"""Generators Iterators and iterable object"""
'''
    iterable - an object that can be “iterated over”, such as in a for-loop. https://docs.python.org/3/glossary.html#term-iterable
    Iterator - is an object that supports the next() function to remember which element will be next. https://docs.python.org/3/glossary.html#term-iterator
    Generator - is a special case of an iterator whose elements can be iterated only once. https://docs.python.org/3/glossary.html#term-generator '''


"""
generator expression - An expression that returns an iterator https://docs.python.org/3/glossary.html#term-generator-expression
"""
squares = (number ** 2 for number in range(0, 100, 6))
print(dir(squares))
print(type(squares))


def squares_generator_function(n):
    """
    generator

    :param n:
    :return: generator iterator
    """
    for e in range(0, n):
        yield e ** 2


squares_generator_function(3)  # Возвращает generator object

print(dir(squares_generator_function))
print(type(squares_generator_function))



class StringByLetter:
    """
    Class is realisation iterator protocol
    """
    def __init__(self, string):
        self.string = string
        self.str_len = len(string)
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < self.str_len:
            letter = self.string[self.position]
            self.position += 1
            return letter.upper()
        raise StopIteration


string_by_letter_test = StringByLetter(' I will be PythonDev')
for letter in string_by_letter_test:
    print(letter)


#  The same with generator
def string_by_letter_generator(string: str):
    for letter in string:
        yield letter.upper()


for letter in string_by_letter_generator('I am a Python developer'):
    print(letter)
