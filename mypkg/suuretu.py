# SPDX-FileCopyrightText: 2023 Yuuki Tsubouchi 　　　　　
# SPDX-License-Identifier: BSD-3-Clause
import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

def harmonic_series_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / i
    return total

def cb():
    global n, sum_so_far
    sum_so_far =  harmonic_series_sum(n) #sum_so_far += 1 / n  # 調和数列の項を足し続ける
    msg = Int16()              
    msg.data = int(sum_so_far)    # 調和数列の和を計算してメッセージにセット
    pub.publish(msg)
    n += 1
    print(f"項数: {n - 1}, 調和数列の和: {sum_so_far:.4f}")# 項と和を表示
    #n += 1

rclpy.init()
node = Node("suuretu")
pub = node.create_publisher(Int16, "harmonic_sum", 10)
n = 1  # 最初の項から始める
#sum_so_far = 0  # 和を保持する変数

node.create_timer(0.5, cb)

rclpy.spin(node)


