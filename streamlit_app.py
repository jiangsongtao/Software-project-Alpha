#!/usr/bin/env python
# coding: utf-8

# In[7]:


#!/usr/bin/env python
# coding: utf-8

# In[9]:
#!/usr/bin/env python
# coding: utf-8

# In[7]:

import numpy as np
import matplotlib.pyplot as plt
import os
import torch
import torch.nn as nn
import torchvision
from torchvision import models,transforms,datasets
import time
import json
import pandas as pd
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import os
import shutil
import time
import pandas as pd
import random
import streamlit as st
import numpy as np
from io import BytesIO
from torch.utils.data import Dataset
from PIL import Image
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
idx_to_class={0: 'Acadian_Flycatcher',
 1: 'American_Crow',
 2: 'American_Goldfinch',
 3: 'American_Pipit',
 4: 'American_Redstart',
 5: 'American_Three_toed_Woodpecker',
 6: 'Anna_Hummingbird',
 7: 'Artic_Tern',
 8: 'Baird_Sparrow',
 9: 'Baltimore_Oriole',
 10: 'Bank_Swallow',
 11: 'Barn_Swallow',
 12: 'Bay_breasted_Warbler',
 13: 'Belted_Kingfisher',
 14: 'Bewick_Wren',
 15: 'Black_Tern',
 16: 'Black_and_white_Warbler',
 17: 'Black_billed_Cuckoo',
 18: 'Black_capped_Vireo',
 19: 'Black_footed_Albatross',
 20: 'Black_throated_Blue_Warbler',
 21: 'Black_throated_Sparrow',
 22: 'Blue_Grosbeak',
 23: 'Blue_Jay',
 24: 'Blue_headed_Vireo',
 25: 'Blue_winged_Warbler',
 26: 'Boat_tailed_Grackle',
 27: 'Bobolink',
 28: 'Bohemian_Waxwing',
 29: 'Brandt_Cormorant',
 30: 'Brewer_Blackbird',
 31: 'Brewer_Sparrow',
 32: 'Bronzed_Cowbird',
 33: 'Brown_Creeper',
 34: 'Brown_Pelican',
 35: 'Brown_Thrasher',
 36: 'Cactus_Wren',
 37: 'California_Gull',
 38: 'Canada_Warbler',
 39: 'Cape_Glossy_Starling',
 40: 'Cape_May_Warbler',
 41: 'Cardinal',
 42: 'Carolina_Wren',
 43: 'Caspian_Tern',
 44: 'Cedar_Waxwing',
 45: 'Cerulean_Warbler',
 46: 'Chestnut_sided_Warbler',
 47: 'Chipping_Sparrow',
 48: 'Chuck_will_Widow',
 49: 'Clark_Nutcracker',
 50: 'Clay_colored_Sparrow',
 51: 'Cliff_Swallow',
 52: 'Common_Raven',
 53: 'Common_Tern',
 54: 'Common_Yellowthroat',
 55: 'Crested_Auklet',
 56: 'Dark_eyed_Junco',
 57: 'Downy_Woodpecker',
 58: 'Eared_Grebe',
 59: 'Eastern_Towhee',
 60: 'Elegant_Tern',
 61: 'European_Goldfinch',
 62: 'Evening_Grosbeak',
 63: 'Field_Sparrow',
 64: 'Fish_Crow',
 65: 'Florida_Jay',
 66: 'Forsters_Tern',
 67: 'Fox_Sparrow',
 68: 'Frigatebird',
 69: 'Gadwall',
 70: 'Geococcyx',
 71: 'Glaucous_winged_Gull',
 72: 'Golden_winged_Warbler',
 73: 'Grasshopper_Sparrow',
 74: 'Gray_Catbird',
 75: 'Gray_Kingbird',
 76: 'Gray_crowned_Rosy_Finch',
 77: 'Great_Crested_Flycatcher',
 78: 'Great_Grey_Shrike',
 79: 'Green_Jay',
 80: 'Green_Kingfisher',
 81: 'Green_Violetear',
 82: 'Green_tailed_Towhee',
 83: 'Groove_billed_Ani',
 84: 'Harris_Sparrow',
 85: 'Heermann_Gull',
 86: 'Henslow_Sparrow',
 87: 'Herring_Gull',
 88: 'Hooded_Merganser',
 89: 'Hooded_Oriole',
 90: 'Hooded_Warbler',
 91: 'Horned_Grebe',
 92: 'Horned_Lark',
 93: 'Horned_Puffin',
 94: 'House_Sparrow',
 95: 'House_Wren',
 96: 'Indigo_Bunting',
 97: 'Ivory_Gull',
 98: 'Kentucky_Warbler',
 99: 'Laysan_Albatross',
 100: 'Lazuli_Bunting',
 101: 'Le_Conte_Sparrow',
 102: 'Least_Auklet',
 103: 'Least_Flycatcher',
 104: 'Least_Tern',
 105: 'Lincoln_Sparrow',
 106: 'Loggerhead_Shrike',
 107: 'Long_tailed_Jaeger',
 108: 'Louisiana_Waterthrush',
 109: 'Magnolia_Warbler',
 110: 'Mallard',
 111: 'Mangrove_Cuckoo',
 112: 'Marsh_Wren',
 113: 'Mockingbird',
 114: 'Mourning_Warbler',
 115: 'Myrtle_Warbler',
 116: 'Nashville_Warbler',
 117: 'Nelson_Sharp_tailed_Sparrow',
 118: 'Nighthawk',
 119: 'Northern_Flicker',
 120: 'Northern_Fulmar',
 121: 'Northern_Waterthrush',
 122: 'Olive_sided_Flycatcher',
 123: 'Orange_crowned_Warbler',
 124: 'Orchard_Oriole',
 125: 'Ovenbird',
 126: 'Pacific_Loon',
 127: 'Painted_Bunting',
 128: 'Palm_Warbler',
 129: 'Parakeet_Auklet',
 130: 'Pelagic_Cormorant',
 131: 'Philadelphia_Vireo',
 132: 'Pied_Kingfisher',
 133: 'Pied_billed_Grebe',
 134: 'Pigeon_Guillemot',
 135: 'Pileated_Woodpecker',
 136: 'Pine_Grosbeak',
 137: 'Pine_Warbler',
 138: 'Pomarine_Jaeger',
 139: 'Prairie_Warbler',
 140: 'Prothonotary_Warbler',
 141: 'Purple_Finch',
 142: 'Red_bellied_Woodpecker',
 143: 'Red_breasted_Merganser',
 144: 'Red_cockaded_Woodpecker',
 145: 'Red_eyed_Vireo',
 146: 'Red_faced_Cormorant',
 147: 'Red_headed_Woodpecker',
 148: 'Red_legged_Kittiwake',
 149: 'Red_winged_Blackbird',
 150: 'Rhinoceros_Auklet',
 151: 'Ring_billed_Gull',
 152: 'Ringed_Kingfisher',
 153: 'Rock_Wren',
 154: 'Rose_breasted_Grosbeak',
 155: 'Ruby_throated_Hummingbird',
 156: 'Rufous_Hummingbird',
 157: 'Rusty_Blackbird',
 158: 'Sage_Thrasher',
 159: 'Savannah_Sparrow',
 160: 'Sayornis',
 161: 'Scarlet_Tanager',
 162: 'Scissor_tailed_Flycatcher',
 163: 'Scott_Oriole',
 164: 'Seaside_Sparrow',
 165: 'Shiny_Cowbird',
 166: 'Slaty_backed_Gull',
 167: 'Song_Sparrow',
 168: 'Sooty_Albatross',
 169: 'Spotted_Catbird',
 170: 'Summer_Tanager',
 171: 'Swainson_Warbler',
 172: 'Tennessee_Warbler',
 173: 'Tree_Sparrow',
 174: 'Tree_Swallow',
 175: 'Tropical_Kingbird',
 176: 'Vermilion_Flycatcher',
 177: 'Vesper_Sparrow',
 178: 'Warbling_Vireo',
 179: 'Western_Grebe',
 180: 'Western_Gull',
 181: 'Western_Meadowlark',
 182: 'Western_Wood_Pewee',
 183: 'Whip_poor_Will',
 184: 'White_Pelican',
 185: 'White_breasted_Kingfisher',
 186: 'White_breasted_Nuthatch',
 187: 'White_crowned_Sparrow',
 188: 'White_eyed_Vireo',
 189: 'White_necked_Raven',
 190: 'White_throated_Sparrow',
 191: 'Wilson_Warbler',
 192: 'Winter_Wren',
 193: 'Worm_eating_Warbler',
 194: 'Yellow_Warbler',
 195: 'Yellow_bellied_Flycatcher',
 196: 'Yellow_billed_Cuckoo',
 197: 'Yellow_breasted_Chat',
 198: 'Yellow_headed_Blackbird',
 199: 'Yellow_throated_Vireo'}
# In[10]:


transform_test = transforms.Compose([
    transforms.Resize(256),
    # 将图像中央的高和宽均为224的正方形区域裁剪出来
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
st.title("My web for bird imges claasification")
uploaded_file=st.file_uploader("上传一张鸟类的图片",type='jpg')
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_test = Image.open(BytesIO(file_bytes))
    st.image(img_test,channels="RGB")          
    net=torch.load("model.pkl",map_location=torch.device('cpu'))
    net.eval()
    img_PIL_Tensor =transform_test(img_test)
    X=img_PIL_Tensor
    X=X.unsqueeze_(0) 
    X=X.cpu()
    net = net.cpu()
    st.button("点击按钮开始多鸟识别")
    if(st.button("点击按钮开始识别")):
        output = net(X)
        output = torch.softmax(output, dim=1)
        vals_try,pred_try = torch.max(output,dim=1)
        st.text(idx_to_class[pred_try.item()])
        st.text(vals_try.item())




