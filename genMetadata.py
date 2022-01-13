import json 

METADATA_FILE = "./metadata/all_traits.json"
with open(METADATA_FILE,"r+") as file:
	data = json.load(file)


IMAGE_BASE_URL = "https://gateway.pinata.cloud/ipfs/QmWWpsdSXUrtMfLcVTEX12CCggAtJPDYG4CsM4kNqiF4yp"
PROJECT = "crazyNFT"


def createAttr(key,value):
	return {
			"trait_type":key,
			"value":value
		}

for item in data:

	token_id = item["token_id"]

	token = { 
		"tokenID" : token_id,
		"image" : f"{IMAGE_BASE_URL}/{token_id}.png",
		"name" : f"{PROJECT}-{token_id}",
		"attributes" : [] 
	}

	token["attributes"].append(createAttr("FACE",item["FACE"]))
	token["attributes"].append(createAttr("EYES",item["EYES"]))
	token["attributes"].append(createAttr("EARS",item["EARS"]))
	token["attributes"].append(createAttr("HAIR",item["HAIR"]))
	token["attributes"].append(createAttr("MOUTH",item["MOUTH"]))
	token["attributes"].append(createAttr("NOSE",item["NOSE"]))
	token["attributes"].append(createAttr("BACKGROUND",item["background"]))
	with open("./metadata/" + str(token_id) + ".json","w") as file:
		json.dump(token,file,indent=3)
			
