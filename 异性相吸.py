ens=open('en.txt','r').read()#密文
des=open('de.txt','r').read()#明文
for i in range(len(des)):
    print(chr(ord(des[i])^ord(ens[i])))