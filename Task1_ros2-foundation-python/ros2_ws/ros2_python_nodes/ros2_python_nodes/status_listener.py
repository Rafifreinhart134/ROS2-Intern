import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StatusListener(Node):
    def __init__(self):
        super().__init__('status_listener')
        self.subscription = self.create_subscription(String, 'robot_status', self.callback, 10)
        self.get_logger().info('Status Listener Node has been started.')

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = StatusListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.init.shutdown()

if __name__ == '__main__':
    main()