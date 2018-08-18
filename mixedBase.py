from base64 import *
import itertools
s=open('mixedBase.txt','r').read()
result={
    '16':lambda x:b16decode(x),
    '32':lambda x:b32decode(x),
    '64':lambda x:b64decode(x)
    }
for i_1 in ['16','32','64']:
    for i_2 in ['16','32','64']:
        for i_3 in ['16','32','64']:
            for i_4 in ['16','32','64']:
                for i_5 in ['16','32','64']:
                    for i_6 in ['16','32','64']:
                        for i_7 in ['16','32','64']:
                            for i_8 in ['16','32','64']:
                                for i_9 in ['16','32','64']:
                                    for i_10 in ['16','32','64']:
                                        try:
                                            print(result[i_10](result[i_9](result[i_8](result[i_7](result[i_6](result[i_5](result[i_4](result[i_3](result[i_2](result[i_1](s)))))))))))
                                        except:
                                            continue