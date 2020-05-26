#!/usr/bin/env python3

import json
import yaml

from phonemes import phonemes

phonemelist = [
    dict(name=ph.name, symbol=sym, **ph.ipa_desc, **ph.properties)#, **ph.features)
    for sym, ph in phonemes.items()
]

with open('data/phonemes.yaml', 'w') as outputfile:
    data = yaml.dump(phonemelist, outputfile)
    outputfile.close()
