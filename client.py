import os
import argparse

parser = argparse.ArgumentParser(description="分布式生成棋谱")
parser.add_argument("--user", default="VinXiangQi", type=str, help="用于统计训练量的用户名")
parser.add_argument("--threads", default=-1, type=int, help="用于跑谱的核心数")
Args = parser.parse_args()

os.system("chmod +x ./stockfish")
os.system(f"./stockfish -u {Args.user} -t {Args.threads}")