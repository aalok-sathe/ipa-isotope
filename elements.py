#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader, BaseLoader, DebugUndefined
from pathlib import Path
import yaml


DATA = Path('./data')

jinja_env = Environment(loader=FileSystemLoader('templates'),
                        # extensions=['jinja2_markdown.MarkdownExtension'],
                        undefined=DebugUndefined)
template = jinja_env.get_template('elements.template.html')

class Element:
    def __init__(self, name='Element', symbol='', number=0, weight=0, **kwargs):
        setattr(self, 'name', name)
        setattr(self, 'symbol', symbol)
        setattr(self, 'number', number)
        setattr(self, 'weight', weight)

        for key, value in kwargs.items():
            setattr(self, key, value)

with (DATA/'elements.yaml').open('r') as fp:
    elements = [Element(**elem) for elem in yaml.load(fp, Loader=yaml.Loader)]

data = dict(
    elements = elements,
)

with Path('elements.html').open('w') as out:
    out.write(template.render(**data))
