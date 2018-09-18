#this is the dictionary using demo
#dictionary's style is {key1:value1,key2:value2)

AddrBook={'tom':'tom@nbcb.cn',
        'jerry':'jerry@nbcb.cn',
        'sam':'sam@nbcb.cn'}

def printdict(pdict):
    for name,addr in pdict.items():
        print ("%s:%s" %(name,addr))

def dict_Isexist(pdict,key):
    if (pdict.has_key(key)):
        return True
    else:
        return False


print ('the oraginal dictionary is:', AddrBook)
print ('now add a user')

AddrBook['bob']='bob@nbcb.cn'
print ('the new address book is:',AddrBook)

print ('sam is in the address book?',dict_Isexist(AddrBook,'sam'))
print ("pop sam's value is:",AddrBook.pop('sam'))

print ('Now,the new address book is:',AddrBook)


