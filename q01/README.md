# 人生の時計

## 問題文
あなたの一生を24時間にたとえると今日は何時何分何秒ですか？
ただしあなたはあなたの誕生日(a年b月c日)の0時ちょうどに生まれてn歳まで生きる(n歳のときは生きていてn+1歳にはなれない)とし、bとcは一般的な月日の範囲とします。

1. 1990<=a<=2000,n=80のとき、今日は何時何分何秒ですか？
2. 1900<=a<=2000,n=200のとき、今日は何時何分何秒ですか？

[Go For It 人生の時計](http://www.sony.co.jp/SonyInfo/Jobs/newgrads/sus/q01.html)より

## 実行方法
実行にはPythonが必要です。実行すると生まれた年、月、日、生きることのできる年齢を標準入力から入力すると、一生を24時間に例えた時の時刻が表示されます。

    $ python q01.py
    Birth Year?:1988
    Birth Month?:10
    Birth Day?:17
    How many years will you live?:100
     5:35:38.813720

テストするにはnosetestsが必要です。

    $ pip install nose
    nosetests

