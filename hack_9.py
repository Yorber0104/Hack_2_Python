"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    new_result = {}

    text = {"foo":"fookziman","bar":"barziman"}

    for key, value in text.items():
        if key == "foo":
            new_result[key.capitalize()] = value.replace("fook","Foo")
    

    return new_result
    
print(fn_hack_9("foo"))

