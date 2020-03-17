#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : main.py
#   Create Time   : 2020-03-17 16:08
#   Last Modified : 2020-03-17 16:08
#   Describe      :
#
# ====================================================
import sys
import logging
import ProcessRequire
import RepoSet
import CheckBOSS

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

USAGEE="""AutoInstall requirements"""

def main():
    processRequire = ProcessRequire.ProcessRequire()
    processRequire.AddRepository(RepoSet.remote)
    if "-h" in sys.argv:
        print(USAGEE)
        exit(0)
    m_Force = False
    if "-f" in sys.argv:
        m_Force = True
    if len(sys.argv) < 2:
        try:
            logger.info("Process {}".format(CheckBOSS.GetTestRelease()))
            processRequire.Install(CheckBOSS.GetTestRelease(), m_Force)
        except Exception as e:
            print(e)
            return
    for i in sys.argv[1:]:
        if "-" == i[0]:
            continue
        logger.info("Processing '{}' now".format(i))
        processRequire.Install(i, m_Force)


if __name__ == "__main__":
    main()
