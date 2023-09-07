import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import pandas as pd
import os
import sys
class grid(GridLayout):
    def __init__(self,**kwargs):
        super(grid,self).__init__(**kwargs)
        self.out=pd.DataFrame([[0,0,0,0]],columns=["Date","Usage Perpose","Amount", "Total"])
        if  os.path.exists(r"/daily_investements.csv"):
            err_output="Path already exists"
        else:
            self.out.to_csv("daily_investements.csv")
        self.cols=1
        self.sec_grid=GridLayout()
        self.sec_grid.cols=2
        self.sec_grid.add_widget(Label(text="Enter Date dd/mm/yyyy"))
        self.date=TextInput(multiline=False)
        self.sec_grid.add_widget(self.date)
        self.sec_grid.add_widget(Label(text="Enter Usage porpose"))
        self.usage=TextInput(multiline=False)
        self.sec_grid.add_widget(self.usage)
        self.sec_grid.add_widget(Label(text="Amount"))
        self.amount=TextInput(multiline=False)
        self.sec_grid.add_widget(self.amount)
        self.add_widget(self.sec_grid)
        self.submit=Button(text="Save")
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
        self.show=Button(text="Show")
        self.show.bind(on_press=self.Shows)
        self.add_widget(self.show)
        self.add_amount=Button(text="Add Amount")
        self.add_amount.bind(on_press=self.Add_Amount)
        self.add_widget(self.add_amount)
        
    def press(self,instance):
        usage=self.usage.text
        amount=self.amount.text
        self.add_widget(Label(text=amount))
        self.usage.text=""
        self.amount.text=""
        
    def Shows(self,instance):
        self.open_dataset=pd.read_csv(r"daily_investements.csv")
        self.add_widget(Label(text=self.open_dataset.to_string()))
    def Add_Amount(self,instance):
        self.open_dataset=pd.read_csv(r"daily_investements.csv")
        self.total=self.open_dataset.to_string()
        self.total=self.total.split(" ")
        self.total=int(self.total[-1])+int(self.amount.text)
        self.out1=pd.DataFrame([[self.date.text,self.usage.text,self.amount.text,self.total]],columns=["Date","Usage Perpose","Amount", "Total"])
        
        self.add_widget(Label(text=self.out1.to_string()))
    '''def save_press(self,instance):
        self.dataset=pd.read_csv("daily_investements.csv")
        self.ls=[self.date.text,self.usage.text,self.amount.text,"  "]
        
        self.out.at[2]=self.ls'''
        
class myApp(App):
    def build(self):
        return grid()
    
    
if __name__=="__main__":
    myApp().run()

