import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ReaderNode(Node):
    def __init__(self):
        super().__init__('reader_node')
        # Suscripción al tópico sensor_data
        self.subscription = self.create_subscription(
            String, 'sensor_data', self.listener_callback, 10)
        self.subscription  # evitar warning de variable sin usar
        self.get_logger().info('Nodo Reader iniciado y escuchando sensor_data.')

    def listener_callback(self, msg):
        self.get_logger().info(f'Recibido: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = ReaderNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Nodo Reader detenido por el usuario.')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
