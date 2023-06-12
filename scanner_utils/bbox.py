
import cv2
from pathlib import Path
import numpy as np
from PIL import ImageFont, ImageDraw, Image



def get_iou(bbox1, bbox2):
    bb1 = {'x1': bbox1[0], 'y1': bbox1[1], 'x2': bbox1[2], 'y2':bbox1[3] }
    bb2 = {'x1': bbox2[0], 'y1': bbox2[1], 'x2': bbox2[2], 'y2':bbox2[3] }
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters
    ----------
    bb1 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x1, y1) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner
    bb2 : dict
        Keys: {'x1', 'x2', 'y1', 'y2'}
        The (x, y) position is at the top left corner,
        the (x2, y2) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """
    assert bb1['x1'] < bb1['x2']
    assert bb1['y1'] < bb1['y2']
    assert bb2['x1'] < bb2['x2']
    assert bb2['y1'] < bb2['y2']

    # determine the coordinates of the intersection rectangle
    x_left = max(bb1['x1'], bb2['x1'])
    y_top = max(bb1['y1'], bb2['y1'])
    x_right = min(bb1['x2'], bb2['x2'])
    y_bottom = min(bb1['y2'], bb2['y2'])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    # compute the area of both AABBs
    bb1_area = (bb1['x2'] - bb1['x1']) * (bb1['y2'] - bb1['y1'])
    bb2_area = (bb2['x2'] - bb2['x1']) * (bb2['y2'] - bb2['y1'])

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = intersection_area / float(bb1_area + bb2_area - intersection_area)
    assert iou >= 0.0
    assert iou <= 1.0
    return iou



def draw_bboxes(cv_image, instances):
    """
    Draws bounding boxes with class labels and confidence scores on a given input image.
    format : [ [label, score, [ x1, y1, x2, y2 ]] ]
    """
    FONT_FACTOR = 20/1000
    BOX_FACTOR = 4/1000
    FONT_PATH = Path("src/static/Helvetica.ttf")
    HEIGHT, WIDTH, _ = cv_image.shape
    FONT_SCALE = int(min(HEIGHT, WIDTH) * FONT_FACTOR)
    BOX_SCALE = int(min(HEIGHT, WIDTH) * BOX_FACTOR)
    for instance in instances:
        x1, y1, x2, y2 = [int(v) for v in instance[2]]
        score = round(instance[1],1)*100 if instance[1] > 0 else None
        caption = f"{instance[0]} {score}%" if score else f"{instance[0]}"
        color = (255,0,255)
        cv2.rectangle(cv_image, (x1, y1), (x2, y2), color, BOX_SCALE)
        # Text Bg
        font = ImageFont.truetype(str(FONT_PATH) , FONT_SCALE)
        img_pil = Image.fromarray(cv_image)
        draw = ImageDraw.Draw(img_pil)
        text_bg = draw.textbbox((x1, y1), caption, font=font)
        draw.rectangle(text_bg, fill=(0,0,0))
        draw.text((x1, y1), caption, font = font, fill = (255, 255, 255, 0))
        cv_image = np.array(img_pil)
    return cv_image


def get_bbox_height(bbox):
    return bbox[3]- bbox[1]