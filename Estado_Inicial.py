#Proyecto Laboratorio de Robótica Industrial
#Docente: Ing. María José Prado
#Integrantes del grupo: Henry Puhueyestewa - Miguel Espinoza
#Proyecto: Pintado de Objetos
#Paralelo 103


from robolink import *    # API to communicate with RoboDK
from robodk import *      # basic matrix operations
RDK = Robolink()

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
#Limpio la pintura anterior¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
RDK.Spray_Clear()               #Limpio la pintura
pi1.Recolor([0.90,0.91,0.96,1]) #La pieza inicia blanca
pi2.Recolor([0.90,0.91,0.96,1]) #La pieza inicia blanca
pi3.Recolor([0.90,0.91,0.96,1]) #La pieza inicia blanca
pi4.Recolor([0.90,0.91,0.96,1]) #La pieza inicia blanca
pi5.Recolor([0.90,0.91,0.96,1]) #La pieza inicia blanca

#Colocando a posición inicial Pieza1------------------------------------------------------------------
#RobotA se acerca a la MesaA1
ap1=transl(1323.030,-935.107,93.068)*roty(pi)
robotA.MoveJ(ap1)
robotA.setSpeed(1000)
#RobotA toma la pieza1 de la MesaA1
bp1=transl(1323.030,-933.806,-220.350)*roty(pi)
robotA.MoveJ(bp1)
robotA.setSpeed(1000)
mesafinal.DetachAll()
pi1.setParentStatic(gripper1)
#RobotA se aleja de la MesaA1
cp1=transl(1323.030,-935.107,93.068)*roty(pi)
robotA.MoveJ(cp1)
robotA.setSpeed(1000)
#RobotA se aproxima a MesaA0 para dejar la pieza
dp1= transl(1323.030,955.182,93.068)*roty(pi)
robotA.MoveJ(dp1)
robotA.setSpeed(1000)
#RobotA deja la pieza1 en la MesaA0 
ep1= transl(1323.030,956.483,-220.350)*roty(pi)
robotA.MoveJ(ep1)
robotA.setSpeed(1000)
gripper1.DetachAll()
#RobotA se mueve a la posición de home
fp1=transl(945.000,0.000,834.135)*roty(pi)
robotA.MoveJ(fp1)
robotA.setSpeed(1000)

