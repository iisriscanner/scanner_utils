import cv2
from pathlib import Path

def get_details(video_path):
    VIDEO_PATH = Path(video_path) if isinstance(video_path, str) else video_path
    
    if not VIDEO_PATH.is_file():
       raise Exception("Input video not found!")
   
    VideoCapture = cv2.VideoCapture(str(VIDEO_PATH))
    video_data = {"name": f"{VIDEO_PATH.stem}", "type": f"{VIDEO_PATH.suffix[1:]}",
            "frame_count": int(VideoCapture.get(cv2.CAP_PROP_FRAME_COUNT)), "fps": float(VideoCapture.get(cv2.CAP_PROP_FPS))}
    VideoCapture.release()
    return video_data
    