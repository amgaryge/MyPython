import re
import chardet
try:
    import requests
except ImportError:
    raise SystemExit('\n import module error ,please pip install requests!')
s = requests.Session()
#地址
url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
#header头
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)','Cookie': 'PHPSESSID=d155798f0fb890c54db6fb3939a51888'}

r = s.get(url, headers=headers)
c = r.content
regstr = re.compile(r'[0-9+*()]+[)]')

try:
    #python2默认和3正好相反，需要转换，str->bytes:encode编码，bytes->str:decode解码
    encode_type = chardet.detect(c)
    html = c.decode(encode_type['encoding'])
    obj = regstr.findall(html)
    #a = regstr.findall(content)
    if obj:
        result = eval(obj[0])
        #v为post的值
        data = {'v':result}
        r = s.post(url,data=data,headers= headers)
        print(r.content)
finally:
    print('ok!!!')