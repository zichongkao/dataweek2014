
import numpy as np
import cv2
from skimage import measure
from collections import Counter

def color_func(blob_id, people_blob_ids):
    ''' Color the blobs identified as people blue. '''
    if blob_id = 0:  # background
        return [0, 0, 0]  # black
    if blob_id in people_blob_ids:
        return [0, 0, 255]  # blue
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
    return len(people_blob_ids), colored_mask


def process_mask(fgbg, frame):
    fgmask = fgbg.apply(frame)
    count, colored_mask = v1_ppl_counter(fgmask, 20, 100)
    return count, colored_mask


def process_video(in_path,
                  out_path,
                  seconds,
                  show_vid=False,
                  verbose=True):
    ''' Creates mask video and generates counts. '''

    assert agg_lvl > 0, 'Must aggregate at least 1 frame'

    # initialize everything
    if verbose:
        print "Accessing video %s" % in_path
    cap = cv2.VideoCapture(video_clip)

    fgbg = cv2.BackgroundSubtractorMOG()
    frame_counter = 1  # start at 1 because first frame used for sizing
    count_storage = []

    if verbose:
        print "Sizing first frame"
    ret, frame = cap.read()
    height, width, layers = frame.shape
    video = cv2.VideoWriter(out_path, -1, 1, (width,height))
    count, mask = process_mask(fbgb, frame)
    video.write(mask)
    count_storage.append(count)

    if verbose:
        print "Commencing frame-by-frame analysis"

    while(1):
        ret, frame = cap.read()
        if frame is None:
            # video has ended
            break

        frame_counter += 1
        count, mask = process_mask(fbgb, frame)
        video.write(mask)
        count_storage.append(count)

        if show_vid:
            cv2.imshow('frame', fgmask)
            k = cv2.waitKey(30) & 0xff
            if k == 27:  # esc to stop 
                break

    if verbose:
        print "Closing connections"
    cap.release()
    video.release()
    cv2.destroyAllWindows()

    return count_storage



# Insert some data
# data comes in a dict of {locname: 'video_path', longitude, latitude}
# output {locname: time, count}
data = {}
data['tsrobo1'] = ('testclip.mp4', 40.7577, 73.9857) #http://www.earthcam.com/usa/newyork/timessquare/?cam=tsrobo1

for locname, details in data:
    
	
