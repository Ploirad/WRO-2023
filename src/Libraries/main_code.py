import servo_lib.py as Servomotor
import ultrasound_lib.py as Us
import button.py as boton
import time

TRIG_pin_DELANTE = 23
ECHO_pin_DELANTE = 24
TRIG_pin_ATRAS = 17
ECHO_pin_ATRAS = 27
TRIG_pin_IZQUIERDA = 22
ECHO_pin_IZQUIERDA = 10
TRIG_pin_DERECHA = 5
ECHO_pin_DERECHA = 6
servo_pin_direccion = 2
servo_pin_traccion = 3

#VARIABLES
distancia_delante = 0
distancia_atras = 0
distancia_izquierda = 0
distancia_derecha = 0
v = 0

ultrasonidos = Us.Ultrasound(TRIG_pin_DELANTE, ECHO_pin_DELANTE, TRIG_pin_ATRAS, ECHO_pin_ATRAS, TRIG_pin_IZQUIERDA, ECHO_pin_IZQUIERDA, TRIG_pin_DERECHA, ECHO_pin_DERECHA)
servos = Servomotor.servos(servo_pin_traccion, servo_pin_direccion)

