from logging import PlaceHolder
from gramformer import Gramformer

def correct(sentence):
    res=gf.correct(sentence)
    return res[0]

app_inputs = gr.inputs.Textbox(lines=3, placeholder="Enter a grammatically incorrect sentence here:-")
interface = gr.Interfaace(fn=correct,inputs=app_inputs,ouputs='text',title='Hi there, I\'m Gramformer')
interface.launch()