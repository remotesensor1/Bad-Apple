import cv2, time
print('BAD APPLE INIT')

file_path="bad-apple.mp4"
video=cv2.VideoCapture(file_path)
target_frame=100
video.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
print(video.read())

input('INIT VIDEO READ COMPLETE\nPRESS ENTER TO CONTINUE')
ret,frame=video.read()

cv2.imshow("Image", frame)

cv2.waitKey(2000)

input('IMAGE RENDERED\n APPLYING COLOR FILTER\nPRESS ENTER TO CONTINUE')

new_frame=frame.copy()

frame_stats=(len(new_frame[0]),len(new_frame))

print('FRAME STATS: ',frame_stats)

for pixely in range(len(new_frame)):
    for pixelx in range(len(new_frame[pixely])):
        if new_frame[pixely][pixelx][0]>100:
            new_frame[pixely][pixelx]=[2,253,253]
        else:
            new_frame[pixely][pixelx]=[0,253,0]


cv2.imshow("Image", new_frame)

cv2.waitKey(10000)

video.release()
cv2.destroyAllWindows()

