# 1.加入例外處理 try+except Exception as e
# 2.重複輸入，直到a=>exit 離開，使用while true

try:
    a=eval(input("請輸入a:"))
    b=eval(input("請輸入b:"))

    if a==b:
        print("a跟b一樣大")
    elif a>b:
        print(f"a>b,相差:{a-b}")
    else:
        print(f"a<b,相差:{b-a}")
except Exception as e:
    print("輸入錯誤!",e)