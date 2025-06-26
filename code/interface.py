from import_lib import *
from global_variables import *
from detect import *
from extract_feature import *
from spell_check import *

# Các biến điều khiển
last_saved_label = None
last_saved_time = 0
cooldown = 2  # Giây
sentence = ""
completed_words = []
current_word_tokens = []
blackout_frames = 0

def update_frame():
    global imgOutput, imgBlack, last_saved_label, last_saved_time, sentence, completed_words, current_word_tokens, blackout_frames

    success, img = cap.read()
    if not success:
        print("Không đọc được frame")
        return

    imgOutput = img.copy()
    imgHand, x, y, w, h = detect_hand(img)
    
    if imgHand is not None:
        if feature_name=='mnv2':
            feature = extract_feature_mobile_net_v2(imgHand)
        elif feature_name=='mnv3':
            feature = extract_feature_mobile_net_v3(imgHand)
        elif feature_name=='mnv4':
            feature = extract_feature_mobile_net_v4(imgHand)
        prob = classify_model.predict(feature)
        prediction = np.argmax(prob, axis=1)[0]

        prediction_buffer.append(prediction)
        if len(prediction_buffer) > 20:
            prediction_buffer.pop(0)  # Giới hạn buffer

        most_common, count = Counter(prediction_buffer).most_common(1)[0]

        # Tính tỷ lệ phần trăm
        ratio = count / len(prediction_buffer)

        # Vẽ thông tin lên ảnh
        cv2.rectangle(imgOutput, (x - offset, y - offset-50), (x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput, label[most_common], (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(imgOutput, (x-offset, y-offset), (x + w+offset, y + h+offset), (255, 0, 255), 4)

        # Nếu nhãn chiếm ≥90% và khác lần trước => thêm vào text box
        current_time = time.time()
        
        if ratio >= 0.9 and (last_saved_label != most_common or current_time - last_saved_time > cooldown) and len(prediction_buffer) == num_frame:
            last_saved_label = most_common
            last_saved_time = current_time

            # Hiệu ứng: chụp ảnh (có thể lưu nếu cần)
            print("✅ Chụp ảnh:", label[most_common])
            blackout_frames = 1  # Hiển thị ảnh đen trong 3 frame

            # Thay đổi output
            label_token = label[most_common]

            if label_token == 'del':
                if current_word_tokens:
                    current_word_tokens.pop()

            elif label_token == 'space':
                # Kết thúc từ đang gõ
                word_raw = ' '.join(current_word_tokens)
                processed_word = process_sentence(word_raw)
                corrected_word = check_spell(processed_word)

                if corrected_word:
                    completed_words.append(corrected_word)

                current_word_tokens = []  # Bắt đầu từ mới

            else:
                # Ghi nhận ký tự đang gõ
                current_word_tokens.append(label_token)
            
            raw_current = ' '.join(current_word_tokens)
            partial_word = process_sentence(raw_current)
            sentence = ' '.join(completed_words + [partial_word])


            # Hiển thị trong textbox
            print(sentence)
            listbox.delete(0, tk.END)
            listbox.insert(tk.END, sentence)
        # Hiển thị ảnh đen nếu cần
        if blackout_frames > 0:
            imgOutput = imgBlack
            blackout_frames -= 1

    else:
        print("No Hand")
    
    # Instructor
    instruct_img = cv2.imread(instruct_image_dir)
    instruct_img = cv2.resize(instruct_img, (600, 800))
    cv2.imshow("Instruct", instruct_img)

    # Hiển thị video lên Tkinter
    img_rgb = cv2.cvtColor(imgOutput, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    imgtk = ImageTk.PhotoImage(image=img_pil)

    label_video.imgtk = imgtk
    label_video.configure(image=imgtk)

    root.after(10, update_frame)

# Giao diện Tkinter
root = tk.Tk()
root.title("Hand Detection")

frame_video = tk.Frame(root)
frame_video.pack()

label_video = tk.Label(frame_video)
label_video.pack()

# Khung hiển thị nhãn đã chụp
frame_text = tk.Frame(root)
frame_text.pack(pady=10)

tk.Label(frame_text, text="📸 Kết quả").pack()
listbox = tk.Listbox(frame_text, width=80, height=5)
listbox.pack()

# Mở webcam
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
imgBlack = np.zeros((height, width, 3), np.uint8)

# Bắt đầu
update_frame()
root.mainloop()
cap.release()
cv2.destroyAllWindows()