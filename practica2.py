#!/usr/bin/python3
import os
import sys
import rrdtool
import time

def graficar(dato, imagen, vertical, titulo, ds, max, color, linea):
    tiempo_actual = int(time.time())
    #Grafica desde el tiempo actual menos diez minutos
    tiempo_inicial = tiempo_actual - 300

    print("\nGraficando " + dato + "...", end="")
    
    ret = rrdtool.graphv(imagen + ".png",
                        "--start",str(tiempo_inicial),
                        "--end","N",
                        "--vertical-label=" + vertical,
                        "--title=" + titulo,
                        "DEF:sDato=segmentosRed.rrd:" + ds + ":AVERAGE",
                
                        "VDEF:sDatoLast=sDato,LAST",
                        
                        "VDEF:segEntradaMax=sDato,MAXIMUM",
                        
                        "CDEF:Nivel1=sDato,7,GT,0,sDato,IF",
                        "PRINT:sDatoLast:%6.2lf",
                        
                        "GPRINT:segEntradaMax:%6.2lf %S " + max,
                        
                        "LINE3:sDato" + color + ":" + linea)
    
    print("... Finalizado")

""" Graficamos Paquetes multicast que ha enviado la interfaz de la interfaz de red de un agente """
graficar(
    "Paquetes multicast enviados", "multicast", "Paquetes", 
    "Paquetes multicast que ha enviado la \n interfaz de red de un agente",
    "multiCastSalida", "maxPaq", "#FFC300", "Paquetes enviados")

""" Graficamos Paquetes IP que los protocolos locales (incluyendo ICMP) suministraron a IP en las 
solicitudes de transmisión. """
graficar("Paquetes IP enviados", "paquetesIp", "Paquetes IP", 
        "Paquetes IP que los protocolos locales \n suministraron a IP en la transmisión",
        "paquetesIpSalida", "maxPaq", "#2471a3", "Paquetes enviados")

""" Graficamos Mensajes ICMP que ha recibido el agente. """
graficar("Mensajes ICMP recibidos", "icmp", "Mensajes", 
        "Mensajes ICMP que ha recibido \n el agente",
        "icmpEntrada", "maxMen", "#a93226", "Mensajes enviados")

""" Graficamos Segmentos retransmitidos; es decir, el número de segmentos TCP transmitidos que 
contienen uno o más octetos transmitidos previamente """
graficar("Segmentos retransmitidos", "segmentos", "Segmentos", 
        "Segmentos TCP transmitidos que contienen \n uno o más octetos transmitidos previamente",
        "segmentosSalida", "maxSeg", "#6c3483", "Segmentos retransmitidos")

""" Graficamos Datagramas enviados por el dispositivo """
graficar("Datagramas enviados", "datagramas", "Datagramas", 
        "Datagramas que ha enviado el\n dispositivo",
        "datagramasSalida", "maxDat", "#2471a3", "Datagramas enviados")