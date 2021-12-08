import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# creating the class for grid
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1

# creating the secend gridlayout
        self.inside = GridLayout()
        # this command is for creating columns
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        # self.name = TextInput()
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput()
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text="Email : "))
        self.email = TextInput()
        self.inside.add_widget(self.email)

# for adding the grid number 1
        self.add_widget(self.inside)

# for adding the button
        self.submit = Button(text= "Submit Now",font_size=40)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)

    def pressed(self,instance):
        name = self.name.text
        last = self.lastname.text
        email = self.email.text
        print(f"Name: {name} and Last Name: {last} and Email: {email}")

        self.name.text = ""
        self.lastname.text = ""
        self.email.text = ""
# app is the class in kivy which is inherited in this class and this is the main class which we work it
class MyApp(App):
    def build(self):
        return MyGrid()

# this command is used when we work only this class and if we work another file this code is not to execute
if __name__=="__main__":
    MyApp().run()
