#! /usr/bin/python3

from src.EnvSupport import *

foundOS = CheckOS()

envManaged = CheckEnv(foundOS.lower())

# if envManaged:
envInstall = PrepareEnv(foundOS.lower())
dependenciesInstall = PreparePip()
    # requirementInstall = 



