#! /usr/bin/env python2
from subprocess import check_output

def get_pass(acc):
    if acc == 'northumbria':
        return check_output("gpg -dq --default-key F8C034F1 ~/.mutt_offline/northumbria_pass.gpg", shell=True).strip("\n")
    elif acc == 'hesabu':
        return check_output("gpg -dq --default-key F8C034F1 ~/.mutt_offline/hesabu_pass.gpg", shell=True).strip("\n")
    else:
        return check_output("gpg -dq --default-key F8C034F1 ~/.mutt_offline/gmail_pass.gpg", shell=True).strip("\n")
    

