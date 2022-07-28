import sys
import os
import time
import subprocess
import multiprocessing as mp

FILE_NAME = "xiangqi.bin"


test_params = {
    "depth": 4,
    "eval_limit": 3000,
    "eval_diff_limit": 500,
    "random_move_min_ply": 1,
    "random_move_max_ply": 3,
    "random_move_count": 8,
    "random_multi_pv": 4,
    "random_multi_pv_diff": 100,
    "random_multi_pv_depth": 4,
    "write_min_ply": 1,
    "write_max_ply": 400,
}


def get_generation_command(data_count, threads, output_file, generation_params):
    params = f"""setoption name UCI_Variant value xiangqi
setoption name Use NNUE value pure
setoption name EvalFile value ./xiangqi-weights.nnue
setoption name Threads value {threads}
setoption name Hash value 2048
"""
    gen_params_str = ""
    for k, v in generation_params.items():
        gen_params_str += f"{k} {v} "
    cmd = f"generate_training_data count {data_count} book xiangqi-book.epd {gen_params_str}" \
          f"set_recommended_uci_options data_format bin output_file_name {output_file}\n"
    return params + cmd


def generate_data(params, threads=-1, amount=10000):
    if threads < 1:
        threads = mp.cpu_count()
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
    while os.path.exists(FILE_NAME):
        time.sleep(0.1)
    exe_file = "fairy.exe" if os.name == "nt" else "./fairy"
    if os.name != "nt":
        os.system("chmod +x " + exe_file)
    fairy = subprocess.Popen([exe_file], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp_params = get_generation_command(amount, threads, FILE_NAME, params)
    fairy.stdin.write(tmp_params.encode())
    fairy.stdin.flush()
    fairy.stdout.flush()
    output = fairy.stdout.readline()
    while output:
        output = output.decode("utf-8").replace("\r\n", "")
        if "sfen" in output or "evaluation" in output:
            print(output)
        if "finished" in output:
            print(output)
            time.sleep(1)
            fairy.terminate()
            break
        fairy.stdout.flush()
        output = fairy.stdout.readline()
    while not os.path.exists(FILE_NAME):
        time.sleep(0.1)


if __name__ == "__main__":
    generate_data(test_params, threads=4, amount=5000)
