# ROS2 Taller 2 – Redes de Sensores (Docker)

Este proyecto implementa una red de sensores simulada en **ROS 2 (Jazzy)** dentro de un contenedor **Docker**.  
Incluye tres nodos principales:
- `sensor_node`: genera y publica datos de temperatura.
- `reader_node`: recibe los mensajes publicados.
- `plotter_node`: grafica los valores recibidos cada 5 segundos.

## Objetivo
Implementar un entorno dockerizado de ROS2 para simular una red de sensores, automatizarlo con Dockerfile,  
capturar su tráfico con `tcpdump` y analizarlo con Wireshark.

## Contenido del proyecto

taller2/
| - Guazhima_Sebastian_Taller2_WSN.pdf → informe del taller2 de Redes de sensores realizado
 
|- Dockerfile

|- nodes/ → Nodos en Python (.py)

|- data/ → Imágenes generadas (.png)

|- pcap/ → Capturas de tráfico (.pcap)



## Imagenes realizadas se encuentran disponible en DOCKER HUB

La imagen preconfigurada (del desarrollo paso a paso) se encuentra disponible en:

https://hub.docker.com/repository/docker/sebast15g/ros2_taller2_manual/general

Y la imagen del reto se encuentra disponible en:

https://hub.docker.com/repository/docker/sebast15g/ros2_taller2_reto/general



Autor

Sebastián Guazhima

Universidad de Cuenca – Ingeniería en Telecomunicaciones

