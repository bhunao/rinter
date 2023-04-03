# rinter

A new ~~wrong~~ way of printing something in python.

```python
rinter() >> 3141592     # `>>` prints 
3141592
rinter = rinter()       # `>>` prints 
rinter >> "text", 3, 5  # for some reasong the first element is None
("text", )
rinter << 5             # `<<`store the value inside rinter and prints it
5
```

### weird stuff i discovered doing this

**trying to print with:**
- `__matmult__` the first element becones None
- `__rshift__` only gets the first element
