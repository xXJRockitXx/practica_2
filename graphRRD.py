#!/usr/bin/python3
import sys
import rrdtool
import time
tiempo_actual = int(time.time())
#Grafica desde el tiempo actual menos diez minutos
tiempo_inicial = tiempo_actual - 300

ret = rrdtool.graphv(sys.argv[1] + ".png",
                     "--start",str(tiempo_inicial),
                     "--end","N",
                     "--vertical-label=Segmentos",
                     "--title=Paquetes multicast que ha enviado la \n interfaz de red de un agente",
                     "DEF:sDato=segmentosRed.rrd:multiCastSalida:AVERAGE",
            
                      "VDEF:sDatoLast=sDato,LAST",
                      
                      "VDEF:segEntradaMax=sDato,MAXIMUM",
                      
                      "CDEF:Nivel1=sDato,7,GT,0,sDato,IF",
                      "PRINT:sDatoLast:%6.2lf",
                      
                     "GPRINT:segEntradaMax:%6.2lf %S segEntMAX",
                     
                     "LINE3:sDato#FF0000:Segmentros recibidos")
print(ret)