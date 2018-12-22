from random import randint
numbers = []  # 空のリスト
# numbers の値が 10 個になるまで繰り返す
while len (numbers) < 10:
    n = randint(-10, 90) # -10~90 の乱数
    if n < 0:
        # nがマイナスならブレイクする
        print("中断されました")
        break
    if n in numbers:
        # n が numbers に含まれていたらスキップする
        continue
    # numbers に n を追加する
    numbers.append(n)
else: # 繰り返しが終わったら実行される（break 後はスルーされる）
    print(numbers)
