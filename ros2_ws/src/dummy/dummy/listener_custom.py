#!/usr/bin/env python
import rclpy
from rclpy.node import Node
import time
from custom_msgs.msg import CustomMsg  # Assuming you have a custom message defined

class ListenerNode(Node):
    def __init__(self):
        super().__init__('listener_node')  # Initialize the node with a name
        self.subscription = self.create_subscription(
            CustomMsg,               # Message type
            'chatter',            # Topic name (must match publisher)
            self.listener_callback,  # Function to call when a message is received
            10                   # Queue size (number of buffered messages)
        )
        self.subscription  # prevents unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg}"')  # Log received message

def main(args=None):
    rclpy.init(args=args)          # Initialize ROS 2
    node = ListenerNode()          # Create an instance of the node
    rclpy.spin(node)               # Keep the node running to receive messages
    node.destroy_node()            # Clean up node resources
    rclpy.shutdown()               # Shutdown ROS 2

if __name__ == '__main__':
    main()
