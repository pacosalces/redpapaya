#! /usr/bin/python
#
# __author__ = [pacosalces,]
# "I'm not a wrapper"
#
# Red Pitaya SCPI server utils following:
# https://redpitaya.readthedocs.io/en/latest/appsFeatures/remoteControl/remoteControl.html

import os
import time
import sh
from rich.progress import track


class SCPIServer:

    """ """

    def __init__(self, **kwargs):
        print(sh.ls("./"))


if __name__ == "__main__":
    server = SCPIServer()
