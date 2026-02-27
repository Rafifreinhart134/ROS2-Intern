import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool # Gunakan interface standar

class StatusServer(Node):
    def __init__(self):
        super().__init__('service_server')
        self.srv = self.create_service(SetBool, 'get_status', self.get_status_callback)
        self.get_logger().info('Service Server /get_status is Ready')

    def get_status_callback(self, request, response):
        if request.data:
            response.success = True
            response.message = "Robot is Healthy and Running"
        else:
            response.success = False
            response.message = "Robot is Offline"
        return response

def main():
    rclpy.init()
    node = StatusServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()