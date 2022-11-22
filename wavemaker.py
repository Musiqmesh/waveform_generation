from p5 import *
import numpy as np
from scipy.io import wavfile
import matplotlib
from matplotlib import pyplot
import sys

arr = []
filename = ''
outfilename = ''
hexArr = ['#00e4ff', '#00e0ff', '#00dcff', '#00d8ff', '#00d4ff', '#00d0ff',
       '#00ccff', '#00c8ff', '#00c4ff', '#00bfff', '#00bbff', '#00b6ff',
       '#00b2ff', '#00adff', '#00a8ff', '#00a3ff', '#009eff', '#0099ff',
       '#0094ff', '#008eff', '#0089ff', '#0083ff', '#007dff', '#0076ff',
       '#0070ff', '#0069ff', '#0062ff', '#005aff', '#0051ff', '#0048ff',
       '#003dff', '#0030ff', '#131efd', '#131efd', '#1f1efd', '#281dfd',
       '#301dfd', '#361cfd', '#3b1cfd', '#411cfd', '#451bfd', '#4a1bfd',
       '#4e1afd', '#521afd', '#561afd', '#5919fd', '#5d19fd', '#6019fd',
       '#6318fd', '#6618fd', '#6917fd', '#6c17fd', '#6f17fd', '#7216fd',
       '#7516fd', '#7716fd', '#7a15fd', '#7d15fd', '#7f15fd', '#8215fd',
       '#8414fd', '#8614fd', '#8914fd', '#8b14fd', '#8d13fd', '#9013fd',
       '#9213fd', '#9213fd', '#9513fd', '#9812fd', '#9a12fd', '#9d11fd',
       '#a011fd', '#a210fd', '#a510fd', '#a810fd', '#aa0ffd', '#ad0ffd',
       '#af0ffd', '#b20efd', '#b40efd', '#b70efd', '#b90efd', '#bb0efd',
       '#be0efd', '#c00efd', '#c20efd', '#c50efd', '#c70efd', '#c90efd',
       '#cc0ffd', '#ce0ffd', '#d00ffd', '#d210fd', '#d410fd', '#d611fd',
       '#d911fd', '#db12fd', '#dd12fd', '#df13fd']


def setup():
    size(1900, 1000)
    #no_stroke()
    background("#FFFFFF")
    fill("#FFFFFF")

def draw():
    background("#FFFFFF")
    for i in range(100):
        stroke(hexArr[i])
        fill(hexArr[i])
        ellipse((10+19*i), 500, 10, arr[i])
    no_loop()
    save_frame(filename=outfilename)
    exit()

def readData():
    fs, data = wavfile.read(filename)
    return data


def makeChunks(data):
    chunks = []
    for i in range(0,len(data),len(data)//100):
        chunks.append(data[i:i+(len(data)//100)])
    return chunks

def calculateAverages(chunks):
    averages = []
    for each in chunks:
        avg_x = np.average(each[:,0])
        avg_y = np.average(each[:,1])
        averages.append([avg_x,avg_y])
    return averages
    
def calculateHeights(averages):
    heights = []
    for each in averages:
        diff = abs(each[0]-each[1])
        heights.append(diff)
    return heights

def scaleHeights(heights):
    old_min = min(heights)
    old_max = max(heights)
    new_max = 500
    new_min = 100
    newHeights = []
    for each in heights:
        new_value = ( (each - old_min) / (old_max - old_min) ) * (new_max - new_min) + new_min
        newHeights.append(new_value)
    return newHeights



# p5 supports different backend to render sketches, viz "vispy" for both 2D and 3D sketches and "skia" for 2D sketches
# Default renderer is set to "vispy"
#run()


if __name__ == "__main__":
   #global filename
    filename = sys.argv[1]
    data = readData()
    chunks = makeChunks(data)
    averages = calculateAverages(chunks)
    heights = calculateHeights(averages)
    scaledHeights = scaleHeights(heights)
   # global arr
    arr = scaledHeights
   # global outfilename
    outfilename = filename.split('.')[0] + ".png"
    run()

# def main(filename):
#     filename = filename
    
#     data = readData()
#     chunks = makeChunks(data)
#     averages = calculateAverages(chunks)
#     heights = calculateHeights(averages)
#     scaledHeights = scaleHeights(heights)
#     arr = scaledHeights

#     outfilename = filename.split('.')[0] + ".png"
#     run()
