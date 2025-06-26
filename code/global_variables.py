from import_lib import *

## Paths
current_file = os.path.abspath(__file__)
code_folder = os.path.dirname(current_file) # /HandSign/code
HandSign_folder = os.path.dirname(code_folder) # /HandSign
model_folder = os.path.join(HandSign_folder, 'new_models') # /HandSign/new_models

instruct_image_dir = os.path.join(HandSign_folder, 'instruct_alphabet.png')

## Global Variable
offset = 20
imgSize = 128

## detector
detector = HandDetector(maxHands=1)
###
# V2
mobile_net_v2 = MobileNetV2(weights='imagenet', include_top=False, input_shape=(128, 128, 3))
# V3
mobile_net_v3 = MobileNetV3Small(weights='imagenet', include_top=False, input_shape=(128, 128, 3))
# V4
mobile_net_v4 = timm.create_model('mobilenetv4_conv_small.e2400_r224_in1k', pretrained=True,features_only=True,).eval()
data_config = {'input_size': (3, 128, 128),
 'interpolation': 'bicubic',
 'mean': (0.485, 0.456, 0.406),
 'std': (0.229, 0.224, 0.225),
 'crop_pct': 0.875,
 'crop_mode': 'center'}
transforms_mnv4 = timm.data.create_transform(**data_config, is_training=False)
###

# Classify model
feature_name = 'mnv2'
dataset_train = 'gen' # gen, aug, or
size_classify = 'small' # large, medium, small

type_size_classify = '128' if size_classify=='large' else ('64' if size_classify=='medium' else 'rm')
classify_model_name = f'NN_{dataset_train}_{feature_name}_10_20000_{type_size_classify}_28.h5'
print(classify_model_name)
classify_model_dir = os.path.join(model_folder, feature_name, classify_model_name)
classify_model = tf.keras.models.load_model(classify_model_dir)
classify_model.summary()

## Map label
map_label = {'A': 0,    'B': 1,    'C': 2,    'D': 3,    'E': 4,
    'F': 5,    'G': 6,    'H': 7,    'I': 8,    'J': 9,
    'K': 10,    'L': 11,    'M': 12,    'N': 13,    'O': 14,
    'P': 15,    'Q': 16,    'R': 17,    'S': 18,    'T': 19,
    'U': 20,    'V': 21,    'W': 22,    'X': 23,    'Y': 24,
    'Z': 25,    'space': 26,    'del': 27, 'nothing': 28}
label = {v: k for k, v in map_label.items()}

# Ổn định prediction
num_frame = 5
prediction_buffer = deque(maxlen=num_frame) 