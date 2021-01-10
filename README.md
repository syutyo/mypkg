# ロボットシステム学

## 問題児時計 ~~ あなたは正確な時間を得ることができるのか~~ 

ロボットシステム学の課題２で作成したものです。

正確な時間を教えてもらうためにはじゃんけんをするか、問題に正解しなければならず、正解するかじゃんけんで勝つと正確な時間を、間違えるか負けるとUNIX時間を教えられます。
## 動作環境
---
以下の環境で動作確認しました

- Ubuntu 20.04 LTS
- ROS noetic
- Raspberry Pi4 Model B

## 実際の動きの動画
---
デモ動画はこちらです。

https://www.youtube.com/watch?v=p7LifxUswQQ


# インストール方法
本パッケージはROSをインストールしていることが前提なので、インストールされていない場合は、[ROS wiki](http://wiki.ros.org/noetic)を参照しインストールしてください

下記のコマンドをうち本パッケージをインストールしてください
~~~
cd ~/catkin_ws/src
git clone https://github.com/syutyo/mypkg.git
~~~
下記のコマンドで本パッケージをビルドします
~~~
cd ~/catkin_ws && catkin_make
~~~

## 使い方
下記のコマンドを実行してください
~~~
roslaunch mypkg start.launch --screen
~~~
起動したら、プログラムに沿って入力してください

## LICENSE
---
[BSD 3-Clause License](https://github.com/syutyo/mypkg/blob/master/LICENSE)