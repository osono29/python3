# random モジュールの randint関数を読み込む
from random import randint
point = randint(0, 100) # 0~100の乱数
# 判定
if point >= 80:
    result = "A クラス"
elif point >= 60:
    result = "B クラス"
elif point >= 30:
    result = "C クラス"
else:
    result = "不適合"
# 結果の出力
print(f"{point}点：{result}")
