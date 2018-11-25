from ipywidgets import Layout, Button, Box, VBox
from ipywidgets import interact
import ipywidgets as widgets

# Items flex proportionally to the weight and the left over space around the text
print("Model Weights: ")
a = widgets.IntSlider(min=0,max=10,step=1,value=1, description='RF')
b = widgets.IntSlider(min=0,max=10,step=1,value=1, description='AdaBoost')
c = widgets.IntSlider(min=0,max=10,step=1,value=2, description='ExtraTrees')
d = widgets.IntSlider(min=0,max=10,step=1,value=4, description='Bagging')
e = widgets.Dropdown(options=['soft', 'hard'],value='soft', description='voting:')
f = widgets.IntText(description="random_state", value=3)
items_auto = [ a, b, c, d ]

# Items flex proportionally to the weight
items_0 = [ e, f ]
box_layout = Layout(display='flex-grow',
                    flex_flow='direction',
                    align_items='stretch',
                    width='100%')
box_auto = Box(children=items_auto, layout=box_layout)
box_0 = Box(children=items_0, layout=box_layout)
VBox([box_auto, box_0])

ui = widgets.VBox([box_auto, box_0])

# to be used in the training process
global weights
global voting_type
global rs

# update function for the bottom form
def func(a, b, c, d, e, f):
    global weights 
    global voting_type
    global rs
    weights = [a, b, c, d]
    voting_type = e
    rs = f
    print((a, b, c, d, e, f))

out = widgets.interactive_output(func, {'a': a, 'b': b, 'c': c, 'd':d, 'e':e, 'f':f})
display(ui, out)
