import cv2
import numpy as np
# from knn import KNN
from sklearn.neighbors import KNeighborsClassifier

class FindingNemo:
    def __init__(self, train_image):
        self.knn = KNeighborsClassifier(n_neighbors=3)
        X_train, Y_train = self.convert_image_to_dataset(train_image)
        self.knn.fit(X_train, Y_train)

    
    def convert_image_to_dataset(self, image):
        image = cv2.imread(image)
        if image is None:
            raise ValueError("Image not found")
        
        image_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        image_hsv_pix = image_hsv.reshape(-1,3) 

        X_train = image_hsv_pix /255

        light_color_orange = np.array([10,100,100])
        dark_color_orange = np.array([25,255,255])
        mask_orange = cv2.inRange(image_hsv,light_color_orange,dark_color_orange)

        light_color_white = np.array([10,100,100])
        dark_color_white = np.array([25,255,255])
        mask_white = cv2.inRange(image_hsv,light_color_white,dark_color_white)

        final_result = cv2.bitwise_or(mask_orange, mask_white)
        Y_train = final_result.reshape(-1,) // 255

        return X_train , Y_train

    def remove_background(self, test_image):
        image_test = cv2.imread(test_image)
        if image_test is None:
            raise ValueError("Your test image not found !")
        
        image_test_hsv = cv2.cvtColor(image_test,cv2.COLOR_BGR2HSV)
        image_test_hsv_pix = image_test_hsv.reshape(-1,3) / 255

        predict = self.knn.predict(image_test_hsv_pix)
        output = predict.reshape(image_test_hsv.shape[:2])

        return output