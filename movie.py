"""
    Note: Run on Anaconda environment
    To-do: 
        - Change intro variable names with .mp4 extension
        - Push final
"""

import ffmpeg
import os

def processVideo(outputs):
    # Create dictionary of input names
    d = {}
    for output in outputs:
        d[outputs.index(output)] = output


    def get_key(val):
        for key, value in d.items():
            if val == value:
                return key

    key_list = []
    for keys in range(len(outputs)):
        key_list.append(get_key(outputs[keys]))

    #print(key_list)

    for output in d:
    # Loop this to create all inputs
        # Animation clips directory
        import os
        currentDirectory = os.getcwd()
        print (currentDirectory)
        d[output]= ffmpeg.input(currentDirectory+'/animation clips/'+d[output])

    # Loop this to concat all input videos
    concatinated = d[0]
    for output in range(len(key_list)-1):
        concatinated = ffmpeg.concat(concatinated, d[key_list[output+1]] )
        
    stream = ffmpeg.output(concatinated,currentDirectory+'/static/output.mp4')
    stream = ffmpeg.overwrite_output(stream)
    ffmpeg.run(stream)
