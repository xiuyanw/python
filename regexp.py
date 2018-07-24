import re
result=re.finditer('f..','seafood is food')
for m in result:
    print(m.group())
