import subprocess as sp
import re

def CheckOS():
    p = sp.Popen(["cat", "/etc/os-release"], stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = p.communicate()
    searchOS = re.findall('(\w+)\s*=\s*\"([\w%-]+)\"', str(stdout))

    for element in searchOS:
        if element[0].lower() =="name":
            foundOS = element[1]
            break
    return foundOS


def CheckEnv(foundOS):
    try:
        if foundOS.lower() =="ubuntu":
            p = sp.Popen(["apt", "list"], stdout=sp.PIPE)
            output = sp.check_output(['grep', 'python3-virtualenv'], stdin=p.stdout)
            result = True if output else False
        if foundOS.lower() =="fedora":
            p = sp.Popen(["dnf", "list"], stdout=sp.PIPE)
            output = sp.check_output(['grep', 'python3-virtualenv'], stdin=p.stdout)
            result = True if output else False
        return result
    except sp.CalledProcessError:
        raise Exception("VirtualEnv no encontrado")


def PrepareEnv(choosenPM):
    relationEnv = {"fedora":["dnf", "python","pip"], "ubuntu":["apt","python3","pip3"]}
    p = sp.Popen(f"sudo {relationEnv[choosenPM][0]} update",shell=True, executable="/bin/bash")
    p.wait()
    p2 = sp.Popen(f"sudo {relationEnv[choosenPM][0]} install -y {relationEnv[choosenPM][1]}-virtualenv", shell=True, executable="/bin/bash")
    p2.wait()
    p3 = sp.Popen("virtualenv MainEnv", shell=True, executable="/bin/bash")
    p3.wait()
    return True

def PreparePip():
    exec(open("EnvCreate.py").read(), {'__file__': "EnvCreate.py"})
    p4 = sp.Popen(f"{relationEnv[choosenPM][2]} install -r requirements.txt", shell=True,  executable="/bin/bash")
    p4.wait() 



