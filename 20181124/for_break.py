numlist = [3, 4.2, 10, "x", 1, 9]  # 文字列が含まれている
sum = 0
for num in numlist:
    # num が数値ではないときブレイクする
    if not isinstance(num, (int, float)):
        # isinstance(num, (int, float))
        # ↑ num が数値のときにTrueとなる
        print(num, "数値ではありません。")
        break  # ブレイクする
        #continue  # スキップする
    sum += num
    print(num, "/", sum)
