import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ros2_python_nodes'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rafifreinhart',
    maintainer_email='rafifreinhart@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'status_publisher = ros2_python_nodes.status_publisher:main',
            'status_listener = ros2_python_nodes.status_listener:main',
            'service_server = ros2_python_nodes.service_server:main',
            'service_client = ros2_python_nodes.service_client:main',
        ],
    },
)
