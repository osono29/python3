from random import randint
# 値が見つかるまで無限ループする
while True:
    a = randint(1, 13)
    b = randint(1, 13)
    c = randint(1, 13)
    print(a, b, c)
    sum = a + b + c
    # 合計が21ならばブレイクする
    print(f"合計：{sum}")
    if sum == 21:
        break # ブレイクする
print("合計が21になった！")
