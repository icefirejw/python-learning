import pprint

def inv(plist, pdic):
    for it in plist:
        if it in pdic.keys():
            pdic[it] = pdic[it] + 1
        else:
            pdic.setdefault(it, 1)


def printinv(pdic):
    tvalue = 0
    for k, v in pdic.items():
        tvalue = tvalue + v
        print('%s %s' % (k,str(v)))

    print('the total value is:' + str(tvalue))


itemlist = ['coin', 'ruby', 'coin', 'dagger', 'coin' ]
itemdic  = {'coin': 5, 'ruby': 1}

inv(itemlist, itemdic)
printinv(itemdic)
pprint.pprint(itemdic)
