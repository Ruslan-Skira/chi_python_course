"""Data types and objects in Python"""
# Immutable object

x = 2  # int
print(id(x), type(x))
x *= .2
print(id(x), type(x))
# str
country_name = "Vatican City"
print(id(country_name))
country_name += " the smallest country in world"
print(id(country_name))

# is vs ==
greetings_first = "Hello awesome python developers"
greetings_second = "Hello awesome python developers"

print(greetings_first is greetings_second, greetings_first == greetings_second)

# frozenset
fz = frozenset({"ips not changed", "important unique data", "255.255.0.0.1"})

# tuple
ukrainians_presidents = ("Leonid Kravchuk", "Leonid Kuchma", "Viktor Yushchenko", "Viktor Yanukovych", "Oleksandr Turchynov", "Petro Poroshenko", "Volodymyr Zelenskyy")

# Mutable objects
l = list()
d = dict()
s = set()

# What the main difference between mutable and immutable
__hash__()
__eq__()

