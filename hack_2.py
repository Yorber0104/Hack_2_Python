"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):
    result = s
    vowels = "aeiouAEIOU"
    result = ''.join([char for char in s if char not in vowels])
    return result

print(fn_hack_2("fooziman"))
print(fn_hack_2("barziman"))
print(fn_hack_2("qux"))
