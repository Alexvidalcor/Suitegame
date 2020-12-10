import subprocess as sp
import re

def PrepareEnv(choosenPM = foundOS.lower()):
    relationEnv = {"fedora":["dnf", "python"], "ubuntu":["apt","neofetch"]}
    p = sp.Popen(["sudo", f"{relationEnv[choosenPM][0]}", "install", "-y", f"{relationEnv[choosenPM][1]}"])









def CheckOS():
    p = sp.Popen(["cat", "/etc/os-release"], stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = p.communicate()
    searchOS = re.findall('(\w+)\s*=\s*\"([\w%-]+)\"', str(stdout))

    for element in searchSO:
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
        # raise Exception("VirtualEnv no encontrado")



