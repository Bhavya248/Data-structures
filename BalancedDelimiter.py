#Balanced Delimiter Using Stack

from stack import *
Open  = [ "[", "{", "(" ]
Close = [ "]", "}", ")" ]

def CheckBalanced(Text):
    S = stack()
    for i in Text:
        if i in Open :
            S.push(i)
        elif i in Close :
            pos = Close.index(i)
            if ( Open[pos] != S.pop()):
                break
            else:
                pass
    if (S.length() == 0 ):
        return (True,"Stack Is balanced")
    else :
        return (False,"Stack Is Unbalanced")

    

