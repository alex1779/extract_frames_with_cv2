# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:26:35 2022

@author: Ale
"""
import os
from natsort import natsorted


def getBaseName(pathFile):
    basename = os.path.splitext(os.path.basename(pathFile))[0]
    return basename


def listFiles(path):
    files = natsorted(os.listdir(path))
    return files


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
