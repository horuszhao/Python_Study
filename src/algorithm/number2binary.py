
def number_to_binary(b):
    r=[]
    tmp = b
    while tmp>1:
        r.append(int(tmp%2))
        tmp = (tmp-tmp%2)/2
        if(tmp==1):
            r.append(int(tmp))
    return r

r = number_to_binary(11);
r.reverse()
newR = map(lambda x:str(x),r)
print(''.join(newR))
