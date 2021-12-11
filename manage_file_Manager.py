from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivy.lang import Builder

kv = """

BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: "File Manager"

    FloatLayout:
        MDFlatButton:
            text: "Open File Manager"
            pos_hint: {'center_x':0.5,'center_y':0.5}
            on_release: app.open_file_manager()

"""

class FileModuleApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager_obj = MDFileManager(
            select_path = self.select_path,
            exit_manager = self.exit_manager,
            preview = True
        )
    
    def open_file_manager(self):
        self.file_manager_obj.show("/")
    
    def select_path(self, path):
        print(path)
        self.exit_manager()

    def exit_manager(self):
        self.file_manager_obj.close()


    def build(self):
        Builder.load_string(kv)

if __name__ =="__main__":
    FileModuleApp().run()