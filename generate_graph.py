import keyboard
import glob
import subprocess
import re
import os
import array as arr
import time
import glob
import shutil

global res2
# This will search for the model file with highest number i.e most trained file
os.chdir(r"C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/training")
for name in glob.glob('*[^0-^100000]*.index'):
    Reste = " ".join(re.split("[^0-^10000]*", name))
    #print(Reste)
# Removes all the extra spaces
def remove1(Reste):
    return Reste.replace(" ", "")

res2 = remove1(Reste)
print(res2)
# replaces xxxx with the largest number found above
given_str = "python C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/export_inference_graph.py --input_type image_tensor --pipeline_config_path C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/training/faster_rcnn_inception_v2_pets.config --trained_checkpoint_prefix C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/training/model.ckpt-xxxx --output_directory C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/inference_graph"
sub_string = "xxxx"

if(given_str.find(sub_string) != -1):
    x = given_str.replace("xxxx", res2)
print(x)

shutil.rmtree(r'C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/inference_graph/saved_model')
files = glob.glob(r'C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/inference_graph/*')
for f in files:
    os.remove(f)
    
# execute the command to generate fozen inference graph
subprocess.call(x)
