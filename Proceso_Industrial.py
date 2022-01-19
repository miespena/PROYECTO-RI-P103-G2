#Proyecto Laboratorio de Robótica Industrial
#Docente: Ing. María José Prado
#Integrantes del grupo: Henry Puhueyestewa - Miguel Espinoza
#Proyecto: Pintado de Objetos
#Paralelo 103

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#ChooseColors¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations

PARAM_COLOR_OBJECT = 'ColorObject' 
RDK = Robolink()
color_object = RDK.getParam(PARAM_COLOR_OBJECT)

color_object_input = mbox('Enter the number that contains the color to paint the objects: 1. Red, 2. Green, 3. Blue, 4. Pink', entry=color_object)
if color_object_input:
    RDK.setParam(PARAM_COLOR_OBJECT, color_object_input)
else:
    raise Exception('Operation cancelled by user')

color=int(color_object_input)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Asignación de variables y robots¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Se asignan variables a los objetos
toola = 'RobotiQ Sanding Kit'
toolb = 'Paint gun'
objecta = 'Pieza1'
objectb = 'Pieza2' 
objectc = 'Pieza3'
objectd = 'Pieza4'
objecte = 'Pieza5'   
mesa2 = 'MesaB'
mesa3 = 'MesaA1'
gripper1 = RDK.Item(toola, ITEM_TYPE_TOOL)
gripper2 = RDK.Item(toolb, ITEM_TYPE_TOOL)
pi1 = RDK.Item(objecta, ITEM_TYPE_OBJECT)
pi2 = RDK.Item(objectb, ITEM_TYPE_OBJECT)
pi3 = RDK.Item(objectc, ITEM_TYPE_OBJECT)
pi4 = RDK.Item(objectd, ITEM_TYPE_OBJECT)
pi5 = RDK.Item(objecte, ITEM_TYPE_OBJECT)
mesapaint = RDK.Item(mesa2, ITEM_TYPE_OBJECT)
mesafinal = RDK.Item(mesa3, ITEM_TYPE_OBJECT)

#Con respecto a RobotA
robotA = RDK.Item('RobotA',ITEM_TYPE_ROBOT)
if not robotA.Valid():
    quit()  
reference = robotA.Parent()
robotA.setPoseFrame(reference)
pose_ref = robotA.Pose()
print(Pose_2_TxyzRxyz(pose_ref))
home_joints = robotA.JointsHome().tolist()

#Con respecto a RobotB
robotB = RDK.Item('RobotB',ITEM_TYPE_ROBOT)
if not robotB.Valid():
    quit()   
reference1 = robotB.Parent()
robotB.setPoseFrame(reference1)
pose_ref1 = robotB.Pose()
print(Pose_2_TxyzRxyz(pose_ref1))
home_joints1 = robotB.JointsHome().tolist()

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Limpio a pintura anterior¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
RDK.Spray_Clear()               #Limpio la pintura
pi1.Recolor([0.90,0.91,0.96,1]) #La pieza inicia blanca
pi2.Recolor([0.90,0.91,0.96,1]) #La pieza inicia blanca
pi3.Recolor([0.90,0.91,0.96,1]) #La pieza inicia blanca
pi4.Recolor([0.90,0.91,0.96,1]) #La pieza inicia blanca
pi5.Recolor([0.90,0.91,0.96,1]) #La pieza inicia blanca

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Process_Pieza1¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pick and Place en area de trabajo A0
#RobotA se aproxima a MesaA0 para recoger la pieza
aprox=20
a1 = transl(1323.030,955.182,93.068)*roty(pi)
robotA.MoveJ(a1)
robotA.setSpeed(1000)
#RobotA toma la pieza1 de la MesaA0 
b1 = transl(1323.030,956.483,-220.350)*roty(pi)
robotA.MoveJ(b1)
robotA.setSpeed(1000)
pi1.setParentStatic(gripper1)
#RobotA lleva la pieza1 cerca de la MesaB
c1=transl(-1417.075,4.293,400.446)*roty(pi)
robotA.MoveJ(c1)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaB
d1=transl(-1417.075,4.293,100.367)*roty(pi)
robotA.MoveJ(d1)
robotA.setSpeed(1000)
gripper1.DetachAll()
pi1.setParentStatic(mesapaint)
#RobotA se ubica en la posición de espera
e1=transl(-643.019,4.293,741.529)*roty(pi)
robotA.MoveJ(e1)
robotA.setSpeed(1000)
#RobotB se aproxima a MesaB
aprox=20
a02 = xyzrpw_2_pose([951.091,-99.100,515.373,90.000,-60.175,-173.197])
robotB.MoveJ(a02)
robotB.setSpeed(100)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#SprayOn1¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
Tool_Name = 'Paint gun'
Object_Name = 'Pieza1'

# Define the default action (0 to deactivate, +1 to activate, -1 to clear any spray gun simulation)
# Setting it to None will display a message
ACTION = +1

# quit if we are not in simulation mode
if RDK.RunMode() != RUNMODE_SIMULATE:
    quit()

# Get any previously added spray gun simulations and display statistics (spray on the part vs spray falling out of the part)
info, data = RDK.Spray_GetStats()
if data.size(1) > 0:
    print("Spray gun statistics:")
    print(info)
    print(data.tr())
    RDK.Spray_Clear() 

