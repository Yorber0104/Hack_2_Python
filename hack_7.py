"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = s
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    new_result = []
    numero = 0
    
    if not s:
        return [0]
    else:
        for letra in s:
            if str(letra) in alfabeto:
                numero = alfabeto.index(letra) + 1
            new_result.append(str(numero) if numero % 2 == 1 else (numero))
   

    return new_result

print(fn_hack_7(["a","b","c","d","e"]))
print(fn_hack_7([]))




