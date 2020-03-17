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
from configCmtPack import ProcessRequire
from configCmtPack import RepoSet
from configCmtPack import CheckBOSS


logging.basicConfig(level=logging.INFO,
                    format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


def main():
    processRequire = ProcessRequire.ProcessRequire()
    processRequire.AddRepository(RepoSet.remote)
    if len(sys.argv) < 2:
        try:
            logger.info("Process {}".format(CheckBOSS.GetTestRelease()))
            processRequire.Install(CheckBOSS.GetTestRelease())
        except Exception as e:
            print(e)
            return
    for i in sys.argv[1:]:
        logger.info("Processing '{}' now".format(i))
        #processRequire.Install(i)

if __name__ == "__main__":
    main()
