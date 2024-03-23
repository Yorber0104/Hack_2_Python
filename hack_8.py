"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    new_result = []

    for i in range(len(s), 0, -1):
        if len(s) % 2 == 0:
            new_result.append(str(i))
        else:
            new_result.append(f"{s[i-1]}-{i}")
    return new_result


print(fn_hack_8(["a", "b", "c", "d", "e"]))  
print(fn_hack_8(["a", "b", "c"]))           
print(fn_hack_8(["a", "b", "c", "d"]))      
print(fn_hack_8(["a", "b"]))                


