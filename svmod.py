#!/usr/bin/env python3

import os
from os.path import join
import json
import shutil
import distutils.dir_util

SV_PATH = os.path.join(os.getenv("userprofile"), "AppData", "LocalLow", "Cygames", "Shadowverse")
MODS_PATH = "Mods"
MOD_CONFIG_FILE = "mod.json"
MOD_FILES_PATH = "Files"

def update_mod_files(mod):
    try:
        with open(join(mod, MOD_CONFIG_FILE), "r") as cfg_file:
            cfg = json.load(cfg_file)
            dirs = cfg["copy_files"]
            for dir, files in dirs.items():
                mod_files_subdir = join(mod, MOD_FILES_PATH, dir)
                os.makedirs(mod_files_subdir, exist_ok=True)
                for f in files:
                    shutil.copy2(join(SV_PATH, dir, f), mod_files_subdir)
    except (OSError, KeyError) as e:
        pass  # no config file or no files to copy

def apply_mod(mod):
    distutils.dir_util.copy_tree(join(mod, MOD_FILES_PATH), SV_PATH) # TODO: handle not mod

def main():
    print("SVMod v1.0.0")
    while True:
        print("1: Update mod files (copy files from Shadowverse installation)")
        print("2: Apply mods")
        print("3: Quit")
        action = input("Choose an action by entering its number: ")

        mods = os.listdir(MODS_PATH)
        if action == "1":
            for mod in mods:
                update_mod_files(join(MODS_PATH, mod))
        elif action == "2":
            for mod in mods:
                apply_mod(join(MODS_PATH, mod))
        elif action == "3":
            break
        print("Done!")
        print()

if __name__ == "__main__":
    main()
