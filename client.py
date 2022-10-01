import os
import argparse
import multiprocessing as mp

parser = argparse.ArgumentParser(description="")
parser.add_argument("--user", default="colabb", type=str, help="")
parser.add_argument("--threads", default=-1, type=int, help="")
Args = parser.parse_args()


os.system("chmod +x ./colabb")
os.system(f"./colabb -u {Args.user} -t {Args.threads}")