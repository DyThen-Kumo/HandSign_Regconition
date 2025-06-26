from import_lib import *
from global_variables import *
from detect import *
# from extract_feature import *

cap = cv2.VideoCapture(0)
save_folder = r'C:\D\UIT\HOC KI 6\CS431\HandSign\data_gen'
char = 'del'
i = 1

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    imgHand, x, y, w, h = detect_hand(img)
    if imgHand is not None:
        cv2.rectangle(imgOutput, (x-offset, y-offset), (x + w+offset, y + h+offset), (255, 0, 255), 4)

        cv2.imshow("Hand", imgHand)
    else:
       print("No Hand")
    
    cv2.imshow("Image", imgOutput)

    # Instructor
    instruct_img = cv2.imread(instruct_image_dir)
    instruct_img = cv2.resize(instruct_img, (600, 800))
    cv2.imshow("Instruct", instruct_img)
    # End app
    key = cv2.waitKey(1)
    if key == ord('q') and i < 1001:
        save_path = os.path.join(save_folder, char)
        os.makedirs(save_path, exist_ok=True)
        save_dir = os.path.join(save_path, f"{char}_{i}.jpg")
        i += 1
        print(save_dir)
        cv2.imwrite(save_dir, imgHand)
    if key == ord('s'):
       break