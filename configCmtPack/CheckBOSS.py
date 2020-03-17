#!/usr/bin/env python3
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2020 All rights reserved.
#
#   Author        : Xin-Xin MA
#   Email         : xxmawhu@163.com
#   File Name     : CheckBOSS.py
#   Create Time   : 2020-02-27 20:45
#   Last Modified : 2020-02-27 20:51
#   Describe      :
#
# ====================================================
import os


def IsBOSSSetUp():
    if "TESTRELEASEROOT" in os.environ:
        return True
    else:
        return False


def GetWorkArea():
    return os.environ['TESTRELEASEROOT'].split("TestRelease")[0]


def GetBossVersion():
    BesArea = os.environ['BesArea']
    return BesArea.split(r"/")[-1]


def GetTestRelease():
    if "TESTRELEASEROOT" in os.environ:
        return os.environ["TESTRELEASEROOT"] + "/cmt/requirements"
    else:
        return ""


if __name__ == "__main__":
    if IsBOSSSetUp():
        print("BOSS set up now")
        print("BOSS version {}".format(GetBossVersion()))
        print("workarea {}".format(GetWorkArea()))
    else:
        print("Error :BOSS didnot set up now")