# Check if we are running this program inside another program and passing arguments
import sys
if len(sys.argv) > 1:
    ACTION = int(sys.argv[1])

# If the default ACTION is None, display a message to activate/deactivate the spray gun
if ACTION is None:
    print('Note: This macro can be called as Spray(1) or SprayOn(0)')
    entry = mbox('Turn gun ON or OFF', ('On', '1'), ('Off', '0'))
    if not entry:
        quit()
    ACTION = int(entry)    

if ACTION == 0:
    # Turn the gun off
    RDK.Spray_SetState(SPRAY_OFF)
    
elif ACTION < 0:
    # Clear all spray simulations (same as pressing ESC key)
    RDK.Spray_Clear()
    
elif ACTION > 0:
   
    tool = 0    # auto detect active tool
    obj = 0     # auto detect object in active reference frame
    if Tool_Name is not None:
        tool = RDK.Item(Tool_Name, ITEM_TYPE_TOOL)
    
    if Object_Name is not None:
        obj = RDK.Item(Object_Name, ITEM_TYPE_OBJECT)

    #options_command = "ELLYPSE PROJECT PARTICLE=SPHERE(4,8,1,1,0.5) STEP=8x8 RAND=2" # simulate 
    options_command = "PARTICLE=CUBE(10,10,2) STEP=8x8"

    # Another example with a varying rectancular shape
    # define the rectangular volume as p0, pA, pB, colorRGBA (close and far)
    if color == 1:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       1,0,0,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)
    
    if color == 2:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       0,1,0,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)
    
    if color == 3:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       0,0,1,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)

    if color == 4:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       1,0,1,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#PP1_A¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pintado en area de trabajo B
