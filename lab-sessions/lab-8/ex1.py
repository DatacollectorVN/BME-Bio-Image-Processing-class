import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.feature import match_template
import argparse

def main(image_file_path, image_temp_file_path):
    image = cv2.imread(image_file_path, 0)
    template = cv2.imread(image_temp_file_path, 0)
    result = match_template(image, template)
    ij = np.unravel_index(np.argmax(result), result.shape)
    x, y = ij[::-1]
    fig = plt.figure(figsize=(8, 3))
    ax1 = plt.subplot(1, 3, 1)
    ax2 = plt.subplot(1, 3, 2)
    ax3 = plt.subplot(1, 3, 3)
    ax1.imshow(template, cmap=plt.cm.gray)
    ax1.set_axis_off()
    ax1.set_title('template')
    ax2.imshow(image, cmap=plt.cm.gray)
    ax2.set_axis_off()
    ax2.set_title('image')
    # highlight matched region
    height_template, width_template = template.shape
    rect = plt.Rectangle((x, y), width_template, height_template,

    edgecolor='r', facecolor='none')

    ax2.add_patch(rect)
    ax3.imshow(result)
    ax3.set_axis_off()
    ax3.set_title('match_template result')
    ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none',
    markersize=10)
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--imagepath", dest = "image_file_path", type = str,
                        default = None, help = "Image file path")
    parser.add_argument("--imagetemppath", dest = "image_temp_file_path", type = str,
                        default = None, help = "Image file template path")
    args = parser.parse_args()
    image_file_path = args.image_file_path
    image_temp_file_path = args.image_temp_file_path
    main(image_file_path, image_temp_file_path)