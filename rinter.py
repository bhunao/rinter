# why?
# because yes
from dataclasses import dataclass


class rinter:
    def __init__(self) -> None: self._v = None

    def __rshift__(self, *content):
         print(content)
    def __lshift__(self, *content):
        self._v = content
        print(*content)


@dataclass
class function:
    def __init__(self, f=sum) -> None:
        self.f = f
        self.val1 = None
        self.val2 = None
        self.re = None

    def __matmul__(self, other):
        print(other, self.val1, self.val2)
        if not self.val1:
            self.val1 = other
        elif not self.val2:
            self.val2 = other
            self.re = self.f([self.val1, self.val2])
            return self.re
        return self

    def __rmatmul__(self, other):
        print(other, self.val1, self.val2)
        if not self.val1:
            self.val1 = other
        elif not self.val2:
            self.val2 = other
            self.re = self.f([self.val1, self.val2])
            return self.re
        return self

    def __str__(self) -> str:
        return f"{self.f}, {self.val1}, {self.val2}, {self.re}"

    

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
# dirnter(tst)

f = function()
coisa = 5 @ f @ 10
print(coisa)
print(coisa)
