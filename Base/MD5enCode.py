import hashlib

str=input('输入需要加密的字符串： ')
# 创建md5对象
hl = hashlib.md5()
hl.update(str.encode(encoding='utf-8'))

print(hl.hexdigest())