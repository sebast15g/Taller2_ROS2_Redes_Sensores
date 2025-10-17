import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import matplotlib.pyplot as plt
import time
import os

class PlotterNode(Node):
    def __init__(self):
        super().__init__('plotter_node')
        self.data = []
        self.timestamps = []
        self.subscription = self.create_subscription(
            String, 'sensor_data', self.listener_callback, 10)
        self.timer = self.create_timer(5.0, self.save_plot)
        self.get_logger().info('PlotterNode iniciado, esperando datos...')

    def listener_callback(self, msg):
        """Recibe los mensajes del nodo reader."""
        self.get_logger().info(f'Recibido: {msg.data}')
        try:
            value = float(msg.data.split(':')[1].split('°')[0].strip())
            self.data.append(value)
            self.timestamps.append(time.time())
        except:
            pass  # Ignora cualquier formato incorrecto

    def save_plot(self):
        """Genera el gráfico y lo guarda en la carpeta compartida."""
        if not self.data:
            return
        os.makedirs('/root/ros2_ws/data', exist_ok=True)
        plt.figure(figsize=(8, 4))
        plt.plot(self.data, color='orange', marker='o')
        plt.title('Temperatura recibida')
        plt.xlabel('Muestras')
        plt.ylabel('Temperatura (°C)')
        plt.grid(True)
        plt.tight_layout()
        path = '/root/ros2_ws/data/sensor_plot.png'
        plt.savefig(path)
        plt.close()
        self.get_logger().info(f'Gráfico guardado en {path}')

def main(args=None):
    rclpy.init(args=args)
    node = PlotterNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
