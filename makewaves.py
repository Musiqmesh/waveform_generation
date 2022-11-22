import os
import subprocess

directory = os.getcwd()
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     
     if filename.endswith(".wav"): 
         print(filename)
         command = 'python wavemaker.py ' + filename
         print(command)
         subprocess.run(command)  
         continue
     else:
         continue