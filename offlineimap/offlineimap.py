#! /usr/bin/env python2
from subprocess import check_output

def get_pass():
    return check_output("gpg -dq --default-key F8C034F1 ~/.mutt_offline/northumbria_pass.gpg", shell=True).strip("\n")