#RobotB pinta pieza1, lado derecho 
aprox=20
a2 = xyzrpw_2_pose([1128.463,-77.940,203.783,90.000,-60.175,-173.197])
robotB.MoveJ(a2)
robotB.setSpeed(100)
c2 = xyzrpw_2_pose([1071.476,-84.739,225.057,90.000,-60.175,-173.197])
robotB.MoveJ(c2)
robotB.setSpeed(1000)
d2 = xyzrpw_2_pose([1002.267,-92.996,254.878,90.000,-60.175,-173.197])
robotB.MoveJ(d2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, centro 
e2 = xyzrpw_2_pose([1011.397,-39.866,300.368,180.000,0.000,-173.197])
robotB.MoveJ(e2)
robotB.setSpeed(1000)
f2 = xyzrpw_2_pose([1050.893,5.934,300.367,180.000,0.000,-173.197])
robotB.MoveJ(f2)
robotB.setSpeed(1000)
g2 = xyzrpw_2_pose([1079.262,49.092,300.367,180.000,0.000,-173.197])
robotB.MoveJ(g2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, lado izquierdo 
h2 = xyzrpw_2_pose([1098.260,69.520,285.711,-90.000,0.000,-173.197])
robotB.MoveJ(h2)
robotB.setSpeed(1000)
i2 = xyzrpw_2_pose([1048.722,63.609,234.840,-90.000,0.000,-173.197])
robotB.MoveJ(i2)
robotB.setSpeed(1000)
j2 = xyzrpw_2_pose([1007.902,58.739,193.572,-90.000,0.000,-173.197])
robotB.MoveJ(j2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, frente 
k2 = xyzrpw_2_pose([972.738,-18.594,202.789,0.000,-90.000,-173.197])
robotB.MoveJ(k2)
robotB.setSpeed(1000)
l2 = xyzrpw_2_pose([973.710,-26.748,277.710,0.000,-90.000,-173.197])
robotB.MoveJ(l2)
robotB.setSpeed(1000)
#RobotB se mueve a la posición de home
b2 = xyzrpw_2_pose([670.544,0.000,1022.351,0.000,-60.000,-180.000])
robotB.MoveJ(b2)
robotB.setSpeed(100)
#Color
if color == 1:    
    pi1.Recolor([1,0,0,1])
if color == 2:    
    pi1.Recolor([0,1,0,1])
if color == 3:    
    pi1.Recolor([0,0,1,1])
if color == 4:    
    pi1.Recolor([1,0,1,1])

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#PP1_B¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pick and Place en area de trabajo A1
#RobotA toma la pieza1 de la MesaB
a3=transl(-1417.075,4.293,100.367)*roty(pi)
robotA.MoveJ(a3)
robotA.setSpeed(1000)
mesapaint.DetachAll()
pi1.setParentStatic(gripper1)
#RobotA lleva la pieza1 lejos de la MesaB
b3=transl(-1417.075,4.293,400.446)*roty(pi)
robotA.MoveJ(b3)
robotA.setSpeed(1000)
#RobotA lleva la pieza1 entre MesaB y MesaA1
f3=transl(1323.030,955.182,93.068)*roty(pi)
robotA.MoveJ(f3)
robotA.setSpeed(1000)
#RobotA lleva la pieza1 cerca de la MesaA1
c3=transl(1323.030,-935.107,93.068)*roty(pi)
robotA.MoveJ(c3)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaA1
d3=transl(1323.030,-933.806,-220.350)*roty(pi)
robotA.MoveJ(d3)
robotA.setSpeed(1000)
gripper1.DetachAll()
pi1.setParentStatic(mesafinal)
#RobotA se mueve a la posición de home
e3=transl(945.000,0.000,834.135)*roty(pi)
robotA.MoveJ(e3)
robotA.setSpeed(1000)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Process_Pieza2¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pick and Place en area de trabajo A0
#RobotA se aproxima a MesaA0 para recoger la pieza
aprox=20
a1 = transl(1323.030,780.657,93.068)*roty(pi)      #Se cambia respecto a AproxMesaA0_P________________________
robotA.MoveJ(a1)
robotA.setSpeed(1000)
#RobotA toma la pieza1 de la MesaA0 
b1 = transl(1323.030,780.657,-220.350)*roty(pi)    #Se cambia respecto a Take_P________________________
robotA.MoveJ(b1)
robotA.setSpeed(1000)
pi2.setParentStatic(gripper1)                      #Se cambia el pi_____________________________________
#RobotA lleva la pieza1 cerca de la MesaB
c1=transl(-1417.075,4.293,400.446)*roty(pi)
robotA.MoveJ(c1)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaB
d1=transl(-1417.075,4.293,100.367)*roty(pi)
robotA.MoveJ(d1)
robotA.setSpeed(1000)
gripper1.DetachAll()
pi2.setParentStatic(mesapaint)                     #Se cambia el pi_____________________________________
#RobotA se ubica en la posición de espera
e1=transl(-643.019,4.293,741.529)*roty(pi)
robotA.MoveJ(e1)
robotA.setSpeed(1000)
#RobotB se aproxima a MesaB
aprox=20
a02 = xyzrpw_2_pose([951.091,-99.100,515.373,90.000,-60.175,-173.197])
robotB.MoveJ(a02)
robotB.setSpeed(100)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#SprayOn2¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
Tool_Name = 'Paint gun'
Object_Name = 'Pieza2'

# Define the default action (0 to deactivate, +1 to activate, -1 to clear any spray gun simulation)
# Setting it to None will display a message
ACTION = +1

# quit if we are not in simulation mode
if RDK.RunMode() != RUNMODE_SIMULATE:
    quit()

# Get any previously added spray gun simulations and display statistics (spray on the part vs spray falling out of the part)
info, data = RDK.Spray_GetStats()
if data.size(1) > 0:
    print("Spray gun statistics:")
    print(info)
    print(data.tr())
    RDK.Spray_Clear() 

# Check if we are running this program inside another program and passing arguments
import sys
if len(sys.argv) > 1:
    ACTION = int(sys.argv[1])

# If the default ACTION is None, display a message to activate/deactivate the spray gun
if ACTION is None:
    print('Note: This macro can be called as Spray(1) or SprayOn(0)')
    entry = mbox('Turn gun ON or OFF', ('On', '1'), ('Off', '0'))
    if not entry:
        quit()
    ACTION = int(entry)    

if ACTION == 0:
    # Turn the gun off
    RDK.Spray_SetState(SPRAY_OFF)
    
elif ACTION < 0:
    # Clear all spray simulations (same as pressing ESC key)
    RDK.Spray_Clear()
    
elif ACTION > 0:
   
    tool = 0    # auto detect active tool
    obj = 0     # auto detect object in active reference frame
    if Tool_Name is not None:
        tool = RDK.Item(Tool_Name, ITEM_TYPE_TOOL)
    
    if Object_Name is not None:
        obj = RDK.Item(Object_Name, ITEM_TYPE_OBJECT)

    #options_command = "ELLYPSE PROJECT PARTICLE=SPHERE(4,8,1,1,0.5) STEP=8x8 RAND=2" # simulate 
    options_command = "PARTICLE=CUBE(10,10,2) STEP=8x8"

    # Another example with a varying rectancular shape
    # define the rectangular volume as p0, pA, pB, colorRGBA (close and far)
    if color == 1:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       1,0,0,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)
    
    if color == 2:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       0,1,0,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)
    
    if color == 3:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       0,0,1,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)

    if color == 4:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       1,0,1,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#PP2_A¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pintado en area de trabajo B
