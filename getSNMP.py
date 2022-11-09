#!/usr/bin/python3
from pysnmp.hlapi import *

def consultaSNMP(comunidad,host,oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(comunidad),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    else:
        for varBind in varBinds:
            varB=(' = '.join([x.prettyPrint() for x in varBind]))
            resultado= varB.split()[2]
    return resultado

#1. print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.2.2.1.12.2"))
""" print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.1.5.0"))
print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.1.4.0"))
print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.4.2.0"))
print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.2.2.1.10.1"))
print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.2.2.1.16.1"))
print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.1.3.0"))
print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.2.2.1.11.1"))
print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.2.2.1.17.1")) """



""" print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.2.1.0"))
print(consultaSNMP("LuisAlbertoGarcia","localhost","1.3.6.1.2.1.2.2.1.6.2")) """
""" snmpget -v1 -c LuisAlbertoGarcia localhost 1.3.6.1.2.1.2.2.1.6.1
snmpget -v1 -c LuisAlbertoGarcia localhost 1.3.6.1.2.1.2.1.0 """

""" snmpget -v1 -c JRockitDesk localhost 1.3.6.1.2.1.7.4.0 """