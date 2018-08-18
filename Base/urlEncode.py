from urllib import parse

str1 = input( '输入需要url编码的内容： ')
str2 = parse.quote(str1)    #将字符串进行编码
print(str2)