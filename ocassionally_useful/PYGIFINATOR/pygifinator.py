from moviepy.editor import *  # Fetching  our video manipulation library
import argparse  # package for using command line arguments

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="path to clip to be converted")
ap.add_argument("-t1", "--start", default = 0,
                help="time from which gif starts")
ap.add_argument("-t2", "--end", default = 4, help="time from which gif ends")
args = vars(ap.parse_args())


input_video = VideoFileClip(args['video'])  # loading the video
# Selecting a subclip from the video between t1 and t2 seconds
crop_clip = input_video.subclip(args['start'], args['end'])
# Convert the cropped clip as a gif
crop_clip.write_gif("./output.gif")
