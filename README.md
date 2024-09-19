## pythonのテストで使う問題です。
### 問題1
変数 x が 10 より大きいかどうかを判定し、大きい場合は**大きい**、そうでない場合は**小さい**と表示してください。<br>
入力例:
```
20
```
出力結果
```
大きい
```
### 問題2
**1からx**までの数字を順に表示してください。ただし、次のルールに従ってください

数字が3で割り切れる場合、その数字の代わりに「Fizz」と表示します。
数字が5で割り切れる場合、その数字の代わりに「Buzz」と表示します。
数字が3でも5でも割り切れる場合、その数字の代わりに「FizzBuzz」と表示します。

また50からまで次のルールに変更してください。
数字が3で割り切れる場合、その数字の代わりに「!Buzz」と表示します。
数字が5で割り切れる場合、その数字の代わりに「!Fizz」と表示します。
数字が3でも5でも割り切れる場合、その数字の代わりに「!FizzBuzz」と表示します。<br>
入力例:
```
101
```
出力結果
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
!Buzz
52
53
!Buzz
!Fizz
56
!Buzz
58
59
!FizzBuzz
61
62
!Buzz
64
!Fizz
!Buzz
67
68
!Buzz
!Fizz
71
!Buzz
73
74
!FizzBuzz
76
77
!Buzz
79
!Fizz
!Buzz
82
83
!Buzz
!Fizz
86
!Buzz
88
89
!FizzBuzz
91
92
!Buzz
94
!Fizz
!Buzz
97
98
!Buzz
!Fizz
```

### 問題3
あなたはテレビ番組の放送禁止用語を検閲するために雇われました。x個ある放送禁止用語はリストで指定されています。視聴者に適切な放送を届けるために、以下の文中に含まれる禁止用語を「\*」に置き換えてください。禁止用語の文字数に応じて、文字ごとに「\*」を表示します。<br>
入力例 xが3の場合:
```
3
訪れる人々
観光客
感動
歴史的な重要性を持つ、世界的に有名な建築物が立ち並ぶ都市の中心部には、訪れる人々を魅了するさまざまな文化施設や観光名所が点在しており、それぞれの施設が持つ独自の歴史と魅力によって、数多くの観光客がその地域の豊かな文化遺産を体験し、感動を覚えることができるでしょう。
```
出力結果
```
歴史的な重要性を持つ、世界的に有名な建築物が立ち並ぶ都市の中心部には、*****を魅了するさまざまな文化施設や観光名所が点在しており、それぞれの施設が持つ独自の歴史と魅力によって、数多くの***がその地域の豊かな文化遺産を体験し、**を覚えることができるでしょう。
```
### 問題4
**human**というclassを作成し名前**name**と年齢**age**を持たせx人作成してください。また**hello**メソッドを用意し、**name**と**age**を使い自己紹介をさせてください。
<br>自己紹介は以下のようなフォーマットにしてください
```
こんにちは私の名前は[name]です。年齢は[age]です。
```
入力例 xが1の場合:
```
1
グイド・ヴァン・ロッサム
68
```
出力結果
```
こんにちは私の名前はグイド・ヴァン・ロッサムです。年齢は68歳です。
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

**Animal** クラスを使って、x匹の動物を作成してください。それぞれの動物には異なる名前と年齢を設定します。
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
入力例 xが2の場合:
```
2
猫
12
犬
3
```
出力結果:
```
名前:猫,年齢12
名前:犬,年齢3
猫は年長です
犬は若いです
```
