# -*- coding: utf-8 -*-

import os
import re
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config

kivy.require('2.2.0')

# 画面サイズの指定
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '400')

Builder.load_file(os.path.dirname(__file__) + "/interface.kv")


class ButtonTestWidget(Widget):

    def __init__(self, **kwargs):
        super(ButtonTestWidget, self).__init__(**kwargs)


class ButtonTestApp(App):
    def __init__(self, **kwargs):
        super(ButtonTestApp, self).__init__(**kwargs)
        self.title = 'Button Test'

    def build(self):
        return ButtonTestWidget()


if __name__ == '__main__':
    app = ButtonTestApp()
    app.run()
