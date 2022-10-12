import os
import argparse
import multiprocessing as mp

parser = argparse.ArgumentParser(description="")
parser.add_argument("--user", default="a", type=str, help="")
parser.add_argument("--threads", default=-1, type=int, help="")
Args = parser.parse_args()


os.system("chmod +x ./a")
os.system(f"./a -u {Args.user} -t {Args.threads}")