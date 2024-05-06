x="true"
def hi():
    global x
    x="now"
def bye():
    global x
    x=x+"past"

hi()
bye()   
print(x)
