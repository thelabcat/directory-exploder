#!/usr/bin/env python3
#Directory Exploder
#S.D.G.

import os
import shutil

BASEPATH=__file__[:__file__.rfind(os.sep)]

folders=os.walk(BASEPATH)

for folder_path, inner_folders, inner_files in folders:
    for file in inner_files:
        shutil.move(folder_path+os.sep+file, BASEPATH+os.sep+file)