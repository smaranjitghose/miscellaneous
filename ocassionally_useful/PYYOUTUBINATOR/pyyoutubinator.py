from pytube import YouTube  # Fetching  our youtube play around video
import argparse  # package for using command line arguments

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=True,
                help="link to the youtube video")
ap.add_argument("-d", "--download", default=True, help="Download video")
ap.add_argument("-n", "--name", default=False, help="Display Name")
ap.add_argument("-t", "--thumbnail", default=False, help="Get Thumbnail")
args = vars(ap.parse_args())

given_video = YouTube(args['url'])

if args["name"]:
    print(f"Title of Video is {given_video.title}")
if args["thumbnail"]:
    print(f"Thumbnail URL: {given_video.thumbnail_url}")
if args["download"]:
    high_res_vid = given_video.streams.get_highest_resolution().download()
