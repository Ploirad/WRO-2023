#Special Libraries                             #Functions
import Libraries.Motor as M            #movement(vel, dir, stop)
import Libraries.Ultrasonidos as US    #measure_distance(position)  -> distance
import Libraries.color_detector as cam #obtener_centroide()           -> green_area, red_area, magent_area, cv, cr, cm
import Libraries.Boton as B            #button_state()              -> True/False

#Variables
start = False #It says if the car have to start or not
run = True
Aparcar = False
vueltas = 0

#This distances are the distances of the ultrasounds sensors
frontal_distance = 0.0
right_distance = 0.0
left_distance = 0.0
back_distance = 0.0

#The areas detected by the camera
green_area = 0
red_area = 0
magenta_area = 0

#The position in the X edge of the centroids of the colors detected by the camera
green_centroid = 0
red_centroid = 0
magenta_centroid = 0

def update_variables():
  frontal_distance = US.measure_distance(1)
  right_distance = US.measure_distance(2)
  left_distance = US.measure_distance(4)
  back_distance = US.measure_distance(3)
  green_area, red_area, magenta_area, green_centroid, red_centroid, magenta_centroid = cam.obtener_centroide()

#640 _> 0-213-427-640
def aparcar():
  update_variables()

  if magenta_centroid < 213:
    M.movement(1, -1, False)
    while magenta_area > 0:
      update_variables()
      M.movement(1, 0, False)
    while back_distance > 2:
      update_variables()
      M.movement(-1, 1, False)
  
  else:
    M.movement(1, 1, False)
    while magenta_area > 0:
      update_variables()
      M.movement(1, 0, False)
    while back_distance > 2:
      update_variables()
      M.movement(-1, -1, False)

  M.movement(0, 0, True)
  run = False
  start = False
  Aparcar = False
  print("CAR STOPPED")

while run:
  if B.button_state():
    start = True
  
  if start:
    update_variables()

    if frontal_distance > 30:
      if right_distance < 10:
        M.movement(1, 1, False)
        last_direction = 1
        M.movement(1, 0, False)
      elif left_distance < 10:
        M.movement(1, -1, False)
        last_direction = -1
        M.movement(1, 0, False)
      else:
        M.movement(1, 0, False)

    elif frontal_distance > 10:
      if right_distance < 10:
        while frontal_distance < 25:
          update_variables()
          M.movement(1, 1, False)
          last_direction = 1
        M.movement(1, 0, False)

      elif left_distance < 10:
        while frontal_distance < 25:
          update_variables()
          M.movement(1, -1, False)
          last_direction = -1
        M.movement(1, 0, False)
      else:
        while frontal_distance < 25:
          update_variables()
          M.movement(1, -1, False)
        M.movement(1, 0, False)
    
    else:
      while frontal_distance < 10:
        update_variables()
        if right_distance > left_distance:
          while frontal_distance < 8:
            update_variables()
            M.movement(-1, -1, False)
          M.movement(1, 1, False)
        else:
          while frontal_distance < 8:
            update_variables()
            M.movement(-1, 1, False)
          M.movement(1, -1, False)
      M.movement(1, 0, False)
    
    if green_area > red_area:
      if green_area > 10000:
        M.movement(1, 1, False)
    
    else:
      if red_area > 10000:
        M.movement(1, -1, False)

    #AÑADIR AQUÍ EL DETECTOR TCS PARA SABER SI HEMOS DADO UNA VUELTA

    if vueltas == 3:
      if magenta_area > 10000:
        Aparcar = True
  
    while Aparcar:
        aparcar()