i = 50
def foo():
    global i
    i = 100
    return i

foo()
print(i)
