#! python3
# ----------------------------------------------------------------
# function allow user to query a dictionary and check for matching
# i.e. d = {'a':39, 'b':40, 'c':99, 'd':100}
# ----------------------------------------------------------------
def query_dic(dct, **kwargs):
    r ={k:v for k,v in kwargs.items() if dct.get(k)==v}
    return r

d = {'a':39, 'b':40, 'c':99, 'd':100}
result = query_dic(d, a=1, b=40)
print(result)

