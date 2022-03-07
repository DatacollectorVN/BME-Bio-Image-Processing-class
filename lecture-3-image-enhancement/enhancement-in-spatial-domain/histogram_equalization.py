import cv2
import argparse

''' EXPLAIN:
Source: https://stackoverflow.com/questions/31998428/opencv-python-equalizehist-colored-image

Histogram Equalization (HE) is a statistical approach for spreading out intensity values. 
In image processing, HE is used for improving the contrast of any image, that is- to make 
the dark portion darker and the bright portion brighter.

For a grey-scale image, each pixel is represented by the intensity value (brightness); 
that is why we can feed the pixel values directly to the HE function. However, that is not how 
it works for an RGB-formatted color image. Each channel of the R, G, and B represents the intensity 
of the related color, not the intensity/brightness of the image as a whole. And so, running HE on 
these color channels is NOT the proper way.

We should first separate the brightness of the image from the color and then run HE on the brightness. 
Now, there are already standardized colorspaces that encode brightness and color separately, 
like- YCbCr, HSV, etc.; so, we can use them here for separating and then re-merging the brightness. 

The proper way:
Convert the colorspace from RGB to YCbCr >> Run HE on the Y channel (this channel represents brightness) 
>> Convert back the colorspace to RGB

'''
def main(image_file_path):
    img_ori = cv2.imread(image_file_path)
    img_clone = img_ori.copy()
    
    # convert from RGB color-space to YCrCb
    img_ycrcb = cv2.cvtColor(img_clone, cv2.COLOR_BGR2YCrCb)

    # equalize the histogram of the Y channel
    img_ycrcb[:, :, 0] = cv2.equalizeHist(img_ycrcb[:, :, 0])

    # convert back to RGB color-space from YCrCb
    equalized_img = cv2.cvtColor(img_ycrcb, cv2.COLOR_YCrCb2BGR)

    while True:
        cv2.imshow("image before", img_ori)
        cv2.imshow("image after", equalized_img)
        key = cv2.waitKey(0)
        
        # close all if press ESC
        if key == 27: 
            break

    cv2.destroyallwindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagepath", dest = "image_file_path", type = str,
                        default = None, help = "Image file path")
    args = parser.parse_args()
    image_file_path = args.image_file_path
    main(image_file_path)
