from random import randint
miss = 0 # 間違えた数
correct = 0 # 正解数
print("問題！３回間違えたら終了。「q」で止める")
while miss < 3:
    a = randint(1, 100)
    b = randint(1, 100)
    ans = a + b
    # 問題を出題し、キーボードからの入力待ちにする
    question = f"{a} + {b} は？"
    value = input(question)
    # 「q」と入力されたら中断する
    if value == "q":
        break  # ブレイクする
    # 回答が正解かどうか判定する(入力値は文字の場合もあるので、回答を文字列型にして比較する。)
    elif value == str(ans):
        correct += 1
        print("正解です！")
    else:
        miss += 1
        print("間違い！", "×" * miss) # 間違いの数だけ「×」を表示する
print("-" * 20)
print("正解：", correct)
print("間違い：", miss)
