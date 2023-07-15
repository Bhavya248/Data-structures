#prefix to postfix notation using Stack
from stack import *
operators = {'+','-','*','/'}

def PrefixToInfix(_text):
    opArray = []
    l1 = len(_text)
    for i in range(l1) :
        if _text[i] in operators:
            opArray.append([_text[i],i])
    l2 = len(opArray)
    for i in range(len(opArray)):
        t = opArray.pop()
        replc = 2*(l2)-1
        del _text[t[1]]
        _text.insert(replc,t[0])
        l2 -= 1 

    return _text
        
def PrefixToPostfix(_text):
    _temp = stack()
    for i in reversed(_text) :
        if i in operators:
            a = _temp.pop()
            b = _temp.pop()
            _temp.push(a+b+i)
        else:
            _temp.push(i)
    return _temp.items

Text = "+/+347*28"
print(PrefixToPostfix(Text))
print("".join(PrefixToInfix(list(Text))))


