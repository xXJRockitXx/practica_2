#!/usr/bin/python3
import rrdtool
ret = rrdtool.create("segmentosRed.rrd",
                     "--start",'N',
                     "--step",'150',
                     "DS:multiCastSalida:COUNTER:120:U:U",
                     "DS:paquetesIpSalida:COUNTER:120:U:U",
                     "DS:icmpEntrada:COUNTER:120:U:U",
                     "DS:segmentosSalida:COUNTER:120:U:U",
                     "DS:datagramasSalida:COUNTER:120:U:U",
                     "RRA:AVERAGE:0.5:1:200",
                     "RRA:AVERAGE:0.5:1:200",
                     "RRA:AVERAGE:0.5:1:200",
                     "RRA:AVERAGE:0.5:1:200",
                     "RRA:AVERAGE:0.5:1:200")

if ret:
    print (rrdtool.error())