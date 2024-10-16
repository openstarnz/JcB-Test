# JcB test control code
# design to run on pyvisa/nidaqmx
# live plot the resulting data in uV/cm
# plan to use the agilent PSU instead of top-magnet supply

# break down to individual components
    # nidaqmx data acquisition/handling
    # saving data
    # initialize psu
    # step psu current
    # check signal overvoltage
    # step down experiment
import sys

from PyQt6.QtWidgets import QApplication

import pyvisa as pv

