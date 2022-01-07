#!/usr/bin/env python3

from PIL import Image
from IPython.display import display 
from data import *
import random
from colorGen import genColor
''' 
Each avatar will be unique and have 5 traits
'''

TOTAL_IMAGES = 50

all_images = [] 

def create_new_images():

	new_image = {}

	new_image["FACE"] = random.choices(face,face_weights)[0]
	new_image["EARS"] = random.choices(ears,ears_weights)[0]
	new_image["EYES"] = random.choices(eyes,eyes_weights)[0]
	new_image["HAIR"] = random.choices(hair, hair_weights)[0]
	new_image["MOUTH"] = random.choices(mouth, mouth_weights)[0]
	new_image["NOSE"] = random.choices(nose, nose_weights)[0]

	if new_image in all_images:
		return create_new_images()
	else:
		return new_image


for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_images()
    
    all_images.append(new_trait_image)
	

def all_images_unique(all_images):
	seen = list()
	#print([i in seen or seen.append(i) for i in all_images])
	return any(i in seen or seen.append(i) for i in all_images)

i=0 

for item in all_images:
	item["token_id"]=f"nft{i}"
	i+=1


''' Getting trait counts '''
mouth_count = {}
for item in mouth:
	mouth_count[item] = 0

face_count = {} 
for item in face:
	face_count[item] = 0

eyes_count = {}
for item in eyes:
	eyes_count[item] = 0

nose_count = {}
for item in nose:
	nose_count[item] = 0

ears_count = {} 
for item in ears:
	ears_count[item] = 0

hair_count = {}
for item in hair:
	hair_count[item] = 0

for image in all_images:
	face_count[image["FACE"]] += 1
	ears_count[image["EARS"]] += 1
	eyes_count[image["EYES"]] += 1
	hair_count[image["HAIR"]] += 1
	mouth_count[image["MOUTH"]] += 1
	nose_count[image["NOSE"]] += 1

for item in all_images:
	im1 = Image.open(f'substrapunks-master/scripts/face_parts/face/{face_files[item["FACE"]]}.png')
	im2 = Image.open(f'substrapunks-master/scripts/face_parts/eyes/{eyes_files[item["EYES"]]}.png')
	im3 = Image.open(f'substrapunks-master/scripts/face_parts/ears/{ears_files[item["EARS"]]}.png')
	im4 = Image.open(f'substrapunks-master/scripts/face_parts/hair/{hair_files[item["HAIR"]]}.png')
	im5 = Image.open(f'substrapunks-master/scripts/face_parts/mouth/{mouth_files[item["MOUTH"]]}.png')
	im6 = Image.open(f'substrapunks-master/scripts/face_parts/nose/{nose_files[item["NOSE"]]}.png')
	bg = Image.new("RGBA",im5.size,color=genColor())
	
	com = Image.alpha_composite(bg,im1)
	com1 = Image.alpha_composite(com,im2)
	com2 = Image.alpha_composite(com1,im3)
	com3 = Image.alpha_composite(com2,im4)
	com4 = Image.alpha_composite(com3,im5)
	com5 = Image.alpha_composite(com4,im6)

	rgb_im = com5.convert("RGB")
	file_name = str(item["token_id"]) + ".png"
	
	rgb_im.save("./images/"+file_name)
	

