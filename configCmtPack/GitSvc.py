# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : GitSvc.py
#   Create Time   : 2020-02-28 21:23
#   Last Modified : 2020-02-28 21:23
#   Describe      :
#
# ====================================================
import os
from util import getoutput
import subprocess
import logging
import CheckBOSS
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


class GitSvc(object):
    def __init__(self, workarea=""):
        self._workarea = workarea
        self._remoteAddress = ""
        # self._localAddress = ""
        self._force = False

    def SetWorkArea(self, workarea):
        self._workarea = workarea

    def Force(self):
        self._force = True

    def SetRemoteAddress(self, remoteAddress):
        self._remoteAddress = remoteAddress.strip()
        self._packName = remoteAddress.split(r"/")[-1].split('.')[0]

    def WriteRequirement(self, packagename, localAddress):
        testRelease = CheckBOSS.GetTestRelease()
        s = open(testRelease, 'r').read()
        content = ""
        for line in open(testRelease, 'r').readlines():
            if len(line.split()) < 4:
                continue
            if "use" == line.split()[0]:
                content += line
        if localAddress in content and packagename in content:
            return
        newLine = "use {} {}-* {}\n".format(packagename, packagename,
                                            localAddress)
        s += newLine
        f = open(testRelease, 'w')
        f.write(s)
        f.close()

    def Install(self, localAddress="", remoteAddress=""):
        self.SetRemoteAddress(remoteAddress)
        self.WriteRequirement(self._packName, localAddress)
        # string: localAddress
        # where you want to put the remote package into,
        # for example: Analysis, Utility
        logging.info("workarea {}".format(self._workarea))
        logging.info("The remote repository is {}".format(self._remoteAddress))
        target = os.path.join(self._workarea, localAddress, self._packName)
        if os.path.exists(target):
            logging.info("the local package is exist!")
            output = getoutput("cd {}; git pull".format(target))
            output = getoutput("cd {}; git remote -v".format(target))
            print("target = {}".format(target))
            try:
                remoteAddress = output.split("\n")[1].split()[1]
            except Exception as e:
                print(e)
            if remoteAddress.strip() != self._remoteAddress:
                while True and not self._force:
                    c = raw_input(
                        "The current remote Address is {} \n".format(
                            remoteAddress) +
                        "but the input is {}\n".format(self._remoteAddress) +
                        "Do you want overwrite it? y/n:")
                    # print(c)
                    if c == "y":
                        # print("yes \n")
                        getoutput('cd {} ; /bin/rm -rf *'.format(target))
                        output = getoutput("git clone {} {}".format(
                            self._remoteAddress, target))
                        print(output)
                        break
                    if c == "n":
                        break
                if self._force:
                    getoutput('cd {} ; /bin/rm -rf *'.format(target))
                    output = getoutput("git clone {} {}".format(
                        self._remoteAddress, target))
        else:
            logging.info("makedirs {}".format(target))
            os.makedirs(target)
            output = getoutput("git clone {} {}".format(
                self._remoteAddress, target))
            logging.debug(output)


if __name__ == "__main__":
    gitSvc = GitSvc(CheckBOSS.GetWorkArea())
    gitSvc.Install(
        remoteAddress="https://github.com/xxmawhu/McDecayModeSvc.git",
        localAddress="test2")
