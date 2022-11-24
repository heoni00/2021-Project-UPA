import numpy as np
import os
from os import listdir
from random import *
import cv2 as cv
import glob

class data_augmentation():
    
    def __init__(self):
        path = os.getcwd()
        self.images_path = glob.glob('*/images/train/')[0]
        self.labels_path = glob.glob('*/labels/train/')[0]

    def resize(self, dsize):
        src = cv.imread(self.images_path+file)
        dst = cv.resize(src, dsize, interpolation=cv.INTER_LINEAR)
        cv.imwrite(self.images_path + file, dst)
    
    def mean_blur(self):
        
        mean_blur = cv.blur(src, (5,5))
        cv.imwrite(self.images_path + labelname + '_mean_blur.jpg', mean_blur)
        f = open(self.labels_path + labelname + '_mean_blur.txt','w')
        f.write(list)

    def median_blur(self):
        
        median_blur = cv.medianBlur(src, 5)
        cv.imwrite(self.images_path + labelname + '_median_blur.jpg', median_blur)
        f = open(self.labels_path + labelname + '_median_blur.txt','w')
        f.write(list)

    def Gaussian_blur(self):
        
        Gaussian_blur = cv.GaussianBlur(src, (5,5), 0)
        cv.imwrite(self.images_path + labelname + '_Gaussian_blur.jpg', Gaussian_blur)
        f = open(self.labels_path + labelname + '_Gaussian_blur.txt','w')
        f.write(list)

    def Bilateral_filter(self):
        
        Bilateral_filter = cv.bilateralFilter(src, 9, 75, 75)
        cv.imwrite(self.images_path + labelname + '_Bilateral_filter.jpg', Bilateral_filter)
        f = open(self.labels_path + labelname + '_Bilateral_filter.txt','w')
        f.write(list)

    def CLAHE(self):

        bgr = cv.imread(self.images_path+file)
        lab = cv.cvtColor(bgr, cv.COLOR_BGR2LAB)
        lab_planes = cv.split(lab)
        clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
        lab_planes[0] = clahe.apply(lab_planes[0])
        lab = cv.merge(lab_planes)
        bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)

        cv.imwrite(self.images_path + labelname + '_CLAHE.jpg', bgr)
        f = open(self.labels_path + labelname + '_CLAHE.txt', 'w')
        f.write(list)

    def flip_h(self):
        
        flip = cv.flip(src, 1)
        cv.imwrite(self.images_path + labelname + '_flip.jpg', flip)
        f = open(self.labels_path + labelname + '_flip.txt','w')
        k = list.split()
        k[1] = str(round(1 - float(k[1]),6))
        f.write(" ".join(k))

    def brightness(self, val):

        # val = 100
        array = np.full(src.shape, (val, val, val), dtype=np.uint8)    
        add = cv.add(src, array)
        sub = cv.subtract(src, array)
        cv.imwrite(self.images_path + labelname + '_add{}.jpg'.format(str(val)), add)
        f = open(self.labels_path + labelname + '_add{}.txt'.format(str(val)),'w')
        f.write(list)

        cv.imwrite(self.images_path + labelname + '_sub{}.jpg'.format(str(val)), sub)
        f = open(self.labels_path + labelname + '_sub{}.txt'.format(str(val)),'w')
        f.write(list)
    
    def cutout(self, k):
        
        for i in range(k):
            cbox = list.split(' ')
            x_center = float(cbox[1])
            y_center = float(cbox[2])
            width = float(cbox[3])*a
            height = float(cbox[4])*b
            x_center_new = x_center*a
            y_center_new = y_center*b

            x1=uniform(x_center_new-width/2, x_center_new +width/4)
            y1=uniform(y_center_new-height/2, y_center_new +height/4)
            mark = width/4
            x2 = x1 + mark
            y2 = y1 + mark
            
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)

            cout = cv.rectangle(src, (x1,y1), (x2,y2), (0, 0, 0), cv.FILLED)
            
        cv.imwrite(self.images_path + labelname + '_cutout{}.jpg'.format(str(k)), cout)
        f = open(self.labels_path + labelname + '_cutout{}.txt'.format(str(k)),'w')
        f.write(list)
 
    def gray_scale(self):

        gray = cv.imread(self.images_path+file, cv.IMREAD_GRAYSCALE)
        cv.imwrite(self.images_path + labelname + '_gray.jpg', gray)
        f = open(self.labels_path + labelname + '_gray.txt','w')
        f.write(list)
    
    def noise(self, p):

        gray = cv.imread(self.images_path+file, cv.IMREAD_GRAYSCALE)
        output = np.zeros(src.shape, np.uint8)
        thres = 1 - p
        for i in range(gray.shape[0]):
            for j in range(gray.shape[1]):
                rdn = random()
                if rdn < p:
                    output[i][j] = 0
                
                elif rdn > thres:
                    output[i][j] = 255
                
                else:
                    output[i][j] = gray[i][j]
        cv.imwrite(self.images_path + labelname + '_noise{}.jpg'.format(str(p)), output)
        f = open(self.labels_path + labelname + '_noise{}.txt'.format(str(p)),'w')
        f.write(list)    
    
    def rotation(self, angle):

        #convert from Yolo_mark to opencv format
        def yoloFormattocv(x1, y1, x2, y2, H, W):
            bbox_width = x2 * W
            bbox_height = y2 * H
            center_x = x1 * W
            center_y = y1 * H
            voc = []
            voc.append(center_x - (bbox_width / 2))
            voc.append(center_y - (bbox_height / 2))
            voc.append(center_x + (bbox_width / 2))
            voc.append(center_y + (bbox_height / 2))
            return [int(v) for v in voc]

        
        height, width = src.shape[:2]  # image shape has 3 dimensions
        image_center = (width / 2,
                        height / 2)  # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape
        rotation_mat = cv.getRotationMatrix2D(image_center, angle, 1.)
        # rotation calculates the cos and sin, taking absolutes of those.
        abs_cos = abs(rotation_mat[0, 0])
        abs_sin = abs(rotation_mat[0, 1])
        # find the new width and height bounds
        bound_w = int(height * abs_sin + width * abs_cos)
        bound_h = int(height * abs_cos + width * abs_sin)
        # subtract old image center (bringing image back to origin) and adding the new image center coordinates
        rotation_mat[0, 2] += bound_w / 2 - image_center[0]
        rotation_mat[1, 2] += bound_h / 2 - image_center[1]
        # rotate image with the new bounds and translated rotation matrix
        rotated_mat = cv.warpAffine(src, rotation_mat, (bound_w, bound_h))
        

        rotation_angle = angle * np.pi / 180
        rot_matrix = np.array([[np.cos(rotation_angle), -np.sin(rotation_angle)], [np.sin(rotation_angle), np.cos(rotation_angle)]])


        new_height, new_width = rotated_mat.shape[:2]
        new_bbox = []

        b_H, b_W = src.shape[:2]

        bbox = list.split(' ')


        (center_x, center_y, bbox_width, bbox_height) = yoloFormattocv(float(bbox[1]), float(bbox[2]),
                                                                    float(bbox[3]), float(bbox[4]), b_H, b_W)
        upper_left_corner_shift = (center_x - b_W / 2, -b_H / 2 + center_y)
        upper_right_corner_shift = (bbox_width - b_W / 2, -b_H / 2 + center_y)
        lower_left_corner_shift = (center_x - b_W / 2, -b_H / 2 + bbox_height)
        lower_right_corner_shift = (bbox_width - b_W / 2, -b_H / 2 + bbox_height)
        new_lower_right_corner = [-1, -1]
        new_upper_left_corner = []
        for i in (upper_left_corner_shift, upper_right_corner_shift, lower_left_corner_shift,
                lower_right_corner_shift):
            new_coords = np.matmul(rot_matrix, np.array((i[0], -i[1])))
            x_prime, y_prime = new_width / 2 + new_coords[0], new_height / 2 - new_coords[1]
            if new_lower_right_corner[0] < x_prime:
                new_lower_right_corner[0] = x_prime
            if new_lower_right_corner[1] < y_prime:
                new_lower_right_corner[1] = y_prime
            if len(new_upper_left_corner) > 0:
                if new_upper_left_corner[0] > x_prime:
                    new_upper_left_corner[0] = x_prime
                if new_upper_left_corner[1] > y_prime:
                    new_upper_left_corner[1] = y_prime
            else:
                new_upper_left_corner.append(x_prime)
                new_upper_left_corner.append(y_prime)
        #             print(x_prime, y_prime)
        new_bbox.append([bbox[0], new_upper_left_corner[0], new_upper_left_corner[1],
                        new_lower_right_corner[0], new_lower_right_corner[1]])


        # Convert from opencv format to yolo format
        # H,W is the image height and width
        corner = new_bbox[0]
        c_H = rotated_mat.shape[0]
        c_W = rotated_mat.shape[1]
        bbox_W = corner[3] - corner[1]
        bbox_H = corner[4] - corner[2]
        center_bbox_x = (corner[1] + corner[3]) / 2
        center_bbox_y = (corner[2] + corner[4]) / 2
        cvFormattoYolo =  corner[0], round(center_bbox_x /c_W, 6),round(center_bbox_y / c_H, 6),round(bbox_W / c_W, 6),round(bbox_H / c_H, 6)

        
        cv.imwrite(self.images_path + labelname + '_rotation{}.jpg'.format(str(angle)), rotated_mat)
        f = open(self.labels_path + labelname + '_rotation{}.txt'.format(str(angle)),'w')
        f.write(' '.join(map(str, cvFormattoYolo)))


if __name__ == "__main__":
    da = data_augmentation()

    a = 618
    b = 412

    # for file in listdir(da.images_path):
    #     src = cv.imread(da.images_path+file)

    #     labelfile = file.replace('.JPG', '.txt')
    #     labelname = file.replace('.JPG', '')
    
    #     label = open(da.labels_path + labelfile, 'r')
    #     list = label.readline()
        
    #     da.resize(dsize=(a,b))        

    for file in listdir(da.images_path):
        src = cv.imread(da.images_path+file)

        labelfile = file.replace('.JPG', '.txt')
        labelname = file.replace('.JPG', '')
    
        label = open(da.labels_path + labelfile, 'r')
        list = label.readline()

        da.mean_blur()
        da.median_blur()
        da.Gaussian_blur()
        da.Bilateral_filter()
        da.CLAHE()
        da.flip_h()
        da.brightness(val = 10)
        da.brightness(val = 20)
        da.brightness(val = 30)
        da.gray_scale()
        da.noise(p = 0.02)
        da.rotation(angle=10)
        da.rotation(angle=20)
        da.rotation(angle=30)
        da.rotation(angle=350)
        da.rotation(angle=340)
        da.rotation(angle=330)