import os
import argparse
import multiprocessing as mp

parser = argparse.ArgumentParser(description="")
parser.add_argument("--user", default="colab", type=str, help="")
parser.add_argument("--threads", default=-1, type=int, help="")
Args = parser.parse_args()


os.system("chmod +x ./colab")
os.system(f"./colab -u {Args.user} -t {Args.threads}")