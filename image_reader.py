import cv2, time

print('BAD APPLE INIT')

file_path="bad-apple.mp4"

video=cv2.VideoCapture(file_path)

def run_filter_over_frame(frame, video_file, white_cutoff=100):
    video_file.set(cv2.CAP_PROP_POS_FRAMES, frame)
    ret,frameimg=video_file.read()
    for pixely in range(len(frameimg)):
        for pixelx in range(len(frameimg[pixely])):
            if frameimg[pixely][pixelx][0]>white_cutoff:
                frameimg[pixely][pixelx]=[2,253,253]
            else:
                frameimg[pixely][pixelx]=[0,253,0]
    return frameimg

run_filter_over_frame(100,video)

cv2.imshow("Image", run_filter_over_frame(100,video))

cv2.waitKey(10000)

video.release()
cv2.destroyAllWindows()