# -*- coding:utf-8 -*-
import os

BASE_DIR = os.path.dirname(__file__)
setting = {
    'debug': True,
    'static_path': os.path.join(BASE_DIR, 'static'),
    'template_path': os.path.join(BASE_DIR, 'templates'),
}