#Colocando a posición inicial Pieza2------------------------------------------------------------------
#RobotA se acerca a la MesaA1            
ap2=transl(1323.030,-761.529,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(ap2)
robotA.setSpeed(1000)
#RobotA toma la pieza2 de la MesaA1
bp2=transl(1323.030,-760.228,-220.350)*roty(pi)        #Se cambia respecto a Left_P________________________
robotA.MoveJ(bp2)
robotA.setSpeed(1000)
mesafinal.DetachAll()
pi2.setParentStatic(gripper1)                        #Se cambia el pi_____________________________________
#RobotA se aleja de la MesaA1             
cp2=transl(1323.030,-761.529,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(cp2)
robotA.setSpeed(1000)
#RobotA se aproxima a MesaA0 para dejar la pieza
dp2= transl(1323.030,780.657,93.068)*roty(pi)      #Se cambia respecto a AproxMesaA0_P________________________
robotA.MoveJ(dp2)
robotA.setSpeed(1000)
#RobotA deja la pieza2 de la MesaA0 
ep2= transl(1323.030,780.657,-220.350)*roty(pi)    #Se cambia respecto a Take_P________________________
robotA.MoveJ(ep2)
robotA.setSpeed(1000)
gripper1.DetachAll()                      #Se cambia el pi_____________________________________
#RobotA se mueve a la posición de home
fp2=transl(945.000,0.000,834.135)*roty(pi)
robotA.MoveJ(fp2)
robotA.setSpeed(1000)

#Colocando a posición inicial Pieza3------------------------------------------------------------------
#RobotA se acerca a la MesaA1            
ap3=transl(1323.030,-585.913,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(ap3)
robotA.setSpeed(1000)
#RobotA toma la pieza3 de la MesaA1
bp3=transl(1323.030,-584.612,-220.350)*roty(pi)        #Se cambia respecto a Left_P________________________
robotA.MoveJ(bp3)
robotA.setSpeed(1000)
mesafinal.DetachAll()
pi3.setParentStatic(gripper1)                        #Se cambia el pi_____________________________________
#RobotA se aleja de la MesaA1             
cp3=transl(1323.030,-585.913,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(cp3)
robotA.setSpeed(1000)
#RobotA se aproxima a MesaA0 para dejar la pieza
dp3= transl(1323.030,606.483,93.068)*roty(pi)      #Se cambia respecto a AproxMesaA0_P________________________
robotA.MoveJ(dp3)
robotA.setSpeed(1000)
#RobotA deja la pieza2 en la MesaA0 
ep3= transl(1323.030,606.483,-220.350)*roty(pi)    #Se cambia respecto a Take_P________________________
robotA.MoveJ(ep3)
robotA.setSpeed(1000)
gripper1.DetachAll()                      #Se cambia el pi_____________________________________
#RobotA se mueve a la posición de home
fp3=transl(945.000,0.000,834.135)*roty(pi)
robotA.MoveJ(fp3)
robotA.setSpeed(1000)                

#Colocando a posición inicial Pieza4------------------------------------------------------------------
#RobotA se acerca a la MesaA1            
ap4=transl(1323.030,-411.739,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(ap4)
robotA.setSpeed(1000)
#RobotA toma la pieza4 de la MesaA1
bp4=transl(1323.030,-410.438,-220.350)*roty(pi)        #Se cambia respecto a Left_P________________________
robotA.MoveJ(bp4)
robotA.setSpeed(1000)
mesafinal.DetachAll()
pi4.setParentStatic(gripper1)
#RobotA se aleja de la MesaA1             
cp4=transl(1323.030,-411.739,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(cp4)
robotA.setSpeed(1000)
#RobotA se aproxima a MesaA0 para dejar la pieza
dp4= transl(1323.030,430.867,93.068)*roty(pi)      #Se cambia respecto a AproxMesaA0_P________________________
robotA.MoveJ(dp4)
robotA.setSpeed(1000)
#RobotA deja la pieza4 de la MesaA0 
ep4= transl(1323.030,430.867,-220.350)*roty(pi)    #Se cambia respecto a Take_P________________________
robotA.MoveJ(ep4)
robotA.setSpeed(1000)  
gripper1.DetachAll()                      #Se cambia el pi_____________________________________
#RobotA se mueve a la posición de home
fp4=transl(945.000,0.000,834.135)*roty(pi)
robotA.MoveJ(fp4)
robotA.setSpeed(1000)    

#Colocando a posición inicial Pieza5------------------------------------------------------------------
#RobotA se acerca a la MesaA1             
ap5=transl(1323.030,-237.214,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(ap5)
robotA.setSpeed(1000)
#RobotA toma la pieza5 en la MesaA1
bp5=transl(1323.030,-235.913,-220.350)*roty(pi)        #Se cambia respecto a Left_P________________________
robotA.MoveJ(bp5)
robotA.setSpeed(1000)
mesafinal.DetachAll()
pi5.setParentStatic(gripper1) 
#RobotA se aleja de la MesaA1             
cp5=transl(1323.030,-237.214,93.068)*roty(pi)           #Se cambia el AproxMesaA1_P__________________________
robotA.MoveJ(cp5)
robotA.setSpeed(1000)
#RobotA se aproxima a MesaA0 para dejar la pieza
dp5= transl(1323.030,257.289,93.068)*roty(pi)      #Se cambia respecto a AproxMesaA0_P________________________
robotA.MoveJ(dp5)
robotA.setSpeed(1000)
#RobotA deja la pieza5 en la MesaA0 
ep5= transl(1323.030,257.289,-220.350)*roty(pi)    #Se cambia respecto a Take_P________________________
robotA.MoveJ(ep5)
robotA.setSpeed(1000)
gripper1.DetachAll()                      #Se cambia el pi_____________________________________
#RobotA se mueve a la posición de home
fp5=transl(945.000,0.000,834.135)*roty(pi)
robotA.MoveJ(fp5)
robotA.setSpeed(1000)        

