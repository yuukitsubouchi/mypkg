# ros2

[![test](https://github.com/yuukitsubouchi/ros2_ws/actions/workflows/suuretu_test.yml/badge.svg)](https://github.com/yuukitsubouchi/ros2_ws/actions/workflows/suuretu_test.yml)
[![test](https://github.com/yuukitsubouchi/ros2_ws/actions/workflows/test.yml/badge.svg)](https://github.com/yuukitsubouchi/ros2_ws/actions/workflows/test.yml)

ros2のパッケージ

# リポジトリの一覧
## talker.pyについて
* データをトピックに送信するためのパブリッシャーを持つノードである。
* 数字をカウントしてトピック（`/countup`)を通じて送信する。
* メッセージの型は１６ビット符号付き整数

## listener.pyについて
* トピックに送信されたデータを受信するためにのサブスクライバを持つノードである。
* トピック（`/countup`)から送信されたデータを受け取り表示する。

## talk_listener.launch.pyについて
* 複数のノードを立ち上げるlaunchファイルで、talker.pyとlistener.pyを一度に立ち上げるもの。

## suuretu.pyについて
* パブリッシャーを持つノードである。
* 調和数列を項の数だけ足した和の数値を`harmonic_sum`を通じて送信する。
* メッセージの型は１６ビット符号付き整数
* 送られる数値を表示する。

## ans.pyについて
* サブスクライバを持つノードである。
* トピック（`harmonic_sum`)から送られてきた数値を受け取り表示する。

## suuretu_ans.launch.pyについて
* 複数のノードを立ち上げるlaunchファイルで、suuretu.pyとans.pyを一度に立ち上げるもの。

# 実行手順

* `~/ros2_ws$`上で`colcon build`と`source ~/.bashrc`をしてから`ros run`で実行する。
## talkerとlistener

```bash
ros2 run mypkg talker
```
* 上のプログラムを実行すると何も表示されない。
* 終了するときは`Ctrl+C`である。

```bash
ros2 run mypkg listener
```
* 上のプログラムを実行すると以下のようになる。
```bash
                             .
                             .
                             .
[INFO] [1703310437.194430959] [listener]: Listen: 11
[INFO] [1703310437.687230601] [listener]: Listen: 12
[INFO] [1703310438.187462972] [listener]: Listen: 13
[INFO] [1703310438.687530041] [listener]: Listen: 14
[INFO] [1703310439.187801154] [listener]: Listen: 15
[INFO] [1703310439.687243995] [listener]: Listen: 16
[INFO] [1703310440.187479964] [listener]: Listen: 17
[INFO] [1703310440.687557093] [listener]: Listen: 18
[INFO] [1703310441.187874645] [listener]: Listen: 19
[INFO] [1703310441.687225464] [listener]: Listen: 20
[INFO] [1703310442.187271483] [listener]: Listen: 21
[INFO] [1703310442.687637618] [listener]: Listen: 22
[INFO] [1703310443.187523900] [listener]: Listen: 23
                             .
　　　　　　　　　　　　　　 .
                             .
```

* 終了するときは`Ctrl+C`である。

## talk_listen.launch

```bash
ros2 launch mypkg talk_listener.launch.py 
```
* 上のプログラムを実行すると以下のようになる。
```bash
[INFO] [launch]: All log files can be found below /home/dragonet/.ros/log/2023-12-23-14-55-01-252077-Godzilla-4658
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [4660]
[INFO] [listener-2]: process started with pid [4662]
[listener-2] [INFO] [1703310902.073456667] [listener]: Listen: 0
[listener-2] [INFO] [1703310902.568216836] [listener]: Listen: 1
[listener-2] [INFO] [1703310903.068120975] [listener]: Listen: 2
[listener-2] [INFO] [1703310903.567958146] [listener]: Listen: 3
[listener-2] [INFO] [1703310904.068463454] [listener]: Listen: 4
[listener-2] [INFO] [1703310904.568180661] [listener]: Listen: 5
[listener-2] [INFO] [1703310905.068261217] [listener]: Listen: 6
[listener-2] [INFO] [1703310905.567974748] [listener]: Listen: 7
[listener-2] [INFO] [1703310906.068389045] [listener]: Listen: 8
[listener-2] [INFO] [1703310906.568277140] [listener]: Listen: 9
[listener-2] [INFO] [1703310907.068014773] [listener]: Listen: 10
[listener-2] [INFO] [1703310907.568256124] [listener]: Listen: 11
[listener-2] [INFO] [1703310908.068056530] [listener]: Listen: 12
[listener-2] [INFO] [1703310908.567998084] [listener]: Listen: 13
[listener-2] [INFO] [1703310909.067985625] [listener]: Listen: 14
[listener-2] [INFO] [1703310909.568147845] [listener]: Listen: 15
[listener-2] [INFO] [1703310910.068439032] [listener]: Listen: 16
                               .
                               .
                               .
```

* 終了するときは`Ctrl+C`である。

## suuretuとans
```bash
ros2 run mypkg suuretu
```
* 上のプログラムを実行すると以下のようになる。
```bash
項数: 1, 調和数列の和: 1.0000
項数: 2, 調和数列の和: 1.5000
項数: 3, 調和数列の和: 1.8333
項数: 4, 調和数列の和: 2.0833
項数: 5, 調和数列の和: 2.2833
項数: 6, 調和数列の和: 2.4500
項数: 7, 調和数列の和: 2.5929
項数: 8, 調和数列の和: 2.7179
項数: 9, 調和数列の和: 2.8290
項数: 10, 調和数列の和: 2.9290
項数: 11, 調和数列の和: 3.0199
項数: 12, 調和数列の和: 3.1032
項数: 13, 調和数列の和: 3.1801
項数: 14, 調和数列の和: 3.2516
項数: 15, 調和数列の和: 3.3182
項数: 16, 調和数列の和: 3.3807
項数: 17, 調和数列の和: 3.4396
項数: 18, 調和数列の和: 3.4951
項数: 19, 調和数列の和: 3.5477
項数: 20, 調和数列の和: 3.5977
項数: 21, 調和数列の和: 3.6454
項数: 22, 調和数列の和: 3.6908
項数: 23, 調和数列の和: 3.7343
項数: 24, 調和数列の和: 3.7760
項数: 25, 調和数列の和: 3.8160
項数: 26, 調和数列の和: 3.8544
              .
              .
              .

```
* 終了するときは`Ctrl+C`である。

```bash
ros2 run mypkg ans
```
* 上のプログラムを実行すると以下のようになる。
```bash
[INFO] [1703311074.833446441] [ans]: 調和数列の和: 1.0000, 項:1
[INFO] [1703311075.328331267] [ans]: 調和数列の和: 1.5000, 項:2
[INFO] [1703311075.828191549] [ans]: 調和数列の和: 1.8333, 項:3
[INFO] [1703311076.328173462] [ans]: 調和数列の和: 2.0833, 項:4
[INFO] [1703311076.827916715] [ans]: 調和数列の和: 2.2833, 項:5
[INFO] [1703311077.328114075] [ans]: 調和数列の和: 2.4500, 項:6
[INFO] [1703311077.827928714] [ans]: 調和数列の和: 2.5929, 項:7
[INFO] [1703311078.328110838] [ans]: 調和数列の和: 2.7179, 項:8
[INFO] [1703311078.827969395] [ans]: 調和数列の和: 2.8290, 項:9
[INFO] [1703311079.328068102] [ans]: 調和数列の和: 2.9290, 項:10
[INFO] [1703311079.828135510] [ans]: 調和数列の和: 3.0199, 項:11
[INFO] [1703311080.327838422] [ans]: 調和数列の和: 3.1032, 項:12
[INFO] [1703311080.828391061] [ans]: 調和数列の和: 3.1801, 項:13
[INFO] [1703311081.328158660] [ans]: 調和数列の和: 3.2516, 項:14
[INFO] [1703311081.827998588] [ans]: 調和数列の和: 3.3182, 項:15
[INFO] [1703311082.328013595] [ans]: 調和数列の和: 3.3807, 項:16
[INFO] [1703311082.827844521] [ans]: 調和数列の和: 3.4396, 項:17
[INFO] [1703311083.328013355] [ans]: 調和数列の和: 3.4951, 項:18
[INFO] [1703311083.828199807] [ans]: 調和数列の和: 3.5477, 項:19
[INFO] [1703311084.327823945] [ans]: 調和数列の和: 3.5977, 項:20
                             .
                             .
                             .
```

* 終了するときは`Ctrl+C`である。

## suuretu_ans.launch
```bash
ros2 launch mypkg suuretu_ans.launch.launch.py
```
* 上のプログラムを実行すると以下のようになる。
```bash

[INFO] [launch]: All log files can be found below /home/dragonet/.ros/log/2023-12-23-15-03-04-832880-Godzilla-4935
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [suuretu-1]: process started with pid [4937]
[INFO] [ans-2]: process started with pid [4939]
[ans-2] [INFO] [1703311385.643908522] [ans]: 調和数列の和: 1.0000, 項:1
[ans-2] [INFO] [1703311386.138107376] [ans]: 調和数列の和: 1.5000, 項:2
[ans-2] [INFO] [1703311386.637663748] [ans]: 調和数列の和: 1.8333, 項:3
[ans-2] [INFO] [1703311387.137743438] [ans]: 調和数列の和: 2.0833, 項:4
[ans-2] [INFO] [1703311387.637662354] [ans]: 調和数列の和: 2.2833, 項:5
[ans-2] [INFO] [1703311388.137743888] [ans]: 調和数列の和: 2.4500, 項:6
[ans-2] [INFO] [1703311388.637617207] [ans]: 調和数列の和: 2.5929, 項:7
[ans-2] [INFO] [1703311389.137980363] [ans]: 調和数列の和: 2.7179, 項:8
[ans-2] [INFO] [1703311389.637849372] [ans]: 調和数列の和: 2.8290, 項:9
[ans-2] [INFO] [1703311390.138064523] [ans]: 調和数列の和: 2.9290, 項:10
[ans-2] [INFO] [1703311390.637924997] [ans]: 調和数列の和: 3.0199, 項:11
[ans-2] [INFO] [1703311391.137774332] [ans]: 調和数列の和: 3.1032, 項:12
[ans-2] [INFO] [1703311391.637843385] [ans]: 調和数列の和: 3.1801, 項:13
[ans-2] [INFO] [1703311392.137766250] [ans]: 調和数列の和: 3.2516, 項:14
[ans-2] [INFO] [1703311392.637749765] [ans]: 調和数列の和: 3.3182, 項:15
[ans-2] [INFO] [1703311393.138027506] [ans]: 調和数列の和: 3.3807, 項:16
[ans-2] [INFO] [1703311393.638380285] [ans]: 調和数列の和: 3.4396, 項:17
[ans-2] [INFO] [1703311394.138219356] [ans]: 調和数列の和: 3.4951, 項:18
[ans-2] [INFO] [1703311394.637803603] [ans]: 調和数列の和: 3.5477, 項:19
[ans-2] [INFO] [1703311395.137999064] [ans]: 調和数列の和: 3.5977, 項:20
[ans-2] [INFO] [1703311395.638505198] [ans]: 調和数列の和: 3.6454, 項:21
[ans-2] [INFO] [1703311396.138098461] [ans]: 調和数列の和: 3.6908, 項:22
[ans-2] [INFO] [1703311396.637798923] [ans]: 調和数列の和: 3.7343, 項:23
                                     .
                                     .
                                     .

```
* 終了するときは`Ctrl+C`である。

# 必要なソフトウェア
* Python

# テスト環境
* Ubuntu 20.04
* ROS2 foxy

# 権利関係
* このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布および使用が許可されます。
* このパッケージのコードの一部は、下記のスライド（CC-BY-SA 4.0 by Ryuici Ueda)のものを本人の許可を得て自身の著作としたものです。
 * [ryuichiueda.github.io/my_slides/robosys_2022/lesson8](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8)
 * [ryuichiueda.github.io/my_slides/robosys_2022/lesson9](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson9)
 * [ryuichiueda.github.io/my_slides/robosys_2022/lesson10](https://ryuichiueda.github.io/my_slides/robosys_2022/lesson10)



* © 2023 Yuuki Tsubouchi
