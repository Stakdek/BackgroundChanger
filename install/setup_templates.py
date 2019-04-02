#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8
import sys
import os
import getpass
from os.path import expanduser

def run(interval,picpath):
    replace_map = {
        '#HOME#' : expanduser("~"),
        '#IVAN-PATH#' : os.path.dirname(os.path.realpath(__file__)).replace('/install',''),
        '#USER#' : getpass.getuser(),
        '#PICPATH#' : picpath,
        '#INTERVAL#': str(interval),
    }
    output=[]

    with open('install/backgroundchanger_template','r') as service_temp_file:
        service_temp = service_temp_file.readlines()
        for line in service_temp:
            for key in replace_map.keys():
                if key in line:
                    line = line.replace(key, replace_map[key])
            output.append(line)

    with open('backgroundchanger', 'w') as service_file:
        service_file.writelines(output)
    return
