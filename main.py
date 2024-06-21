# import os
# import cvzone
# import cv2
# from cvzone.PoseModule  import PoseDetector


# cap = cv2.VideoCapture(0)
# detector = PoseDetector()
# shirtfolderPath = "Resources/Shirts"
# listShirts = os.listdir (shirtfolderPath)
# #print (listShirts)
# fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint11to12
# shirtRatioHeightWidth = 581 / 440
# imageNumber = 0
# imgButtonRight = cv2.imread("Resources/button.png", cv2.IMREAD_UNCHANGED)
# imgButtonLeft = cv2.flip(imgButtonRight, 1)
# counterRight = 0
# counterLeft = 0
# selectionSpeed = 10


# while True:
#     success, img = cap.read()
#     img = detector.findPose(img)
#     # img = cv2.flip(img,1)
#     lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
#     if lmList:
#         # center = bboxInfo["center"]
#         lm11 = lmList[11][1:3]
#         lm12 = lmList[12][1:3]
#         imgShirt = cv2.imread(os.path.join(shirtfolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)

#         widthOfShirt = int(abs(lm11[0] - lm12[0]) * fixedRatio)
#         heightOfShirt = int(widthOfShirt * shirtRatioHeightWidth) 
#         print(widthOfShirt)
#         imgShirt = cv2.resize(imgShirt,  (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))
#         currentScale = (lm11[0] - lm12[0]) / 190
#         offset = int(44 * currentScale), int(48 * currentScale)

#         try:
#             img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
#         except:
#             pass

#         img = cvzone.overlayPNG(img, imgButtonRight, (1074, 293))
#         img = cvzone.overlayPNG(img, imgButtonLeft, (72, 293))

#         if lmList[16][1] < 300:
#             counterRight += 1
#             cv2.ellipse(img, (139, 360), (66, 66), 0, 0,
#                         counterRight * selectionSpeed, (0, 255, 0), 20)
#             if counterRight * selectionSpeed > 360:
#                 counterRight = 0
#                 if imageNumber < len(listShirts) - 1:
#                     imageNumber += 1
#         elif lmList[15][1] > 900:
#             counterLeft += 1
#             cv2.ellipse(img, (1138, 360), (66, 66), 0, 0,
#                         counterLeft * selectionSpeed, (0, 255, 0), 20)
#             if counterLeft * selectionSpeed > 360:
#                 counterLeft = 0
#                 if imageNumber > 0:
#                     imageNumber -= 1

#         else:
#             counterRight = 0
#             counterLeft = 0
    
    
    
#     cv2.imshow("Image",img)
#     cv2.waitKey(1)
    




# import os
# import cvzone
# import cv2
# from cvzone.PoseModule import PoseDetector

# cap = cv2.VideoCapture(0)
# detector = PoseDetector()
# shirtfolderPath = "Resources/Shirts"
# listShirts = os.listdir(shirtfolderPath)

# fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint11to12
# shirtRatioHeightWidth = 581 / 440
# imageNumber = 0
# imgButtonRight = cv2.imread("Resources/button.png", cv2.IMREAD_UNCHANGED)
# imgButtonLeft = cv2.flip(imgButtonRight, 1)
# counterRight = 0
# counterLeft = 0
# selectionSpeed = 10

# while True:
#     success, img = cap.read()

#     # Check if the frame was captured successfully
#     if not success:
#         print("Error: Failed to capture frame from the webcam.")
#         break

#     img = detector.findPose(img)
#     lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)

#     if lmList:
#         lm11 = lmList[11][1:3]
#         lm12 = lmList[12][1:3]
#         imgShirt = cv2.imread(os.path.join(shirtfolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)

#         widthOfShirt = int(abs(lm11[0] - lm12[0]) * fixedRatio)
#         heightOfShirt = int(widthOfShirt * shirtRatioHeightWidth)

#         # Check if the width and height are valid
#         if widthOfShirt > 0 and heightOfShirt > 0:
#             imgShirt = cv2.resize(imgShirt, (widthOfShirt, heightOfShirt))
#         else:
#             print("Error: Invalid width or height for resizing.")

#         currentScale = (lm11[0] - lm12[0]) / 190
#         offset = int(44 * currentScale), int(48 * currentScale)

#         try:
#             img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
#         except AttributeError:
#             print("Error: overlayPNG function failed to overlay image.")

#         try:
#             img = cvzone.overlayPNG(img, imgButtonRight, (1074, 293))
#             img = cvzone.overlayPNG(img, imgButtonLeft, (72, 293))
#         except AttributeError:
#             print("Error: overlayPNG function failed to overlay button images.")

#         if lmList[16][1] < 300:
#             counterRight += 1
#             cv2.ellipse(img, (139, 360), (66, 66), 0, 0,
#                         counterRight * selectionSpeed, (0, 255, 0), 20)
#             if counterRight * selectionSpeed > 360:
#                 counterRight = 0
#                 if imageNumber < len(listShirts) - 1:
#                     imageNumber += 1
#         elif lmList[15][1] > 900:
#             counterLeft += 1
#             cv2.ellipse(img, (1138, 360), (66, 66), 0, 0,
#                         counterLeft * selectionSpeed, (0, 255, 0), 20)
#             if counterLeft * selectionSpeed > 360:
#                 counterLeft = 0
#                 if imageNumber > 0:
#                     imageNumber -= 1
#         else:
#             counterRight = 0
#             counterLeft = 0

#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# import os
# import cv2
# import cvzone
# from cvzone.PoseModule import PoseDetector

