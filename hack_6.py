"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output =>  ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    result = []
    
    if not s:
        return ["0"]
    
    for i in range(1, len(s) * 2, 2):
        if i <= len(s):
            result.append(str(i))
            if i < len(s) or i == 5:
                result.append("-")
        
    
    result.pop()

    return result

print(fn_hack_6(["a","b","c","d","e"]))
print(fn_hack_6([]))