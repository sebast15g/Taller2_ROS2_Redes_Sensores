import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        # Publicador en el tópico sensor_data
        self.publisher_ = self.create_publisher(String, 'sensor_data', 10)
        # Temporizador: ejecuta cada 1 segundo
        self.timer = self.create_timer(1.0, self.publish_data)
        self.get_logger().info('Nodo Sensor iniciado.')

    def publish_data(self):
        msg = String()
        temp = random.uniform(20.0, 30.0)
        msg.data = f"Temperatura: {temp:.2f} °C"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Nodo Sensor detenido por el usuario.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
