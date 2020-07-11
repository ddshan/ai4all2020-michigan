import cv2
import numpy as np

if __name__ == '__main__':

    im = np.ones((510, 510))
    for i in range(0, 512, 2):
        im[:, i:i+2] = i // 2
        
    cv2.imwrite('gradient.png', im)
    print(im)

        
