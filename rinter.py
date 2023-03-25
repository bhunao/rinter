# why?
# because yes

class rinter:
    def __init__(self) -> None: self._v = None

    def __rshift__(self, *content):
         print(content)
    def __lshift__(self, *content):
        self._v = content
        print(*content)

rinter() >> 3141592     # `>>` prints 
rinter = rinter()       # `>>` prints 
rinter >> "text", 3, 5  # for some reasong the first element is None
rinter << 5             # `<<`store the value inside rinter and prints it
