# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")


def hello(name, greet):
    print(f'Hello {name}, {greet}')


hello("Bean", "hope tomorrow is a better day!")


def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')


greet_with("Bean", "LA")
greet_with(location="LA", name="Bean")
