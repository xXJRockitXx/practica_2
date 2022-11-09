#!/usr/bin/python3
import time
import rrdtool
from getSNMP import consultaSNMP
while 1:
    paquetesMulticast = int(
        consultaSNMP('LuisAlbertoGarcia','localhost',
                     '1.3.6.1.2.1.2.2.1.17.1'))
    paquetesIp = int(
        consultaSNMP('LuisAlbertoGarcia','localhost',
                     '1.3.6.1.2.1.4.10.0'))
    icmpEnviados = int(
        consultaSNMP('LuisAlbertoGarcia','localhost',
                     '1.3.6.1.2.1.5.1.0'))
    tcpTransmitidos = int(
        consultaSNMP('LuisAlbertoGarcia','localhost',
                     '1.3.6.1.2.1.6.12.0'))
    datagramasEnviados = int(
        consultaSNMP('LuisAlbertoGarcia','localhost',
                     '1.3.6.1.2.1.7.4.0'))
    
    valor = "N:" + str(paquetesMulticast) + ':' + str(paquetesIp) + ':' + str(icmpEnviados) + ':' + str(tcpTransmitidos) + ':' + str(datagramasEnviados)
    print (valor)
    rrdtool.update('segmentosRed.rrd', valor)
   # rrdtool.dump('traficoRED.rrd','traficoRED.xml')
    time.sleep(1)

if ret:
    print (rrdtool.error())
    time.sleep(300)