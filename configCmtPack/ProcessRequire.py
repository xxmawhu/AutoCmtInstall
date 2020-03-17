# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : ProcessRequire.py
#   Create Time   : 2020-02-29 20:20
#   Last Modified : 2020-02-29 20:39
#   Describe      :
#
# ====================================================
import logging
import os

import GitSvc
import CheckBOSS
import RepoSet

logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

class ProcessRequire(object):
    def __init__(self):
        """"
        localAddress: dir:
          key: the name of the package
          value: list
             local address that installed the package,
          the local address maybe more than one,
        Repository: dir:
           * key: the package name
           * value: the remote repository address
        installed: set
           * elememt is a tuple, like (package-name, local-address)
        """
        self._Repository={}
        self._localAddress={}
        self._install= set()
    
    def AddRepository(self, repos):
        """
        repos: dir:
          * key: package name
          * value: remote address
        the new remote address maybe over write the old one
        """
        for i in repos:
            self._Repository[i] = repos[i]

    def ReadRequirement(self, requirement):
        f = open(requirement, 'r')
        for Line in f.readlines():
            LL = Line.split()
            if len(LL) < 2 :
                continue
            if LL[0] != "use":
                continue
            packName = LL[1]
            if packName not in self._Repository:
                continue
            if len(LL) < 4:
                localAdd=""
            else:
                localAdd = LL[-1]
            self._install.add((packName, localAdd));
            try:
                self._localAddress[packName].append(localAdd)
            except KeyError as e:
                self._localAddress[packName] = [localAdd]
        f.close()

    def Install(self, requirement):
        self.ReadRequirement(requirement)
        gitSvc = GitSvc.GitSvc(CheckBOSS.GetWorkArea())
        for i in self._install:
            packName = i[0]
            locaddress = i[1]
            logger.info("Install {} into {}".format(i[0], i[1]))
            gitSvc.Install(locaddress, self._Repository[packName])


if __name__ == "__main__":
    processRequire = ProcessRequire()
    processRequire.AddRepository(RepoSet.remote)
    processRequire.Install('requirements')

