
import numpy as np
import cv2
from skimage import measure
from collections import Counter
from collections import deque


def capture_masks(video_clip, count=5, show_vid=False, verbose=True):
    assert count != 0, 'Must capture at least 1 mask'
    
    cap = cv2.VideoCapture(video_clip)
    if verbose:
        print "video access: complete"
    fgbg = cv2.BackgroundSubtractorMOG()
    
    mask_storage = deque(maxlen=count)
    while(1):
        ret, frame = cap.read()
        if frame is None:
            # video has ended
            break
        
        fgmask = fgbg.apply(frame)
        if len(mask_storage) == count:  # full
            mask_storage.popleft()
        mask_storage.append(fgmask)
        
        if show_vid:
            cv2.imshow('frame', fgmask)
            k = cv2.waitKey(30) & 0xff
            if k == 27:  # esc to stop 
                break
    
    if verbose:
        print "video analysis: complete"
    cap.release()
    cv2.destroyAllWindows()    
    
    result = list(mask_storage)
    return result


def v1_ppl_counter(mask, min_size, max_size):
    labelled_mask = measure.label(mask)
    sizer = Counter([item for row in labelled_mask for item in row])
    result = 0
    for blob_id, size in sizer.items():
        if size >= min_size and size <= max_size:
            result += 1
    return result


def agg_ppl_counter(masks, count_func, agg_func=np.mean):
    return agg_func(map(count_func, list(masks)))



# data comes in a dict of {locname: 'video_path', longitude, latitude}
# output {locname: time, count}
data = {}
data['tsrobo1'] = ('testclip.mp4', 40.7577, 73.9857) #http://www.earthcam.com/usa/newyork/timessquare/?cam=tsrobo1

def prep_counts(data, out_path):

    for locname, details in data:
        video_path,_,_ = details
        masks = capture_masks('testclip2.mp4')
        count_func = lambda x: v1_ppl_counter(x, 20, 100)
        agg_ppl_counter(masks, count_func)

	
