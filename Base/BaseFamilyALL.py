import  base64

a=bytes(input('输入编码内容： '),encoding='utf8')
a=base64.b16decode(base64.b32decode(base64.b64decode(a)))
print(a)
