
FROM osrf/ros:jazzy-desktop

SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive

#  Instalar dependencias necesarias
RUN apt update && apt upgrade -y && apt install -y python3-colcon-common-extensions nano python3-pip python3-matplotlib
#  Crear el workspace y paquete base
WORKDIR /root/ros2_ws/src
RUN source /opt/ros/jazzy/setup.bash && \
    ros2 pkg create --build-type ament_python sensor_program --license MIT

#  Copiar los nodos Python al paquete
COPY ./nodes /nodes

RUN cp  /nodes/sensor_node.py /root/ros2_ws/src/sensor_program/sensor_program/sensor_node.py
RUN cp  /nodes/reader_node.py /root/ros2_ws/src/sensor_program/sensor_program/reader_node.py
RUN cp  /nodes/plotter_node.py /root/ros2_ws/src/sensor_program/sensor_program/plotter_node.py
RUN cp  /nodes/setup.py /root/ros2_ws/src/sensor_program/setup.py

#  Compilar el proyecto
WORKDIR /root/ros2_ws
RUN  source /opt/ros/jazzy/setup.bash && colcon build

#  Configurar entorno persistente
RUN echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc && \
    echo "source ~/ros2_ws/install/setup.bash" >> ~/.bashrc


# Copiar entrypoint de ROS 2
COPY --from=osrf/ros:jazzy-desktop /ros_entrypoint.sh /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["bash"]
