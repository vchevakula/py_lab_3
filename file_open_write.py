#!/usr/local/bin/python3
with open('/Users/vchevakula/python/test2.txt','r',encoding = 'utf-8') as f:
    f_contents = f.read()
    print (f_contents)
    #f.write('USCIS\n')
    #f.seek(4)
    #f.write('I have applied for my H1B')
    for f in f_contents:
	print(f)
