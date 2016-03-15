from collections import namedtuple

LED_Detection = namedtuple("LED_Detection",
                           "timestamp1 "  # first timestamp
                           "timestamp2 "  # second timestamp
                           "image_coordinates "  # in (y, x) = [0,1]x[0,1]
                           "frequency "  # > 0
                           "color "  # [r, g, b]
                           "confidence "  # float
                           )


def detect_led(images,
               mask,
               frequencies_to_detect,
               min_distance_between_LEDs_pixels):
    """ 
        images: numpy array        
        images.shape = (nimages,)
        data.dtype # [('timestamp', '<f8'), ('rgb', 'u1', (480, 640, 3))]

        mask: array of bool (H, W) 
            mask[u,v] is 1 if we need to look at that pixel
            
        frequencies_to_detect:
            list of floats 

        returns:
            list of LED detections
    """


