#this is the list using demo
#list's style is [xxx,yyy,zzz]

demolist=['a','cccc','dddd','abc','ddd']

def addtolist(plist,pitem):
    plist.append(pitem)
    print ('add',pitem,'to list')

def delfromlist(plist, n):
    if (int(n)>=(len(plist))):
        return
    pitem=plist[n]
    del plist[n]
    print ('delete the',n,"item:", pitem, "from list")

def printlist(plist):
    for it in plist:
        print (it),
    print ('\n')

print 'the oraginal list is:',
printlist(demolist)

print 'the list lenth is:', len(demolist)

addtolist(demolist,'abcd')
printlist(demolist)

delfromlist(demolist,3)
print demolist

print 'now sort this list'
demolist.sort()
print demolist



    
