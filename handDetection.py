import cv2
from cvzone.HandTrackingModule import HandDetector

captureVideo=cv2.VideoCapture(0)

detector=HandDetector(detectionCon=0.8)

while True:
    try:
        check,image=captureVideo.read()
        # print(image)
        cameraFlipedImage=cv2.flip(image,1)
        handsDetector=detector.findHands(cameraFlipedImage,flipType=False)
        hands=handsDetector[0]
        # print(hands)
        
        if hands:
            hand1=hands[0]
            lmList1=hand1['lmList']
            handType1=hand1['type']

            fingers1=detector.fingersUp(hand1)
            print(fingers1)

            currentFingerUp=""

            if fingers1[0] == 1:
                currentFingerUp="Thumb Finger"
            elif fingers1[1] == 1:
                currentFingerUp="Index Finger"
            elif fingers1[2] == 1:
                currentFingerUp="Middle Finger"
            elif fingers1[3] == 1:
                currentFingerUp="Ring Finger"
            elif fingers1[4] == 1:
                currentFingerUp="Pinkie"
            else:
                currentFingerUp=""
            
            cv2.putText(cameraFlipedImage,handType1+": "+currentFingerUp,(75,50), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

            hand2=hands[0]
            lmList2=hand2['lmList']
            handType2=hand2['type']

            fingers2=detector.fingersUp(hand2)
            print(fingers2)

            currentFingerUp2=""

            if fingers2[0] == 1:
                currentFingerUp2="Thumb Finger"
            elif fingers2[1] == 1:
                currentFingerUp2="Index Finger"
            elif fingers2[2] == 1:
                currentFingerUp2="Middle Finger"
            elif fingers2[3] == 1:
                currentFingerUp2="Ring Finger"
            elif fingers2[4] == 1:
                currentFingerUp2="Pinkie"
            else:
                currentFingerUp2=""

            cv2.putText(cameraFlipedImage,handType2+": "+currentFingerUp2,(75,100), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)    

    except Exception as e:
        print(e)
    # cv2.imshow("mypic",image)
    cv2.imshow("mypicfliped",cameraFlipedImage)
    if cv2.waitKey(1) == 32:
       break
captureVideo.release()
