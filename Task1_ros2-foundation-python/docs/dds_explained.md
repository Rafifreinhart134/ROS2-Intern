DDS (DATA DISTRIBUTION SERVICE)
DDS is the network communication layer that acts as the backbone of ROS2, handling how messages are sent between nodes.

1. Why ROS2 Uses DDS
DDS was chosen because it provides an industrial standard for reliable, secure, and high-performance data exchange.

2. Key Features of DDS
Unlike previous versions of ROS, DDS offers several advanced capabilities:
- No Central Master: There is no single point of failure because nodes communicate peer-to-peer.
- Automatic Node Discovery: Nodes can find each other automatically on a network without manual configuration.
- Real-Time Capable: It is designed for time-critical applications where latency must be minimized.
- Quality of Service (QoS): It allows developers to configure if a message must be guaranteed to arrive or if only the latest data is needed.
- Multi-Machine Support: DDS works across multiple computers, allowing different parts of a robot to run on different hardware.

3. Importance in Task 1
DDS is the reason why our publisher and listener nodes could find each other instantly. It manages the discovery process and ensures the status messages are delivered efficiently across the system.


**(IND)**

DDS adalah "jantung" dari komunikasi ROS2. Ini adalah middleware yang menangani pengiriman pesan antar node di dalam jaringan.

 1. Mengapa ROS2 Menggunakan DDS?
DDS dipilih karena menyediakan standar industri untuk komunikasi data yang andal, aman, dan berkinerja tinggi.

 2. Fitur Utama DDS
Sesuai dengan keunggulan ROS2 dibandingkan versi sebelumnya:
- Tanpa entral Master: Tidak ada "ROS Master". Node bisa saling menemukan seara langsung (Peer-to-Peer), sehingga tidak ada titik kegagalan tunggal.
- Automati Disovery: Node baru yang bergabung dalam jaringan akan otomatis terdeteksi oleh node lain yang memiliki topik atau servie yang sama.
- Real-Time apable: DDS diranang untuk aplikasi yang membutuhkan waktu respon sangat epat dan terukur.
- Quality of Servie (QoS): Memungkinkan kita mengatur apakah pesan harus "Pasti Sampai" (Reliable) atau "ukup yang Terbaru" (Best-effort).
- Multi-Mahine Support: Memungkinkan komunikasi antar node yang berjalan di komputer atau robot yang berbeda selama berada dalam jaringan yang sama.

3. Peran dalam Task 1
DDS memungkinkan `status_publisher` dan `status_listener` untuk berkomunikasi tanpa kita harus mengatur alamat IP atau port seara manual. Semua proses "jabat tangan" antar node ditangani sepenuhnya oleh layer DDS ini.
