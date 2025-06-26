from import_lib import *
from global_variables import *
from detect import *
from extract_feature import *

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    imgHand, x, y, w, h = detect_hand(img)
    if imgHand is not None:
        # cv2.imshow("ImageHand", imgHand)
    
        # Predict
        feature = extract_feature_mobile_net_v2(imgHand)
        prob = classify_model.predict(feature) # Softmax output
        prediction = np.argmax(prob, axis=1)[0]
        print(prediction)

        # Thêm vào buffer
        prediction_buffer.append(prediction)
        # Lấy nhãn xuất hiện nhiều nhất
        most_common = Counter(prediction_buffer).most_common(1)[0][0]
        
        # Draw rectangle
        cv2.rectangle(imgOutput, (x - offset, y - offset-50), (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput, label[most_common], (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(imgOutput, (x-offset, y-offset), (x + w+offset, y + h+offset), (255, 0, 255), 4)

        # cv2.imshow("Hand", remove_background(imgHand))
    else:
       print("No Hand")
    
    cv2.imshow("Image", imgOutput)

    # Instructor
    instruct_img = cv2.imread(instruct_image_dir)
    instruct_img = cv2.resize(instruct_img, (600, 800))
    cv2.imshow("Instruct", instruct_img)
    # End app
    key = cv2.waitKey(1)
    if key == ord('s'):
       break