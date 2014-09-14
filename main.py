
from __future__ import division
import pandas as pd
import numpy as np
import cv2
from skimage import measure
from collections import Counter
from datetime import datetime, timedelta

def color_func(blob_id, people_blob_ids):
    ''' Color the blobs identified as people blue. '''
    if blob_id == 0:  # background
        return [0, 0, 0]  # black
    if blob_id in people_blob_ids:
        return [0, 255, 0]  # blue
    else:  # non-person blob
        return [255, 255, 255] # white


def v1_ppl_counter(mask, min_size, max_size):
    labelled_mask = measure.label(mask)
    sizer = Counter([item for row in labelled_mask for item in row])

    people_blob_ids = []
    for blob_id, size in sizer.items():
        if size >= min_size and size <= max_size:
            people_blob_ids.append(blob_id)

    colored_mask = np.array([[color_func(pixel, people_blob_ids)
                                for pixel in row] for row in labelled_mask])
    return len(people_blob_ids), colored_mask.astype(dtype = 'uint8')


def process_mask(fgbg, frame):
    fgmask = fgbg.apply(frame)
    count, colored_mask = v1_ppl_counter(fgmask, 20, 200)
    return count, colored_mask


def process_video(in_path,
                  out_path,
                  show_vid=False,
                  verbose=True):
    ''' Creates mask video and generates counts. '''

    # initialize everything
    if verbose:
        print "Accessing video %s" % in_path
    cap = cv2.VideoCapture(in_path)

    fgbg = cv2.BackgroundSubtractorMOG()
    frame_counter = 1  # start at 1 because first frame used for sizing
    count_storage = []

    if verbose:
        print "Sizing first frame"
    ret, frame = cap.read()
    height, width, layers = frame.shape
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    video = cv2.VideoWriter(out_path,
                            fourcc,
                            20.0,
                            (width, height),
                            1)  # in color
    count, mask = process_mask(fgbg, frame)
    #video.write(frame)
    count_storage.append(count)

    if verbose:
        print "Commencing frame-by-frame analysis"

    while(1):
        ret, frame = cap.read()
        if not ret:
            print "Video ended"
            break

        frame_counter += 1
        print frame_counter
        count, mask = process_mask(fgbg, frame)
        video.write(frame)
        count_storage.append(count)

        if show_vid:
            cv2.imshow('frame', mask)
            k = cv2.waitKey(30) & 0xff
            if k == 27:  # esc to stop
                print "Manual escape"
                break

    if verbose:
        print "Closing connections"
    cap.release()
    video.release()
    cv2.destroyAllWindows()

    return np.array(count_storage)

def process_counts(counts, clip_time):
    rolling_count = pd.rolling_mean(count_storage, 5)
    frames = len(counts)
    ts = np.arange(1, frames+1)/frames * clip_time
    return zip(ts, rolling_count)

# Insert some data
# data comes in a dict of {locname: 'video_path', longitude, latitude}
# output {locname: time, count}
data = {}
data['tsrobo1'] = ('tsrobo1.mp4', 40.7577, 73.9857)
     # http://www.earthcam.com/usa/newyork/timessquare/?cam=tsrobo1
clip_time = 301  # seconds
result_dict = {}

for locname, details in data.items():
    path, _, _ = details
    count_storage = process_video(path, 'test.mp4', show_vid=False)
    result = process_counts(count_storage, clip_time)
    result_dict[locname] = result
