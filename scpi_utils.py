#! /usr/bin/python3
#
# __author__ = [pacosalces,]
# "I'm not a wrapper"
#
# A very minimal red pitaya SCPI server utils following:
# https://redpitaya.readthedocs.io/en/latest/appsFeatures/remoteControl/remoteControl.html

import os
import subprocess
import time


class SCPIServer:

    """A 100% insecure SCPI server. Do not deploy in unknown networks"""

    def __init__(self, **kwargs):
        try:
            subprocess.check_call("systemctl status redpitaya_scpi", shell=True)
        except subprocess.CalledProcessError as e:
            print(e)
            subprocess.call("systemctl start redpitaya_scpi", shell=True)


if __name__ == "__main__":
    server = SCPIServer()
