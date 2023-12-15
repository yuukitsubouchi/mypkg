import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

#class Talker():          #ヘッダの下にTalkerというクラスを作成
    #def __init__(self, node):#/https://ryuichiueda.github.io/my_slides/robosys_2022/lesson8.html#/5ode):  # オブジェクトを作ると呼ばれる関数
rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0
        #node.create_timer(0.5, self.cb) #ここでタイマーをしかける。
        # ↑ selfはオブジェクトのこと
        # ↑ オブジェクトにひとつパブリッシャと変数をもたせる。
def cb():          #17行目で定期実行されるコールバック関数
    global n       #関数を抜けてもnがリセットされないようにしている
    msg = Int16()  #メッセージの「オブジェクト」msg = Person()
    msg.data = n   #msgオブジェクトの持つdataにnを結び付け msg.name = "坪内優輝"
        #msg.age = n
    pub.publish(msg)        #pubの持つpublishでメッセージ送信
    n += 1

node.create_timer(0.5, cb)

#rclpy.init()
#node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
#talker = Talker(node) #処理のためにnodeを渡す。#pub = node.create_publisher(Int16, "countup", 10)   #パブリッシャのオブジェクト作成
rclpy.spin(node) #n = 0 #カウント用変数
#def cb():          #17行目で定期実行されるコールバック関数
    #global n       #関数を抜けてもnがリセットされないようにしている
#    msg = Int16()  #メッセージの「オブジェクト」msg = Person()
#    msg.data = talker.n   #msgオブジェクトの持つdataにnを結び付け msg.name = "坪内優輝"
    #msg.age = n
#    talker.pub.pblish(msg)        #pubの持つpublishでメッセージ送信
#    talker.n += 1
   
#node.create_timer(0.5, cb)  #タイマー設定
#rclpy.spin(node)   
