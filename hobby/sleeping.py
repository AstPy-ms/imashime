import time
import sys

# ドットがNUM個出たらドットをリセットする
NUM = 133

dot = "."
i = 0

while 1:
    sys.stdout.write("\rNow sleeping{}".format(dot*i))
    time.sleep(1.0)
    i += 1
    if i > NUM:
        i = 0
