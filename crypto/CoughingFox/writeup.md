`flag`の各文字`f`に対して、

`c = (f + i)**2 + i`

で`cipher`を計算したのち`shuffle(cipher)`でシャッフルしています。

各文字に対して適当に`i (0 ≤ i < N)`引いて平方根が取れる数が`flag`の`i`文字目になります。
