import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool

class StatusClient(Node):
    def __init__(self):
        super().__init__('service_client')
        self.client = self.create_client(SetBool, 'get_status')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')
        self.req = SetBool.Request()

    def send_request(self, status):
        self.req.data = status
        return self.client.call_async(self.req)

def main():
    rclpy.init()
    node = StatusClient()
    future = node.send_request(True)
    rclpy.spin_until_future_complete(node, future)
    response = future.result()
    node.get_logger().info(f'Result: {response.message}')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()