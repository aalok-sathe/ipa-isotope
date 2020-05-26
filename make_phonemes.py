import json
import yaml

phonemes = []

with open('data/ipaBook-amundo.json') as log_file, open('data/phonemes-riggle.json') as feat_file:
    info = json.load(log_file)
    features = json.load(feat_file)
    for phone_info in info:
        # print(phone_info)
        for phone, feats in features.items():
            if phone_info["Character"] == phone:
                new_entry = {}
                new_entry['symbol'] = phone
                new_entry['name'] = phone_info["IPA Name"]
                new_entry['number'] = phone_info["IPA Number"]
                new_entry["USV"] = phone_info["USV"]
                new_entry["unicode"] = phone_info["Unicode Name"]
                new_entry["classes"] = phone_info["IPA Description"]
                for feature_desc, feature_value in feats["features"].items():
                    new_entry[feature_desc] = feature_value
                phonemes.append(new_entry)
    log_file.close()
    feat_file.close()

with open('data/phonemes.yaml', 'w') as outputfile:
    data = yaml.dump(phonemes, outputfile)
    outputfile.close()
