a=eval(input("請輸入a:"))
b=eval(input("請輸入b:"))

if a==b:
    print("a跟b一樣大")
elif a>b:
    print(f"a>b,相差:{a-b}")
else:
    print(f"a<b,相差:{b-a}")