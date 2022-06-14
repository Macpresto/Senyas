#run on anaconda environment
#to do:
#chanage intro variable names with .mp4 extension
#push final


import ffmpeg
import os



def processVideo(outputs):

    
    #create dictionary of input names
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
    #loop this to create all inputs
        #animation clips directory
        import os
        currentDirectory = os.getcwd() + '\Thesis'
        print (currentDirectory)
        d[output]= ffmpeg.input(currentDirectory+'\\animation clips\\'+d[output])
        #d[output] = ffmpeg.input('C:\\Users\\Mc\\Documents\\THESIS FILES\\animation clips\\2.mp4')

    #loop this to concat all input videos
    concatinated = d[0]
    for output in range(len(key_list)-1):
        concatinated = ffmpeg.concat(concatinated, d[key_list[output+1]] )
        
    stream = ffmpeg.output(concatinated,currentDirectory+'\\static\\output.mp4')
    stream = ffmpeg.overwrite_output(stream)
    ffmpeg.run(stream)

