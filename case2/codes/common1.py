def adds(x,y):
    if isinstance(x,int) and isinstance(y,int):
        result = x+y
        return result
    else:
        return None
def sub(x,y):
    return x * y

def get_common(x,y):
    z = []
    for i in x:
        if i in y:
            z.append(i)
    return z
def uniq(x):
    z = [] 
    for i in x:
        if i not in z:
            z.append(i)
    return z