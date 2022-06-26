import inspect

import justpy as jp
from webapp.home import Home
from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.page import Page

importacao = list(globals().values())

for obj in importacao:
    if inspect.isclass(obj):
        if issubclass(obj, Page) and obj is not Page:
            jp.Route(obj.path, obj.serve)

# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8000)

