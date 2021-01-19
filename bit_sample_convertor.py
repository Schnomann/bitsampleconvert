import os
import glob
from ffmpy import FFmpeg

#######################config#######################
to_sample = "48000" #sample rate
to_bit = "16" #bit rate
####################################################

local_dir = os.path.dirname(__file__)
f_list = glob.glob(os.path.join(local_dir,"*.wav"))

def bit_convert(f):
    output = f"{f.split('.')[0]}_{to_bit}bit_{to_sample}Hz.wav"
    ff = FFmpeg(inputs={f: None}, 
                outputs={output: f"-sample_fmt s{to_bit} -ar {to_sample}"}
                )
    print(ff.cmd)
    ff.run()

for f in f_list:
    bit_convert(f)
