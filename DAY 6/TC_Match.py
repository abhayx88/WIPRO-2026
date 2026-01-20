import re
text="python is powerful"
result=re.match("python",text)
if result:
    print("match found")
else:
    print("no match found")

searchresult=re.search("powerful",text)
print(searchresult.group())
print(searchresult.start())
print(searchresult.end())

email="admin@gmail.com"
if re.match(r"[a-zA-Z]+@",email):
    print("Valid Start")
else:
    print("no Valid Start")
