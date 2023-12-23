# SPDX-FileCopyrightText: 2023 Yuuki Tsubouchi 　　　　　
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node                  #from person_msgs.msg import Person
from std_msgs.msg import Int16

def harmonic_series_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / i
    return total

def cb(msg):
    global node, sum_so_far, n_received #, received_terms
    sum_so_far += 1 / (n_received + 1)#msg.data  # 受け取った項を足し続ける
    #received_terms += 1
    n_received += 1
    # 調和数列の和をログに出力
    node.get_logger().info("調和数列の和: %.4f, 項:%d" % (sum_so_far, n_received))#"調和数列の和: %.4f, 項:%d" % (sum_so_far, msg.data))#f"項数: {received_terms}, 調和数列の和: {sum_so_far:.4f}")#("調和数列の和: %.4f" % sum_so_far)

rclpy.init()
node = Node("ans")
sum_so_far = 0  # 和を保持する変数
#received_terms = 0  # 受け取った項の数
n_received = 0

sub = node.create_subscription(Int16, "harmonic_sum", cb, 10)

rclpy.spin(node)

