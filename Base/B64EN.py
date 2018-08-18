import  base64

a=bytes(input('输入编码内容： '),encoding='utf8')

print(base64.b64encode(a))