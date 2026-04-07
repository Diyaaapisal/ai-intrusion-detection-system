import time

def follow(file):
    file.seek(0, 2)  # move to end

    while True:
        line = file.readline()
        if not line:
            time.sleep(1)
            continue
        yield line


def monitor_log(log_file):
    with open(log_file, "r") as f:
        loglines = follow(f)

        for line in loglines:
            yield line