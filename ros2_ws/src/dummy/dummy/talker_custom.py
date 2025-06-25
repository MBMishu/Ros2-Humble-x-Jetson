#!/usr/bin/env python
import rclpy
from rclpy.node import Node
import time
from custom_msgs.msg import CustomMsg  # Assuming you have a custom message defined


class TalkerNode(Node):
    def __init__(self):
        super().__init__('talker_node')
        self.publisher_ = self.create_publisher(CustomMsg, 'chatter', 10)
        

def main(args=None):
    rclpy.init(args=args)
    node = TalkerNode()
    counter = 0.0

    try:
        while rclpy.ok():
            msg = CustomMsg()
            msg.name = 'Hello mishu'
            msg.age = node.get_clock().now().to_msg().sec
            msg.score = counter
            counter += 1
            node.publisher_.publish(msg)
            node.get_logger().info(f'Publishing: "{msg.name}, {msg.age}, {msg.score}"')
            time.sleep(1)  # Sleep for 1 second
    except KeyboardInterrupt:
        pass
    
    finally:
        if rclpy.ok():
            rclpy.shutdown()
        node.destroy_node()
        print("ROS 2 node initialized and shut down successfully.")



if __name__ == '__main__':
    main()