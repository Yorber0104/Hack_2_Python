"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    if s.startswith("foo") or s.startswith("bar"):
        return s[1:-1]
    else:
        return result
        

print(fn_hack_4("fooziman"))
print(fn_hack_4("barziman"))
print(fn_hack_4("qux"))
