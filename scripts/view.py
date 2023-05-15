import tempfile
import uuid
import os
import pygraphviz as pgv
from IPython.display import Image, display

def view_graphviz(graphviz):
    name = f'{tempfile.gettempdir()}/{uuid.uuid4()}.png'
    graphviz.draw(name, prog='dot')
    os.system('gwenview ' + name + ' &')
    return Image(name)