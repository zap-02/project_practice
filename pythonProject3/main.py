import os
import time
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from mtcnn.mtcnn import MTCNN

# draw an image with detected objects

def draw_image_with_boxes(filename, image, result_list, name):
    # load the image
    data = pyplot.imread(filename)
    # plot the image
    pyplot.imshow(data)
    # get the context for drawing boxes
    ax = pyplot.gca()
    # plot each box
    # file_to_check = open("D:/py/datacet_parameters.txt", "r")
    # text = file_to_check.read()
    # index = text.find(image)
    # file_to_check.seek(index)
    # file_to_check.readline()
    # count_of_faces = int(file_to_check.readline())
    # for line in range(1, count_of_faces + 1):
    #     s = file_to_check.readline()
    #     array = s.split(' ')
    #     x_r = int(array[0])
    #     y_r = int(array[1])
    #     width_r = int(array[2])
    #     height_r = int(array[3])
    #     # create the shape
    #     rect = Rectangle((x_r,y_r), width_r, height_r, fill=False, color='blue')
    #     # draw the box
    #     ax.add_patch(rect)
    j = 0
    for result in result_list:
        j += 1
        # get coordinates
        x, y, width, height = result['box'] #box - ?
        # create the shape
        rect = Rectangle((x,y), width, height, fill=False, color='red')
        # draw the box
        # ax.add_patch(rect)
    print("Found_faces = ", j)
    pyplot.savefig(name)
    pyplot.close()
    # show the plot
    #pyplot.show()

# def intersection_over_union(x1, y1, width1, height1, x2, y2, width2, height2):
#     # determine the (x, y)-coordinates of the intersection rectangle
#     xA = max(x1, x2)
#     yA = max(y1, y2)
#     xB = min(x1 + width1 - 1, x2 + width2 - 1)
#     yB = min(y1 + height1 - 1, y2 + height2 - 1)
#     # compute the area of intersection rectangle
#     interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
#     # compute the area of both the prediction and true rectangles
#     box1Area = width1 * height1
#     box2Area = width2 * height2
#     #compute the intersection over union
#     IoU = interArea / float(box1Area + box2Area - interArea)
#     return IoU
#
# def compare_data(image, faces, TP, TN, FP, FN):
#     file_to_check = open("D:/py/datacet_parameters.txt", "r")
#     text = file_to_check.read()
#     index = text.find(image)
#     file_to_check.seek(index)
#     file_to_check.readline()
#     count_of_faces = int(file_to_check.readline())
#     print("count_of_faces = ", count_of_faces)
#     #TP, FN
#     for line in range(1, count_of_faces + 1):
#         s = file_to_check.readline()
#         array = s.split(' ')
#         x_r = int(array[0])
#         y_r = int(array[1])
#         width_r = int(array[2])
#         height_r = int(array[3])
#         finding_rate = 0
#         max_iou = 0.0
#         num = 0
#         i = 0
#         for face in faces:
#             i += 1
#             x, y, width, height = face['box']
#             IoU = intersection_over_union(x, y, width, height, x_r, y_r, width_r, height_r)
#             if IoU > 0.5:
#                 finding_rate += 1
#                 if IoU > max_iou:
#                     max_iou = IoU
#                     num = i
#         if finding_rate == 0:
#             FN += 1
#         else:
#             TP += 1
#             faces[num - 1]['box'] = [0, 0, 0, 0]
#
#     #TN
#     if (not faces) and count_of_faces == 0:
#         TN += 1
#     #FP
#     for face in faces:
#         if face['box'] != [0, 0, 0, 0]:
#             FP += 1
#     file_to_check.close()
#     return TP, TN, FP, FN


path_of_images = "C:/py/1"
list_of_images = os.listdir(path_of_images)

full_time = 0.0
i = 0
# TP = 0
# TN = 0
# FP = 0
# FN = 0
output = open("OUTPUTFaces.txt", "w");
output.write("")
output.close()

min_face_size=20
scale_factor=0.7

detector = MTCNN(None, min_face_size, None, scale_factor)

for image in list_of_images:
    filename = os.path.join(path_of_images, image)
    # load image from file
    pixels = pyplot.imread(filename)
    # create the detector, using default weights
    # detect faces in the image and measure the time
    start_time = time.time()
    faces = detector.detect_faces(pixels)
    end_time = time.time()
    full_time += end_time - start_time
    #count of all images
    i += 1
    print(image)
    name = "C:/py/saved/" + image
    draw_image_with_boxes(filename, image, faces, name)
    # comparing data with real parameters
    # TP, TN, FP, FN = compare_data(image, faces, TP, TN, FP, FN)
    # print("TP, TN, FP, FN = ", TP, TN, FP, FN)
    # if faces:
    #     output = open("OUTPUTFaces.txt", "a");
    #     path = filename + "\n"
    #     output.write(path)
    #     output.close()
    # if i % 1000 == 0:
    #     outputStat = open("Stat.txt", "a")
    #     s = "min face size = "+str(min_face_size) + "\n"
    #     outputStat.write(s)
    #     s = "scale factor = " + str(scale_factor) + "\n"
    #     outputStat.write(s)
    #     s = image + "\n"
    #     outputStat.write(s)
    #     s = "Number of all images = " + str(i) + "\n"
    #     outputStat.write(s)
    #     s = "Average time = " + str(full_time/i) + " seconds" + "\n"
    #     outputStat.write(s)
    #     s = "Number of TP = " + str(TP) + "\n"
    #     outputStat.write(s)
    #     s = "Number of TN = " + str(TN) + "\n"
    #     outputStat.write(s)
    #     s = "Number of FP = " + str(FP) + "\n"
    #     outputStat.write(s)
    #     s = "Number of FN = " + str(FN) + "\n"
    #     outputStat.write(s)
    #     accuracy = float(TP + TN) / float(TP + TN + FP + FN) * 100
    #     s = "Accuracy = " + str(accuracy) + "%" + "\n"
    #     outputStat.write(s)
    #     outputStat.write("\n")
    #     outputStat.close()

