import cv2, time

print('BAD APPLE INIT')

file_path="bad-apple.mp4"

video=cv2.VideoCapture(file_path)

def get_video_dimentions(video_file):
    width=int(video_file.get(cv2.CAP_PROP_FRAME_WIDTH))
    height=int(video_file.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return width,height

def run_filter_over_frame(frame, video_file, white_cutoff=100):
    video_file.set(cv2.CAP_PROP_POS_FRAMES, frame)
    ret,frameimg=video_file.read()
    for pixely in range(len(frameimg)):
        for pixelx in range(len(frameimg[pixely])):
            if frameimg[pixely][pixelx][0]>white_cutoff:
                frameimg[pixely][pixelx]=[223,223,223]
            else:
                frameimg[pixely][pixelx]=[0,253,0]
    return frameimg

frame_count=int(cv2.VideoCapture.get(video, cv2.CAP_PROP_FRAME_COUNT))
width,height=get_video_dimentions(video)

new_video=cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height))

for i in range(0, frame_count-1):
    filtered_frame=run_filter_over_frame(i,video)
    cv2.imshow("Image", filtered_frame)
    cv2.waitKey(1)
    new_video.write(filtered_frame)

    


new_video.release()

video.release()
cv2.destroyAllWindows()