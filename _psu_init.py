# 

import pyvisa as pv

rm = pv.ResourceManager()
_list = rm.list_resources()
_target = 'Agilent'

ids = []
for idn in _list:
    inst = rm.open_resource(idn)
    ids.append(inst.query('*IDN?'))
    

    