#RobotB pinta pieza1, lado derecho 
aprox=20
a2 = xyzrpw_2_pose([1128.463,-77.940,203.783,90.000,-60.175,-173.197])
robotB.MoveJ(a2)
robotB.setSpeed(100)
c2 = xyzrpw_2_pose([1071.476,-84.739,225.057,90.000,-60.175,-173.197])
robotB.MoveJ(c2)
robotB.setSpeed(1000)
d2 = xyzrpw_2_pose([1002.267,-92.996,254.878,90.000,-60.175,-173.197])
robotB.MoveJ(d2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, centro 
e2 = xyzrpw_2_pose([1011.397,-39.866,300.368,180.000,0.000,-173.197])
robotB.MoveJ(e2)
robotB.setSpeed(1000)
f2 = xyzrpw_2_pose([1050.893,5.934,300.367,180.000,0.000,-173.197])
robotB.MoveJ(f2)
robotB.setSpeed(1000)
g2 = xyzrpw_2_pose([1079.262,49.092,300.367,180.000,0.000,-173.197])
robotB.MoveJ(g2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, lado izquierdo 
h2 = xyzrpw_2_pose([1098.260,69.520,285.711,-90.000,0.000,-173.197])
robotB.MoveJ(h2)
robotB.setSpeed(1000)
i2 = xyzrpw_2_pose([1048.722,63.609,234.840,-90.000,0.000,-173.197])
robotB.MoveJ(i2)
robotB.setSpeed(1000)
j2 = xyzrpw_2_pose([1007.902,58.739,193.572,-90.000,0.000,-173.197])
robotB.MoveJ(j2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, frente 
k2 = xyzrpw_2_pose([972.738,-18.594,202.789,0.000,-90.000,-173.197])
robotB.MoveJ(k2)
robotB.setSpeed(1000)
l2 = xyzrpw_2_pose([973.710,-26.748,277.710,0.000,-90.000,-173.197])
robotB.MoveJ(l2)
robotB.setSpeed(1000)
#RobotB se mueve a la posición de home
b2 = xyzrpw_2_pose([670.544,0.000,1022.351,0.000,-60.000,-180.000])
robotB.MoveJ(b2)
robotB.setSpeed(100)
#Color
if color == 1:    
    pi2.Recolor([1,0,0,1])
if color == 2:    
    pi2.Recolor([0,1,0,1])
if color == 3:    
    pi2.Recolor([0,0,1,1])
if color == 4:    
    pi2.Recolor([1,0,1,1])

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#PP2_B¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pick and Place en area de trabajo A1
#RobotA toma la pieza1 de la MesaB
a3=transl(-1417.075,4.293,100.367)*roty(pi)
robotA.MoveJ(a3)
robotA.setSpeed(1000)
mesapaint.DetachAll()
pi2.setParentStatic(gripper1)                          #Se cambia el pi_____________________________________
#RobotA lleva la pieza1 lejos de la MesaB
b3=transl(-1417.075,4.293,400.446)*roty(pi)
robotA.MoveJ(b3)
robotA.setSpeed(1000)
#RobotA lleva la pieza1 entre MesaB y MesaA1
f3=transl(1323.030,780.657,93.068)*roty(pi)            #Se cambia el AproxMesaA0_P_____________________________________
robotA.MoveJ(f3)
robotA.setSpeed(1000)
#RobotA lleva la pieza1 cerca de la MesaA1             
c3=transl(1323.030,-761.529,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(c3)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaA1
d3=transl(1323.030,-760.228,-220.350)*roty(pi)        #Se cambia respecto a Left_P________________________
robotA.MoveJ(d3)
robotA.setSpeed(1000)
gripper1.DetachAll()
pi2.setParentStatic(mesafinal)                        #Se cambia el pi_____________________________________
#RobotA se mueve a la posición de home
e3=transl(945.000,0.000,834.135)*roty(pi)
robotA.MoveJ(e3)
robotA.setSpeed(1000)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Process_Pieza3¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pick and Place en area de trabajo A0
#RobotA se aproxima a MesaA0 para recoger la pieza
aprox=20
a1 = transl(1323.030,606.483,93.068)*roty(pi)      #Se cambia respecto a AproxMesaA0_P________________________
robotA.MoveJ(a1)
robotA.setSpeed(1000)
#RobotA toma la pieza1 de la MesaA0 
b1 = transl(1323.030,606.483,-220.350)*roty(pi)    #Se cambia respecto a Take_P________________________
robotA.MoveJ(b1)
robotA.setSpeed(1000)
pi3.setParentStatic(gripper1)                      #Se cambia el pi_____________________________________
#RobotA lleva la pieza1 cerca de la MesaB
c1=transl(-1417.075,4.293,400.446)*roty(pi)
robotA.MoveJ(c1)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaB
d1=transl(-1417.075,4.293,100.367)*roty(pi)
robotA.MoveJ(d1)
robotA.setSpeed(1000)
gripper1.DetachAll()
pi3.setParentStatic(mesapaint)                     #Se cambia el pi_____________________________________
#RobotA se ubica en la posición de espera
e1=transl(-643.019,4.293,741.529)*roty(pi)
robotA.MoveJ(e1)
robotA.setSpeed(1000)
#RobotB se aproxima a MesaB
aprox=20
a02 = xyzrpw_2_pose([951.091,-99.100,515.373,90.000,-60.175,-173.197])
robotB.MoveJ(a02)
robotB.setSpeed(100)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#SprayOn3¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
Tool_Name = 'Paint gun'
Object_Name = 'Pieza3'

# Define the default action (0 to deactivate, +1 to activate, -1 to clear any spray gun simulation)
# Setting it to None will display a message
ACTION = +1

# quit if we are not in simulation mode
if RDK.RunMode() != RUNMODE_SIMULATE:
    quit()

# Get any previously added spray gun simulations and display statistics (spray on the part vs spray falling out of the part)
info, data = RDK.Spray_GetStats()
if data.size(1) > 0:
    print("Spray gun statistics:")
    print(info)
    print(data.tr())
    RDK.Spray_Clear() 

# Check if we are running this program inside another program and passing arguments
import sys
if len(sys.argv) > 1:
    ACTION = int(sys.argv[1])

# If the default ACTION is None, display a message to activate/deactivate the spray gun
if ACTION is None:
    print('Note: This macro can be called as Spray(1) or SprayOn(0)')
    entry = mbox('Turn gun ON or OFF', ('On', '1'), ('Off', '0'))
    if not entry:
        quit()
    ACTION = int(entry)    

if ACTION == 0:
    # Turn the gun off
    RDK.Spray_SetState(SPRAY_OFF)
    
elif ACTION < 0:
    # Clear all spray simulations (same as pressing ESC key)
    RDK.Spray_Clear()
    
elif ACTION > 0:
   
    tool = 0    # auto detect active tool
    obj = 0     # auto detect object in active reference frame
    if Tool_Name is not None:
        tool = RDK.Item(Tool_Name, ITEM_TYPE_TOOL)
    
    if Object_Name is not None:
        obj = RDK.Item(Object_Name, ITEM_TYPE_OBJECT)

    #options_command = "ELLYPSE PROJECT PARTICLE=SPHERE(4,8,1,1,0.5) STEP=8x8 RAND=2" # simulate 
    options_command = "PARTICLE=CUBE(10,10,2) STEP=8x8"

    # Another example with a varying rectancular shape
    # define the rectangular volume as p0, pA, pB, colorRGBA (close and far)
    if color == 1:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       1,0,0,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)
    
    if color == 2:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       0,1,0,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)
    
    if color == 3:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       0,0,1,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)

    if color == 4:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       1,0,1,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#PP3_A¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pintado en area de trabajo B
#RobotB pinta pieza1, lado derecho 
aprox=20
a2 = xyzrpw_2_pose([1128.463,-77.940,203.783,90.000,-60.175,-173.197])
robotB.MoveJ(a2)
robotB.setSpeed(100)
c2 = xyzrpw_2_pose([1071.476,-84.739,225.057,90.000,-60.175,-173.197])
robotB.MoveJ(c2)
robotB.setSpeed(1000)
d2 = xyzrpw_2_pose([1002.267,-92.996,254.878,90.000,-60.175,-173.197])
robotB.MoveJ(d2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, centro 
e2 = xyzrpw_2_pose([1011.397,-39.866,300.368,180.000,0.000,-173.197])
robotB.MoveJ(e2)
robotB.setSpeed(1000)
f2 = xyzrpw_2_pose([1050.893,5.934,300.367,180.000,0.000,-173.197])
robotB.MoveJ(f2)
robotB.setSpeed(1000)
g2 = xyzrpw_2_pose([1079.262,49.092,300.367,180.000,0.000,-173.197])
robotB.MoveJ(g2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, lado izquierdo 
h2 = xyzrpw_2_pose([1098.260,69.520,285.711,-90.000,0.000,-173.197])
robotB.MoveJ(h2)
robotB.setSpeed(1000)
i2 = xyzrpw_2_pose([1048.722,63.609,234.840,-90.000,0.000,-173.197])
robotB.MoveJ(i2)
robotB.setSpeed(1000)
j2 = xyzrpw_2_pose([1007.902,58.739,193.572,-90.000,0.000,-173.197])
robotB.MoveJ(j2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, frente 
k2 = xyzrpw_2_pose([972.738,-18.594,202.789,0.000,-90.000,-173.197])
robotB.MoveJ(k2)
robotB.setSpeed(1000)
l2 = xyzrpw_2_pose([973.710,-26.748,277.710,0.000,-90.000,-173.197])
robotB.MoveJ(l2)
robotB.setSpeed(1000)
#RobotB se mueve a la posición de home
b2 = xyzrpw_2_pose([670.544,0.000,1022.351,0.000,-60.000,-180.000])
robotB.MoveJ(b2)
robotB.setSpeed(100)
#Color
if color == 1:    
    pi3.Recolor([1,0,0,1])
if color == 2:    
    pi3.Recolor([0,1,0,1])
if color == 3:    
    pi3.Recolor([0,0,1,1])
if color == 4:    
    pi3.Recolor([1,0,1,1])

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#PP3_B¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pick and Place en area de trabajo A1
#RobotA toma la pieza1 de la MesaB
a3=transl(-1417.075,4.293,100.367)*roty(pi)
robotA.MoveJ(a3)
robotA.setSpeed(1000)
mesapaint.DetachAll()
pi3.setParentStatic(gripper1)                          #Se cambia el pi_____________________________________
#RobotA lleva la pieza1 lejos de la MesaB
b3=transl(-1417.075,4.293,400.446)*roty(pi)
robotA.MoveJ(b3)
robotA.setSpeed(1000)
#RobotA lleva la pieza1 entre MesaB y MesaA1
f3=transl(1323.030,606.483,93.068)*roty(pi)            #Se cambia el AproxMesaA0_P_____________________________________
robotA.MoveJ(f3)
robotA.setSpeed(1000)
#RobotA lleva la pieza1 cerca de la MesaA1             
c3=transl(1323.030,-585.913,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(c3)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaA1
d3=transl(1323.030,-584.612,-220.350)*roty(pi)        #Se cambia respecto a Left_P________________________
robotA.MoveJ(d3)
robotA.setSpeed(1000)
gripper1.DetachAll()
pi3.setParentStatic(mesafinal)                        #Se cambia el pi_____________________________________
#RobotA se mueve a la posición de home
e3=transl(945.000,0.000,834.135)*roty(pi)
robotA.MoveJ(e3)
robotA.setSpeed(1000)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Process_Pieza4¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pick and Place en area de trabajo A0
#RobotA se aproxima a MesaA0 para recoger la pieza
aprox=20
a1 = transl(1323.030,430.867,93.068)*roty(pi)      #Se cambia respecto a AproxMesaA0_P________________________
robotA.MoveJ(a1)
robotA.setSpeed(1000)
#RobotA toma la pieza1 de la MesaA0 
b1 = transl(1323.030,430.867,-220.350)*roty(pi)    #Se cambia respecto a Take_P________________________
robotA.MoveJ(b1)
robotA.setSpeed(1000)
pi4.setParentStatic(gripper1)                      #Se cambia el pi_____________________________________
#RobotA lleva la pieza1 cerca de la MesaB
c1=transl(-1417.075,4.293,400.446)*roty(pi)
robotA.MoveJ(c1)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaB
d1=transl(-1417.075,4.293,100.367)*roty(pi)
robotA.MoveJ(d1)
robotA.setSpeed(1000)
gripper1.DetachAll()
pi4.setParentStatic(mesapaint)                     #Se cambia el pi_____________________________________
#RobotA se ubica en la posición de espera
e1=transl(-643.019,4.293,741.529)*roty(pi)
robotA.MoveJ(e1)
robotA.setSpeed(1000)
#RobotB se aproxima a MesaB
aprox=20
a02 = xyzrpw_2_pose([951.091,-99.100,515.373,90.000,-60.175,-173.197])
robotB.MoveJ(a02)
robotB.setSpeed(100)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#SprayOn4¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
Tool_Name = 'Paint gun'
Object_Name = 'Pieza4'

# Define the default action (0 to deactivate, +1 to activate, -1 to clear any spray gun simulation)
# Setting it to None will display a message
ACTION = +1

# quit if we are not in simulation mode
if RDK.RunMode() != RUNMODE_SIMULATE:
    quit()

# Get any previously added spray gun simulations and display statistics (spray on the part vs spray falling out of the part)
info, data = RDK.Spray_GetStats()
if data.size(1) > 0:
    print("Spray gun statistics:")
    print(info)
    print(data.tr())
    RDK.Spray_Clear() 

# Check if we are running this program inside another program and passing arguments
import sys
if len(sys.argv) > 1:
    ACTION = int(sys.argv[1])

# If the default ACTION is None, display a message to activate/deactivate the spray gun
if ACTION is None:
    print('Note: This macro can be called as Spray(1) or SprayOn(0)')
    entry = mbox('Turn gun ON or OFF', ('On', '1'), ('Off', '0'))
    if not entry:
        quit()
    ACTION = int(entry)    

if ACTION == 0:
    # Turn the gun off
    RDK.Spray_SetState(SPRAY_OFF)
    
elif ACTION < 0:
    # Clear all spray simulations (same as pressing ESC key)
    RDK.Spray_Clear()
    
elif ACTION > 0:
   
    tool = 0    # auto detect active tool
    obj = 0     # auto detect object in active reference frame
    if Tool_Name is not None:
        tool = RDK.Item(Tool_Name, ITEM_TYPE_TOOL)
    
    if Object_Name is not None:
        obj = RDK.Item(Object_Name, ITEM_TYPE_OBJECT)

    #options_command = "ELLYPSE PROJECT PARTICLE=SPHERE(4,8,1,1,0.5) STEP=8x8 RAND=2" # simulate 
    options_command = "PARTICLE=CUBE(10,10,2) STEP=8x8"

    # Another example with a varying rectancular shape
    # define the rectangular volume as p0, pA, pB, colorRGBA (close and far)
    if color == 1:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       1,0,0,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)
    
    if color == 2:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       0,1,0,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)
    
    if color == 3:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       0,0,1,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)

    if color == 4:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       1,0,1,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#PP4_A¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pintado en area de trabajo B
#RobotB pinta pieza1, lado derecho 
aprox=20
a2 = xyzrpw_2_pose([1128.463,-77.940,203.783,90.000,-60.175,-173.197])
robotB.MoveJ(a2)
robotB.setSpeed(100)
c2 = xyzrpw_2_pose([1071.476,-84.739,225.057,90.000,-60.175,-173.197])
robotB.MoveJ(c2)
robotB.setSpeed(1000)
d2 = xyzrpw_2_pose([1002.267,-92.996,254.878,90.000,-60.175,-173.197])
robotB.MoveJ(d2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, centro 
e2 = xyzrpw_2_pose([1011.397,-39.866,300.368,180.000,0.000,-173.197])
robotB.MoveJ(e2)
robotB.setSpeed(1000)
f2 = xyzrpw_2_pose([1050.893,5.934,300.367,180.000,0.000,-173.197])
robotB.MoveJ(f2)
robotB.setSpeed(1000)
g2 = xyzrpw_2_pose([1079.262,49.092,300.367,180.000,0.000,-173.197])
robotB.MoveJ(g2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, lado izquierdo 
h2 = xyzrpw_2_pose([1098.260,69.520,285.711,-90.000,0.000,-173.197])
robotB.MoveJ(h2)
robotB.setSpeed(1000)
i2 = xyzrpw_2_pose([1048.722,63.609,234.840,-90.000,0.000,-173.197])
robotB.MoveJ(i2)
robotB.setSpeed(1000)
j2 = xyzrpw_2_pose([1007.902,58.739,193.572,-90.000,0.000,-173.197])
robotB.MoveJ(j2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, frente 
k2 = xyzrpw_2_pose([972.738,-18.594,202.789,0.000,-90.000,-173.197])
robotB.MoveJ(k2)
robotB.setSpeed(1000)
l2 = xyzrpw_2_pose([973.710,-26.748,277.710,0.000,-90.000,-173.197])
robotB.MoveJ(l2)
robotB.setSpeed(1000)
#RobotB se mueve a la posición de home
b2 = xyzrpw_2_pose([670.544,0.000,1022.351,0.000,-60.000,-180.000])
robotB.MoveJ(b2)
robotB.setSpeed(100)
#Color
if color == 1:    
    pi4.Recolor([1,0,0,1])
if color == 2:    
    pi4.Recolor([0,1,0,1])
if color == 3:    
    pi4.Recolor([0,0,1,1])
if color == 4:    
    pi4.Recolor([1,0,1,1])

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#PP4_B¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pick and Place en area de trabajo A1
#RobotA toma la pieza1 de la MesaB
a3=transl(-1417.075,4.293,100.367)*roty(pi)
robotA.MoveJ(a3)
robotA.setSpeed(1000)
mesapaint.DetachAll()
pi4.setParentStatic(gripper1)                          #Se cambia el pi_____________________________________
#RobotA lleva la pieza1 lejos de la MesaB
b3=transl(-1417.075,4.293,400.446)*roty(pi)
robotA.MoveJ(b3)
robotA.setSpeed(1000)
#RobotA lleva la pieza1 entre MesaB y MesaA1
f3=transl(1323.030,430.867,93.068)*roty(pi)            #Se cambia el AproxMesaA0_P_____________________________________
robotA.MoveJ(f3)
robotA.setSpeed(1000)
#RobotA lleva la pieza1 cerca de la MesaA1             
c3=transl(1323.030,-411.739,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(c3)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaA1
d3=transl(1323.030,-410.438,-220.350)*roty(pi)        #Se cambia respecto a Left_P________________________
robotA.MoveJ(d3)
robotA.setSpeed(1000)
gripper1.DetachAll()
pi4.setParentStatic(mesafinal)                        #Se cambia el pi_____________________________________
#RobotA se mueve a la posición de home
e3=transl(945.000,0.000,834.135)*roty(pi)
robotA.MoveJ(e3)
robotA.setSpeed(1000)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Process_Pieza5¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pick and Place en area de trabajo A0
#RobotA se aproxima a MesaA0 para recoger la pieza
aprox=20
a1 = transl(1323.030,257.289,93.068)*roty(pi)      #Se cambia respecto a AproxMesaA0_P________________________
robotA.MoveJ(a1)
robotA.setSpeed(1000)
#RobotA toma la pieza1 de la MesaA0 
b1 = transl(1323.030,257.289,-220.350)*roty(pi)    #Se cambia respecto a Take_P________________________
robotA.MoveJ(b1)
robotA.setSpeed(1000)
pi5.setParentStatic(gripper1)                      #Se cambia el pi_____________________________________
#RobotA lleva la pieza1 cerca de la MesaB
c1=transl(-1417.075,4.293,400.446)*roty(pi)
robotA.MoveJ(c1)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaB
d1=transl(-1417.075,4.293,100.367)*roty(pi)
robotA.MoveJ(d1)
robotA.setSpeed(1000)
gripper1.DetachAll()
pi5.setParentStatic(mesapaint)                     #Se cambia el pi_____________________________________
#RobotA se ubica en la posición de espera
e1=transl(-643.019,4.293,741.529)*roty(pi)
robotA.MoveJ(e1)
robotA.setSpeed(1000)
#RobotB se aproxima a MesaB
aprox=20
a02 = xyzrpw_2_pose([951.091,-99.100,515.373,90.000,-60.175,-173.197])
robotB.MoveJ(a02)
robotB.setSpeed(100)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#SprayOn5¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
Tool_Name = 'Paint gun'
Object_Name = 'Pieza5'

# Define the default action (0 to deactivate, +1 to activate, -1 to clear any spray gun simulation)
# Setting it to None will display a message
ACTION = +1

# quit if we are not in simulation mode
if RDK.RunMode() != RUNMODE_SIMULATE:
    quit()

# Get any previously added spray gun simulations and display statistics (spray on the part vs spray falling out of the part)
info, data = RDK.Spray_GetStats()
if data.size(1) > 0:
    print("Spray gun statistics:")
    print(info)
    print(data.tr())
    RDK.Spray_Clear() 

# Check if we are running this program inside another program and passing arguments
import sys
if len(sys.argv) > 1:
    ACTION = int(sys.argv[1])

# If the default ACTION is None, display a message to activate/deactivate the spray gun
if ACTION is None:
    print('Note: This macro can be called as Spray(1) or SprayOn(0)')
    entry = mbox('Turn gun ON or OFF', ('On', '1'), ('Off', '0'))
    if not entry:
        quit()
    ACTION = int(entry)    

if ACTION == 0:
    # Turn the gun off
    RDK.Spray_SetState(SPRAY_OFF)
    
elif ACTION < 0:
    # Clear all spray simulations (same as pressing ESC key)
    RDK.Spray_Clear()
    
elif ACTION > 0:
   
    tool = 0    # auto detect active tool
    obj = 0     # auto detect object in active reference frame
    if Tool_Name is not None:
        tool = RDK.Item(Tool_Name, ITEM_TYPE_TOOL)
    
    if Object_Name is not None:
        obj = RDK.Item(Object_Name, ITEM_TYPE_OBJECT)

    #options_command = "ELLYPSE PROJECT PARTICLE=SPHERE(4,8,1,1,0.5) STEP=8x8 RAND=2" # simulate 
    options_command = "PARTICLE=CUBE(10,10,2) STEP=8x8"

    # Another example with a varying rectancular shape
    # define the rectangular volume as p0, pA, pB, colorRGBA (close and far)
    if color == 1:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       1,0,0,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)
    
    if color == 2:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       0,1,0,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)
    
    if color == 3:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       0,0,1,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)

    if color == 4:    
        close_param = [-90,-117,  0,  90,-117,0,   -90,117,  0,       1,0,1,1]
        far_param   = [-175,-190,200, 175,-190,200,   -175,190,200,   1,0,0,0.2]
        volume = Mat([close_param, far_param])
        RDK.Spray_Add(tool, obj, "RECTANGLE PARTICLE=SPHERE(2,5) STEP=15x15 RAND=3", volume.tr())
        RDK.Spray_SetState(SPRAY_ON)

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#PP5_A¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pintado en area de trabajo B
#RobotB pinta pieza1, lado derecho 
aprox=20
a2 = xyzrpw_2_pose([1128.463,-77.940,203.783,90.000,-60.175,-173.197])
robotB.MoveJ(a2)
robotB.setSpeed(100)
c2 = xyzrpw_2_pose([1071.476,-84.739,225.057,90.000,-60.175,-173.197])
robotB.MoveJ(c2)
robotB.setSpeed(1000)
d2 = xyzrpw_2_pose([1002.267,-92.996,254.878,90.000,-60.175,-173.197])
robotB.MoveJ(d2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, centro 
e2 = xyzrpw_2_pose([1011.397,-39.866,300.368,180.000,0.000,-173.197])
robotB.MoveJ(e2)
robotB.setSpeed(1000)
f2 = xyzrpw_2_pose([1050.893,5.934,300.367,180.000,0.000,-173.197])
robotB.MoveJ(f2)
robotB.setSpeed(1000)
g2 = xyzrpw_2_pose([1079.262,49.092,300.367,180.000,0.000,-173.197])
robotB.MoveJ(g2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, lado izquierdo 
h2 = xyzrpw_2_pose([1098.260,69.520,285.711,-90.000,0.000,-173.197])
robotB.MoveJ(h2)
robotB.setSpeed(1000)
i2 = xyzrpw_2_pose([1048.722,63.609,234.840,-90.000,0.000,-173.197])
robotB.MoveJ(i2)
robotB.setSpeed(1000)
j2 = xyzrpw_2_pose([1007.902,58.739,193.572,-90.000,0.000,-173.197])
robotB.MoveJ(j2)
robotB.setSpeed(1000)
#RobotB pinta pieza1, frente 
k2 = xyzrpw_2_pose([972.738,-18.594,202.789,0.000,-90.000,-173.197])
robotB.MoveJ(k2)
robotB.setSpeed(1000)
l2 = xyzrpw_2_pose([973.710,-26.748,277.710,0.000,-90.000,-173.197])
robotB.MoveJ(l2)
robotB.setSpeed(1000)
#RobotB se mueve a la posición de home
b2 = xyzrpw_2_pose([670.544,0.000,1022.351,0.000,-60.000,-180.000])
robotB.MoveJ(b2)
robotB.setSpeed(100)
#Color
if color == 1:    
    pi5.Recolor([1,0,0,1])
if color == 2:    
    pi5.Recolor([0,1,0,1])
if color == 3:    
    pi5.Recolor([0,0,1,1])
if color == 4:    
    pi5.Recolor([1,0,1,1])

#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#PP5_B¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#Tarea Pick and Place en area de trabajo A1
#RobotA toma la pieza1 de la MesaB
a3=transl(-1417.075,4.293,100.367)*roty(pi)
robotA.MoveJ(a3)
robotA.setSpeed(1000)
mesapaint.DetachAll()
pi5.setParentStatic(gripper1)                          #Se cambia el pi_____________________________________
#RobotA lleva la pieza1 lejos de la MesaB
b3=transl(-1417.075,4.293,400.446)*roty(pi)
robotA.MoveJ(b3)
robotA.setSpeed(1000)
#RobotA lleva la pieza1 entre MesaB y MesaA1
f3=transl(1323.030,257.289,93.068)*roty(pi)            #Se cambia el AproxMesaA0_P_____________________________________
robotA.MoveJ(f3)
robotA.setSpeed(1000)
#RobotA lleva la pieza1 cerca de la MesaA1             
c3=transl(1323.030,-237.214,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(c3)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaA1
d3=transl(1323.030,-235.913,-220.350)*roty(pi)        #Se cambia respecto a Left_P________________________
robotA.MoveJ(d3)
robotA.setSpeed(1000)
gripper1.DetachAll()
pi5.setParentStatic(mesafinal)                        #Se cambia el pi_____________________________________
#RobotA se mueve a la posición de home
e3=transl(945.000,0.000,834.135)*roty(pi)
robotA.MoveJ(e3)
robotA.setSpeed(1000)