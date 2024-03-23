"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    vowels = {'a': '@', 'e': '3', 'i': '¡', 'o': '0', 'u': 'v'}
    new_result = ""

    for index, char in enumerate(s):
        converted_char = vowels.get(char.lower(), char)
        if index == 0 or index == len(s) - 1:
            converted_char = converted_char.upper()
        if s[index:index+2].lower() == "u":
            converted_char = "v"
        new_result += converted_char

    return new_result


print(fn_hack_3("fooziman"))
print(fn_hack_3("barziman"))
print(fn_hack_3("3q"))
print(fn_hack_3("qu"))
print(fn_hack_3("qux"))


