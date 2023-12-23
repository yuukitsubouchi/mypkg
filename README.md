# ros2
[![test](https://github.com/yuukitsubouchi/ros2_ws/actions/workflows/suuretu_test.yml/badge.svg)](https://github.com/yuukitsubouchi/ros2_ws/actions/workflows/suuretu_test.yml)
[![test](https://github.com/yuukitsubouchi/ros2_ws/actions/workflows/test.yml/badge.svg)](https://github.com/yuukitsubouchi/ros2_ws/actions/workflows/test.yml)
ros2のパッケージ

##リポジトリの一覧
#talker.pyについて
* データをトピックに送信するためのパブリッシャーを持つノードである。
* 数字をカウントしてトピック（`/countup`)を通じて送信する。
* メッセージの型は１６ビット符号付き整数

#listener.pyについて
* トピックに送信されたデータを受信するためにのサブスクライバを持つノードである。
* トピック（`/countup`)から送信されたデータを受け取り表示する。

#talk_listener.launch.pyについて
* 複数のノードを立ち上げるlaunchファイルで、talker.pyとlistener.pyを一度に立ち上げるもの。

#suuretu.py
* パブリッシャーを持つノードである。
* 調和数列を項の数だけ足した和の数値を`harmonic_sum`を通じて送信する。
* メッセージの型は１６ビット符号付き整数

#ans.py
* サブスクライバを持つノードである。
* トピック（`harmonic_sum`)から送られてきた数値を受け取り表示する。

#suuretu_ans.launch.py
* 複数のノードを立ち上げるlaunchファイルで、suuretu.pyとans.pyを一度に立ち上げるもの。

##実行手順

* `~/ros2_ws$`上で`colcon build`と`source ~/.bashrc`をしてから`ros run`で実行する。
#talkerとlistener

```bash
ros2 run mypkg talker
```
* 上のプログラムを実行すると以下のようになる。
* 終了するときは`Ctrl+C`である。

```bash
ros2 run mypkg listener
```
* 上のプログラムを実行すると以下のようになる。
* 終了するときは`Ctrl+C`である。

#talk_listener.launch
```bash
ros2 launch mypkg talk_listener.launch.py 
```
* 上のプログラムを実行すると以下のようになる。
* 終了するときは`Ctrl+C`である。

#suuretuとans
```bash
ros2 run mypkg suuretu
```
* 上のプログラムを実行すると以下のようになる。
* 終了するときは`Ctrl+C`である。

```bash
ros2 run mypkg ans
```
* 上のプログラムを実行すると以下のようになる。
* 終了するときは`Ctrl+C`である。

#suuretu_ans.launch
```bash
ros2 launch mypkg suuretu_ans.launch.launch.py
```
* 上のプログラムを実行すると以下のようになる。
* 終了するときは`Ctrl+C`である。

##必要なソフトウェア
* Python

##テスト環境
* Ubuntu 20.04
* ROS2 foxy

##ライセンス
* このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。
* このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuici Ueda)のものを本人の許可を得て自身の著作としたものです。
 * [ryuichiueda.github.io/my_slides/robosys_2022/lesson8](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8)
 * [ryuichiueda.github.io/my_slides/robosys_2022/lesson9](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9)
 * [ryuichiueda.github.io/my_slides/robosys_2022/lesson10](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10)



* © 2023 Yuuki Tsubouchi
