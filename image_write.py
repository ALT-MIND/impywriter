import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='Image Writer')

parser.add_argument('-f', '--file' , help='File name')
namespace = parser.parse_args()
file_name = namespace.f
q = subprocess.check_output(['hwinfo', '--disk', '--short'])
q = q.decode('utf-8')


os.system(f"sudo dd bs=4M if={file_name} of=/dev/sdb status=progress oflag=sync  ")