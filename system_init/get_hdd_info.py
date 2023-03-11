import os
import subprocess
from typing import List


def get_system_hdd(cmd: List):
    cmd = ["bash -i -c  'history -r;history' "]
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.decode("utf-8"), stderr.decode("utf-8")




if __name__ == "__main__":
    commands = [
        {
            "cmd": "history", 
            "cli": "history"
        },
        {
            "cmd": "echo", 
            "cli": "echo"
        },
        {
            "cmd": "ls", 
            "cli": "ls -la"
        },
    ]

    #  ['sudo', 'hdparm', '-I', '/dev/sda']
    for c in commands:

        out, err = get_system_hdd(c.get('cli').split())
        with open('hdd.info', 'a') as f:
            f.write(out)
        with open('hdd.err', 'a') as f:
            f.write(err)
    
        for l in out.split('\n'):
            if "Model Number:" in l:
                hdd_model = "_".join(l.replace("Model Number:", "").strip().split())
                print(hdd_model)
            if "Serial Number:" in l:
                hdd_serial_number = "_".join(l.replace("Serial Number:", "").strip().split())
                print(hdd_serial_number)
            if "device size with M = 1000*1000:" in l:
                hdd_size = "_".join(l.replace("device size with M = 1000*1000:", "").strip().split())
                print(hdd_size)
