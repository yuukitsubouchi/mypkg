#!/bin/bash
# SPDX-FileCopyrightText: 2023 Yuuki Tsubouchi 　　　　　
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   #引数があったら、そちらをホームに変える。

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 30 ros2 launch mypkg suuretu_ans.launch.py > /tmp/mypkg.log
cat /tmp/mypkg.log |
grep '調和数列の和: 3.3182, 項:15' /tmp/mypkg.log
