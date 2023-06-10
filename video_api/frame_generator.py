import cv2
from pathlib import Path


def generate_frames(video_path):
    VIDEO_PATH = Path(video_path) if isinstance(video_path, str) else video_path
    if not VIDEO_PATH.is_file():
       raise Exception("Input video not found!")
    VideoCapture = cv2.VideoCapture(str(VIDEO_PATH))
    frame_number = 0
    while True:
        success, FRAME_BGR = VideoCapture.read()
        if not success:
            break
        FRAME_RGB = cv2.cvtColor(FRAME_BGR, cv2.COLOR_BGR2RGB)
        yield {"number": frame_number,  "bgr": FRAME_BGR, "rgb": FRAME_RGB}
        frame_number += 1
    # Loop ended. Release
    VideoCapture.release()
