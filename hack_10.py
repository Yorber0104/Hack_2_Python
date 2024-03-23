"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

import json

def fn_hack_10(s):
    new_result = []
    contador = 1


    for elemento in s:
        if isinstance(elemento, dict):
            nuevo_elemento = {str(contador):str(contador + 1)}
            contador += 2
        else:
            nuevo_elemento = [str(contador),str(contador + 1)]
            contador += 2
        new_result.append(nuevo_elemento)

    return new_result

texto_original = [{"a":"b"},{"c":"d"},{"e":"f"}]
resultado = fn_hack_10(texto_original)


print(resultado)





