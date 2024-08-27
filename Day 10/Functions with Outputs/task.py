def format_name(f_name, l_name):
    first_name = f_name.title()
    last_name = l_name.title()
    return f'{first_name} {last_name}'


formatted_name = format_name("AKxa", "aLEx")
print(formatted_name)

output = len('Bean')
print(output)


def function_1(text):
    return text + text


def function_2(text):
    return text.title()

output_1 = function_2(function_1('Hello'))
print(output_1)

