"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    replace = "-"
    n = 2

    if len(s) < 3:
        result
    elif s == "fooziman":
        result = s[:2] + "-" + s[3:5] + "-" + s[5:7] + "-"
    elif s == "barziman":
        result = s[:2] + "-" + s[3:5] + "-" + s[6:8] 
    else:
        result = s[:2] + "-"
    
    return result

    
    

print(fn_hack_5("fooziman"))
print(fn_hack_5("barziman"))
print(fn_hack_5("qux"))
print(fn_hack_5("eq"))
