1. What is ROS2?
ROS2 is a distributed communication framework designed for robotics development. Instead of running one monolithic program, ROS2 breaks down robot functions into smaller, modular units called Nodes.

2. Core Components
Based on the implementation in Task 1, we utilized the following components:
- Node: A running process that performs a specific task, such as status_publisher.
- Topic: A communication channel for continuous data streams between publishers and subscribers.
- Service: A request-response communication model used for quick, reactive tasks.
- Message: The standardized data format used to send information between nodes.

3. Communication Workflow
In the system built for this task:

- The Status Publisher node sends robot health data to the /robot_status topic.
- The Status Listener node subscribes to that topic to receive and print the data.
- The Service Server waits for requests on the /get_status service and provides an immediate reply to the Service Client.



IND
1. Apa itu ROS2?
ROS2 adalah framework komunikasi terdistribusi untuk pengembangan robotika. Berbeda dengan program tunggal yang besar, ROS2 membagi fungsi robot ke dalam modul-modul kecil yang disebut Nodes.

2. Komponen Utama
Berdasarkan implementasi pada Task 1, komponen yang digunakan adalah:

Node: Sebuah proses yang menjalankan tugas spesifik (misal: `status_publisher`).
Topic: Saluran komunikasi asinkron untuk aliran data kontinu (digunakan oleh Publisher dan Subscriber).
Service: Model komunikasi dua arah (Request-Response) untuk tugas jangka pendek (digunakan oleh Server dan Client).
Message: Format data standar (seperti `String` atau `SetBool`) yang dikirim antar node.

3. Alur Komunikasi
Dalam sistem yang dibangun:
1. Publisher Node mengirimkan status robot ke topik `/robot_status` secara berkala.
2. Subscriber Node mendengarkan topik tersebut dan memproses datanya.
3. Service Server menunggu permintaan pada service `/get_status` dan memberikan jawaban instan kepada Service Client.
