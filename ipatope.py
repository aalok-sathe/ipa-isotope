#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader, BaseLoader, DebugUndefined
from pathlib import Path
import yaml


DATA = Path('./data')

jinja_env = Environment(loader=FileSystemLoader('templates'),
                        # extensions=['jinja2_markdown.MarkdownExtension'],
                        undefined=DebugUndefined)
template = jinja_env.get_template('phonemes.template.html')


class Phoneme:
    def __init__(self, name='Element', symbol='', sound='', **kwargs):
        kwargs.update(dict(name=name, symbol=symbol, sound=sound))
        for key, value in kwargs.items():
            setattr(self, key, value)


with (DATA / 'phonemes.yaml').open('r') as fp:
    phonemes = [Phoneme(**ph) for ph in yaml.load(fp, Loader=yaml.Loader)]

data = dict(
    phonemes=phonemes,
)

with Path('index.html').open('w') as out:
    out.write(template.render(**data))