# cap = cv2.VideoCapture(0)
# detector = PoseDetector()
# shirtfolderPath = "Resources/Shirts"
# listShirts = os.listdir(shirtfolderPath)

# fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint11to12
# shirtRatioHeightWidth = 581 / 440
# imageNumber = 0
# imgButtonRight = cv2.imread("Resources/button.png", cv2.IMREAD_UNCHANGED)
# imgButtonLeft = cv2.flip(imgButtonRight, 1)
# counterRight = 0
# counterLeft = 0
# selectionSpeed = 10

# while True:
#     success, img = cap.read()

#     if not success:
#         print("Error: Failed to capture frame from the webcam.")
#         break

#     img = detector.findPose(img)
#     lmList, _ = detector.findPosition(img, bboxWithHands=False, draw=False)

#     if lmList:
#         lm11 = lmList[11][1:3]
#         lm12 = lmList[12][1:3]
#         imgShirt = cv2.imread(os.path.join(shirtfolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)

#         widthOfShirt = int(abs(lm11[0] - lm12[0]) * fixedRatio)
#         heightOfShirt = int(widthOfShirt * shirtRatioHeightWidth)

#         shirt_x = int(min(lm11[0], lm12[0]) - widthOfShirt / 2)
#         shirt_y = int(min(lm11[1], lm12[1]) - heightOfShirt / 2)

#         # Check if the shirt is within the frame
#         if shirt_x >= 0 and shirt_y >= 0 and shirt_x + widthOfShirt <= img.shape[1] and shirt_y + heightOfShirt <= img.shape[0]:
#             imgShirt_resized = cv2.resize(imgShirt, (widthOfShirt, heightOfShirt))
#             imgShirt_resized = imgShirt_resized[:min(heightOfShirt, img.shape[0] - shirt_y), :min(widthOfShirt, img.shape[1] - shirt_x)]

#             # Overlay the shirt image on the frame
#             img[shirt_y:shirt_y + imgShirt_resized.shape[0], shirt_x:shirt_x + imgShirt_resized.shape[1]] = imgShirt_resized

#         try:
#             img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for cvzone functions
#             img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)  # Convert back to BGR after overlaying
#             img = cvzone.overlayPNG(img, imgButtonRight, (1074, 293))
#             img = cvzone.overlayPNG(img, imgButtonLeft, (72, 293))
#         except AttributeError:
#             print("Error: overlayPNG function failed to overlay button images.")

#         if lmList[16][1] < 300:
#             counterRight += 1
#             cv2.ellipse(img, (139, 360), (66, 66), 0, 0,
#                         counterRight * selectionSpeed, (0, 255, 0), 20)
#             if counterRight * selectionSpeed > 360:
#                 counterRight = 0
#                 if imageNumber < len(listShirts) - 1:
#                     imageNumber += 1
#         elif lmList[15][1] > 900:
#             counterLeft += 1
#             cv2.ellipse(img, (1138, 360), (66, 66), 0, 0,
#                         counterLeft * selectionSpeed, (0, 255, 0), 20)
#             if counterLeft * selectionSpeed > 360:
#                 counterLeft = 0
#                 if imageNumber > 0:
#                     imageNumber -= 1
#         else:
#             counterRight = 0
#             counterLeft = 0

#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()




import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)
detector = PoseDetector()
shirtfolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtfolderPath)

fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint11to12
shirtRatioHeightWidth = 581 / 440
imageNumber = 0
imgButtonRight = cv2.imread("Resources/button.png", cv2.IMREAD_UNCHANGED)
imgButtonLeft = cv2.flip(imgButtonRight, 1)
counterRight = 0
counterLeft = 0
selectionSpeed = 10

while True:
    success, img = cap.read()

    # Check if the frame was captured successfully
    if not success:
        print("Error: Failed to capture frame from the webcam.")
        break

    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)

    if lmList:
        lm11 = lmList[11][1:3]
        lm12 = lmList[12][1:3]
        imgShirt = cv2.imread(os.path.join(shirtfolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)

        widthOfShirt = int(abs(lm11[0] - lm12[0]) * fixedRatio)
        heightOfShirt = int(widthOfShirt * shirtRatioHeightWidth)

        # Check if the width and height are valid
        if widthOfShirt > 0 and heightOfShirt > 0:
            imgShirt = cv2.resize(imgShirt, (widthOfShirt, heightOfShirt))
        else:
            print("Error: Invalid width or height for resizing.")

        currentScale = (lm11[0] - lm12[0]) / 190
        offset = int(44 * currentScale), int(48 * currentScale)

        try:
            img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
        except AttributeError:
            print("Error: overlayPNG function failed to overlay image.")

        try:
            img = cvzone.overlayPNG(img, imgButtonRight, (1074, 293))
            img = cvzone.overlayPNG(img, imgButtonLeft, (72, 293))
        except AttributeError:
            print("Error: overlayPNG function failed to overlay button images.")

        # Shirt change logic
        if lmList[16][1] < 300:
            counterRight += 1
            cv2.ellipse(img, (139, 360), (66, 66), 0, 0,
                        counterRight * selectionSpeed, (0, 255, 0), 20)
            if counterRight * selectionSpeed > 360:
                counterRight = 0
                imageNumber = (imageNumber + 1) % len(listShirts)  # Cycle through shirts
        elif lmList[15][1] > 900:
            counterLeft += 1
            cv2.ellipse(img, (1138, 360), (66, 66), 0, 0,
                        counterLeft * selectionSpeed, (0, 255, 0), 20)
            if counterLeft * selectionSpeed > 360:
                counterLeft = 0
                imageNumber = (imageNumber - 1) % len(listShirts)  # Cycle through shirts

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




