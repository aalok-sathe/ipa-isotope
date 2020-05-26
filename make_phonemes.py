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

                # basic information
                new_entry['symbol'] = phone
                full_details = phone_info["IPA Description"]
                new_entry['name'] = phone_info["IPA Name"]
                new_entry['number'] = phone_info["IPA Number"]
                new_entry["USV"] = phone_info["USV"]
                new_entry["unicode"] = phone_info["Unicode Name"]
                new_entry["classes"] = full_details

                # determining voicing
                if "Voiced" in full_details or feats["features"]["voice"]:
                    new_entry['voicing'] = 'voiced'
                elif "Unvoiced" in full_details or not feats["features"]["voice"]:
                    new_entry['voicing'] = 'unvoiced'

                # determining sonority
                if phone in ['p', 'b', 't', 'd', 'k', 'g']:
                    new_entry['sonority'] = 1
                elif phone in ['f', 'v', 's', 'z']:
                    new_entry['sonority'] = 2
                elif phone in ['m', 'n']:
                    new_entry['sonority'] = 3
                elif phone in ['l', 'r']:
                    new_entry['sonority'] = 4
                else:
                    new_entry['sonority'] = 5

                # determining manner of articulation
                if "stop" or "plosive" in full_details:
                    new_entry["manner"] = "plosive"
                elif "trill" in full_details:
                    new_entry["manner"] = "trill"
                elif "tap" or "flap" in full_details:
                    new_entry["manner"] = "tap/flap"
                elif "fricative" in full_details:
                    if "lateral" in full_details:
                        new_entry["manner"] = "lateral fricative"
                    else:
                        new_entry["manner"] = "fricative"
                elif "approximant" in full_details:
                    if "lateral" in full_details:
                        new_entry["manner"] = "lateral approximant"
                    else:
                        new_entry["manner"] = "approximant"
                elif "nasal" in full_details:
                    new_entry["manner"] = "nasal"
                else:
                    new_entry["manner"] = "unknown"

                # determining

                # other features
                for feature_desc, feature_value in feats["features"].items():
                    new_entry[feature_desc] = feature_value
                phonemes.append(new_entry)
    log_file.close()
    feat_file.close()

with open('data/phonemes.yaml', 'w') as outputfile:
    data = yaml.dump(phonemes, outputfile)
    outputfile.close()