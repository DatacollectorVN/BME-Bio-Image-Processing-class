import cv2
import numpy as np

def controller(img, brightness=255, contrast=127):
    '''The controller function will control the Brightness and Contrast of an image 
       according to the trackbar position and return the edited image. '''
    
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
    
    # effect of brightness
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255
        else:
            shadow = 0
            max = 255 + brightness
 
        alpha_bright = (max - shadow) / 255
        gamma_bright = shadow
        
        # The function addWeighted calculates the weighted sum of two arrays
        cal = cv2.addWeighted(img, alpha_bright, img, 0, gamma_bright)
    
    # effect of contrast
    if contrast != 0:
        alpha_contrast = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        gamma_contrast = 127 * (1 - alpha_contrast)

        # The function addWeighted calculates the weighted sum of two arrays
        cal = cv2.addWeighted(cal, alpha_contrast, cal, 0, gamma_contrast)
    
    if (brightness == 0) & (contrast == 0):
        cal = img
    else:
        # putText renders the specified text string in the image.
        cv2.putText(cal, 'B:{},C:{}'.format(brightness,
                                            contrast),
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2) 
    
    return cal