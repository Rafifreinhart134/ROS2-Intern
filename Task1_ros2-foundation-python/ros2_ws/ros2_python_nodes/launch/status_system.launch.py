from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_python_nodes',
            executable='status_publisher',
            name='publisher_node'
        ),
        Node(
            package='ros2_python_nodes',
            executable='status_listener',
            name='listener_node'
        ),
    ])