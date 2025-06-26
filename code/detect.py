from import_lib import *
from global_variables import *

def detect_hand(img):
#   img = cv2.imread(img_path)
  img_copy = img.copy()
  hands, img = detector.findHands(img)
  if hands:

      hand = hands[0]
      x, y, w, h = hand['bbox']

      # Ensure cropping coordinates are within image bounds
      y1 = max(0, y - offset)  # Ensure y1 is not negative
      y2 = min(img.shape[0], y + h + offset)  # Ensure y2 is within image height
      x1 = max(0, x - offset)  # Ensure x1 is not negative
      x2 = min(img.shape[1], x + w + offset)  # Ensure x2 is within image width


      imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
      imgCrop = img_copy[y1:y2, x1:x2]
      imgCropShape = imgCrop.shape
      if imgCropShape[0] * imgCropShape[1] == 0:
          return None, None, None, None, None

      aspectRatio = h / w
      if aspectRatio > 1:
          k = imgSize / h
          wCal = math.ceil(k * w)
          imgResize = cv2.resize(imgCrop, (wCal, imgSize))
          imgResizeShape = imgResize.shape
          wGap = math.ceil((imgSize - wCal) / 2)
          imgWhite[:, wGap:wCal + wGap] = imgResize
      else:
          k = imgSize / w
          hCal = math.ceil(k * h)
          imgResize = cv2.resize(imgCrop, (imgSize, hCal))
          imgResizeShape = imgResize.shape
          hGap = math.ceil((imgSize - hCal) / 2)
          imgWhite[hGap:hCal + hGap, :] = imgResize

      return imgWhite, x, y, w, h
  else:
    return None, None, None, None, None