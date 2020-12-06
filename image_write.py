import argparse
import os

parser = argparse.ArgumentParser(description='Image Writer')

parser.add_argument('-f', '--file' , help='File name')
namespace = parser.parse_args()

file_name = namespace.f

os.system(f"sudo dd bs=4M if={file_name} of=/dev/sdb status=progress oflag=sync  ")