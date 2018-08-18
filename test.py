import re

try:
    import requests
except ImportError:
    raise SystemExit('\n import module error ,please pip install requests!')
s = requests.Session()
header = {'Cookie': 'PHPSESSID=21043f4dd0550ef63816741ae089ea7f'}
url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
r = s.get(url, headers=header)
c = r.content

regstr = re.compile(r'[0-9+*()]+[)]')
try:
    obj = regstr.findall(c,r)
    if obj:
        result = eval(obj[0])
        data = {'v':result}
        r = s.post(url,data=data,headers= header)
        print(r.content)
finally:
    print('ok!!!')
