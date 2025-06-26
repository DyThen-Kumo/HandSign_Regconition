from import_lib import *
from global_variables import *

def extract_feature_mobile_net_v2(imgHand):
    img_array = image.img_to_array(imgHand)
    img_array = np.expand_dims(img_array, axis=0)
    # img_array = preprocess_input(img_array)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    features = mobile_net_v2.predict(img_array)
    features = np.array(features)

    return features

def extract_feature_mobile_net_v3(imgHand):
    img_array = image.img_to_array(imgHand)
    img_array = np.expand_dims(img_array, axis=0)
    # img_array = preprocess_input(img_array)
    img_array = tf.keras.applications.mobilenet_v3.preprocess_input(img_array)

    features = mobile_net_v3.predict(img_array)
    features = np.array(features)

    return features

def extract_feature_mobile_net_v4(imgHand):
    hand = cv2.cvtColor(imgHand, cv2.COLOR_BGR2RGB)
    hand = Image.fromarray(hand)

    feature = mobile_net_v4(transforms_mnv4(hand).unsqueeze(0))[-1]  # unsqueeze single image into batch of 1
    feature = feature.squeeze(0).permute(1, 2, 0).detach().numpy()

    features = np.array([feature])

    return features