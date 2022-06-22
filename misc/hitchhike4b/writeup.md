# 解法
ncで接続すると、以下のような出力が得られた。  
```bash
$ nc hitchhike4b.quals.beginners.seccon.jp 55433
 _     _ _       _     _     _ _        _  _   _
| |__ (_) |_ ___| |__ | |__ (_) | _____| || | | |__
| '_ \| | __/ __| '_ \| '_ \| | |/ / _ \ || |_| '_ \
| | | | | || (__| | | | | | | |   <  __/__   _| |_) |
|_| |_|_|\__\___|_| |_|_| |_|_|_|\_\___|  |_| |_.__/


----------------------------------------------------------------------------------------------------

# Source Code

import os
os.environ["PAGER"] = "cat" # No hitchhike(SECCON 2021)

if __name__ == "__main__":
    flag1 = "********************FLAG_PART_1********************"
    help() # I need somebody ...

if __name__ != "__main__":
    flag2 = "********************FLAG_PART_2********************"
    help() # Not just anybody ...

----------------------------------------------------------------------------------------------------

Welcome to Python 3.10's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the internet at https://docs.python.org/3.10/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help>
```
上部にプログラムのソースが表示されている。  
動作としては`help()`を呼んでいるだけで、フラグは変数として保持されているようだ。  
SECCON 2021の[hitchhike](https://ptr-yudai.hatenablog.com/entry/2021/12/19/232158#Misc-227pts-hitchhike)ではページャーとしてlessが使えるが、今回はcatに書き換えられている。  
ページャーからの解決は難しそうである。  
`help`について調査することにし、[ここ](https://docs.python.org/ja/3/library/functions.html#help)を見ると中身はpydocとinspectが使われているようだ。  
pydocについては[ここ](https://docs.python.org/ja/3/library/pydoc.html)を見ればよい。  
以下のようなことが書かれている。  
```
オブジェクトとそのドキュメントを探すために、 pydoc はドキュメント対象のモジュールを import します。そのため、モジュールレベルのコードはそのときに実行されます。 if __name__ == '__main__': ガードを使って、ファイルがスクリプトとして実行したときのみコードを実行し、importされたときには実行されないようにして下さい。
```
`help`に指定したモジュールはimportされるため、ガード(`if __name__ == "__main__":`)が無いすべてのコードが実行されるようだ。  
さらに次のような記述が見られる。  
```
pydoc への引数がパスと解釈されるような場合で(オペレーティングシステムのパス区切り記号を含む場合です。例えばUnixならばスラッシュ含む場合になります)、さらに、そのパスがPythonのソースファイルを指しているなら、そのファイルに対するドキュメントが生成されます。
```
これにより任意の(実行中の自身を含む)pyファイルのドキュメントを生成できることがわかる。  
次にinspectについて[ここ](https://docs.python.org/ja/3/library/inspect.html)を見る。  
活動中のオブジェクトから情報を取得するようなので、変数を取得していることを期待して`help`から実行中のスクリプトのドキュメントを生成することを狙う。  
ここで、実行されているpythonのファイル名を探す必要があるが、ドキュメントの作成のみしか行えないことに気づく。  
変数でファイル名を保持していそうなものを探せばよい。  
コマンドライン引数の最初はファイル名であるはずなので、pythonのコマンドライン引数を用いる方法`sys.argv`を思い出し、取得すればよい(ほかにも`modules`からなど様々な方法がある)。  
```bash
help> sys
Help on built-in module sys:

NAME
    sys
~~~
DATA
~~~
    argv = ['./app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc.py']
~~~
help>
```
ファイル名が`app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc.py`とわかった。  
`help`でファイル名(拡張子なし)を指定してやる。  
```bash
help> app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc
 _     _ _       _     _     _ _        _  _   _
| |__ (_) |_ ___| |__ | |__ (_) | _____| || | | |__
| '_ \| | __/ __| '_ \| '_ \| | |/ / _ \ || |_| '_ \
| | | | | || (__| | | | | | | |   <  __/__   _| |_) |
|_| |_|_|\__\___|_| |_|_| |_|_|_|\_\___|  |_| |_.__/

~~~
help>

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
Help on module app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc:

NAME
    app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc

DATA
    flag2 = 'y_34r5_4nd_1n_my_3y35}'

FILE
    /home/ctf/hitchhike4b/app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc.py


help>
```
もう一度hitchhike4bが起動し、終了すると変数がドキュメントとして表示されていることがわかる。  
`flag2`が取得できたが、`flag1`が見えていない。  
ここでNAMEに注目すると`app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc`である。  
つまり`if __name__ != "__main__":`を通って`help`が呼び出されているので、NAMEを`__main__`にしてやれば`flag1`も同様に取得できると考えられる。  
```bash
help> __main__
Help on module __main__:

NAME
    __main__

DATA
    __annotations__ = {}
    flag1 = 'ctf4b{53cc0n_15_1n_m'

FILE
    /home/ctf/hitchhike4b/app_35f13ca33b0cc8c9e7d723b78627d39aceeac1fc.py


help>
```
`help`に`__main__`を渡してやると、案の定`flag1`が取得できた。  
`flag1`、`flag2`をつなげるとflagとなった。  

## ctf4b{53cc0n_15_1n_my_34r5_4nd_1n_my_3y35}