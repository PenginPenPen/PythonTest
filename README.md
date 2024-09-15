## pythonのテストで使う問題です。
このリポジトリをクローンして問題フォルダに回答を記述してください。
### 問題1
変数 x が 10 より大きいかどうかを判定し、大きい場合は**大きい**、そうでない場合は**小さい**と表示してください。
### 問題2
**1から100**までの数字を順に表示してください。ただし、次のルールに従ってください

数字が3で割り切れる場合、その数字の代わりに「Fizz」と表示します。
数字が5で割り切れる場合、その数字の代わりに「Buzz」と表示します。
数字が3でも5でも割り切れる場合、その数字の代わりに「FizzBuzz」と表示します。

また50からまで次のルールに変更してください。
数字が3で割り切れる場合、その数字の代わりに「!Buzz」と表示します。
数字が5で割り切れる場合、その数字の代わりに「!Fizz」と表示します。
数字が3でも5でも割り切れる場合、その数字の代わりに「!FizzBuzz」と表示します。
### 問題3
あなたはテレビ番組の放送禁止用語を検閲するために雇われました。放送禁止用語はリストで指定されています。視聴者に適切な放送を届けるために、以下の文中に含まれる禁止用語を「\*」に置き換えてください。禁止用語の文字数に応じて、文字ごとに「\*」を表示します。

### 禁止用語リスト
+ 禁止用語1: "訪れる人々"
+ 禁止用語2: "観光客"
+ 禁止用語3: "感動"

### 与えられる文章
```
text = "歴史的な重要性を持つ、世界的に有名な建築物が立ち並ぶ都市の中心部には、訪れる人々を魅了するさまざまな文化施設や観光名所が点在しており、それぞれの施設が持つ独自の歴史と魅力によって、数多くの観光客がその地域の豊かな文化遺産を体験し、感動を覚えることができるでしょう。"
```
> [!TIP]
> 上の文章はコピーしてそのままで使えるようになっています。
### 問題4
**human**というclassを作成し名前**name**と年齢**age**を持たせ5人作成してください。また**hello**メソッドを用意し、**name**と**age**を使い自己紹介をさせてください。
<br>自己紹介は以下のようなフォーマットにしてください
```
こんにちは私の名前は[name]です。年齢は[age]です。
```
### 問題5
**Animal** という名前のクラスを作成してください。このクラスは以下の2つの属性を持ちます:

name（動物の名前、文字列型）
age（動物の年齢、整数型）
クラス内に **describe** という名前のメソッドを定義してください。このメソッドは、動物の名前と年齢を表示します。表示の形式は
```
「名前: [名前], 年齢: [年齢]」
```
としてください。
### 5-1動物の作成

**Animal** クラスを使って、5匹の動物を作成してください。それぞれの動物には異なる名前と年齢を設定します。
作成した動物を全て **animals** というリストに格納してください。
### 5-2動物の説明の出力

**animals** リストに格納されている全ての動物について、**describe** メソッドを使ってその説明を表示してください。
### 5-3年齢の判定

動物の年齢を判定する関数 check_age を定義してください。関数内で以下のように処理を行ってください:
引数として **Animal** クラスのインスタンスを受け取ります。
もし動物の年齢が7歳以上なら
```
[名前]は年長です。
```
と表示します。
それ以外（6歳以下）なら
```
[名前]は若いです。
```
と表示します。
