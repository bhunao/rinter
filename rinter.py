# why?
# because yes

class rinter:
    def __init__(self) -> None: self._v = None

    def __rshift__(self, *content):
         print(content)
    def __lshift__(self, *content):
        self._v = content
        print(*content)

def dirnter(obj, sep=' | ', end='\n'):
    for option in dir(obj):
        text = option
        if callable(getattr(obj, option)):
            text += "()"
        print(text)

    # print(*dirs, sep=sep, end=end)

rinter() >> 3141592     # `>>` prints 
rinter = rinter()       # `>>` prints 
rinter >> "text", 3, 5  # for some reasong the first element is None
rinter << 5             # `<<`store the value inside rinter and prints it
rinter >> ""



tst = [1,2,3]
dirnter(tst)
