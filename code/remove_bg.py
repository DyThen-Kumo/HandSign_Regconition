from rembg import remove, new_session

session = new_session(model_name="u2netp", providers=["CPUExecutionProvider"])

def remove_background(img):
    return remove(img, session=session)

# input = cv2.imread(r'C:\d\DELL\Pictures\Wallpaper\Screenshot 2025-04-20 224957.png')
# print(input)

# input = remove(input, session=session)

# cv2.imwrite(r"C:\D\UIT\HOC KI 6\CS431\HandSign\test.jpg", input)

