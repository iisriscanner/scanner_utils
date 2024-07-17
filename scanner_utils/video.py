import cv2
from pathlib import Path


# Convert framest to timecode MM:SS:MS
def frames_to_TC(fps, frames):
    h = int(frames / (fps * 3600))
    m = int(frames / (fps * 60)) % 60
    s = int(frames / fps % 60)
    f = frames % fps
    time = "%02d:%02d:%02d:%02d" % (h, m, s, f)
    return time[3:]


def get_details(video_path):
    VIDEO_PATH = Path(video_path) if isinstance(video_path, str) else video_path

    if not VIDEO_PATH.is_file():
        raise Exception("Input video not found!")

    video_capture = cv2.VideoCapture(str(VIDEO_PATH))
    video_data = {
        "name": f"{VIDEO_PATH.stem}",
        "type": f"{VIDEO_PATH.suffix[1:]}",
        "frame_count": int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT)),
        "fps": int(round(video_capture.get(cv2.CAP_PROP_FPS))),
        "width": int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        "height": int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    }
    video_capture.release()
    return video_data

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
        yield {"number": frame_number, "bgr": FRAME_BGR, "rgb": FRAME_RGB}
        frame_number += 1
    # Loop ended. Release
    VideoCapture.release()
