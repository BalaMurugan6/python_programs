boy=input("Enter boy name").lower()
girl=input("Enter girl name").lower()
boy=list(boy.replace(" ",""))
girl=list(girl.replace(" ",""))
for i in boy:
    if i in girl:
        boy.remove(i)
        girl.remove(i)
count=len(boy)+len(girl)

if count>0:
  flames=["Friends","Love","Affection","Marriage","Enemy","Siblings"]
  while len(flames)>1:
     c=count%len(flames)
     index=c-1
     if index>=0:
         left=flames[:index]
         right=flames[index+1:]
         flames=right+left
     else:
         flames=flames[:len(flames)-1]
  print(f"Relationship is {flames[0]}")
else:
    print("enter different name")