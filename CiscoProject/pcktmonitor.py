import time
import psutil
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
la_rcd_bytes=psutil.net_io_counters().bytes_recv
la_snt_bytes=psutil.net_io_counters().bytes_sent
total_bytes=la_rcd_bytes+la_snt_bytes
io_bytes=psutil.net_io_counters(pernic=True)
io_bytes1=psutil.net_io_counters()
print(io_bytes)
print(io_bytes1)