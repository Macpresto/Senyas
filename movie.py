'''
from moviepy.editor import *
 
# loading video dsa gfg intro video
clip = VideoFileClip("C:\\Users\\Mac\\Desktop\\moviepy\\hey hi hello.mp4")
clip2 = VideoFileClip("C:\\Users\\Mac\\Desktop\\moviepy\\magandang umaga.mp4")

# concatenating both the clips
final = concatenate_videoclips([clip, clip2])

#writing the video into a file / saving the combined video
#final.write_videofile("C:\\Users\\Mac\\Desktop\\moviepy\\merged.mp4")
 
moviepy.video.io.ffmpeg_tools.ffmpeg_merge_video_audio(video, audio, output, vcodec='copy', acodec='copy', ffmpeg_output=False, logger='bar')
'''
import ffmpeg
video1 = ffmpeg.input('C:\\Users\\Mac\\Desktop\\moviepy\\hey hi hello.mp4')

video2 = ffmpeg.input('C:\\Users\\Mac\\Desktop\\moviepy\\magandang umaga.mp4')


ffmpeg.concat(video1, video2, v=2).output('C:\\Users\\Mac\\Desktop\\moviepy\\out.mp4').run()