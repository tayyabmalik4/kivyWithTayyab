import kivy
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from kivy.uix.layout import Layout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture


class MainApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        self.image = Image()
        layout.add_widget(self.image)
        self.save_img_button=MDRaisedButton(
            text="Take Picture",
            pos_hint = {'center_x': 0.5, 'center_y':0.5},
            size_hint=(None,None))
        self.save_img_button.bind(on_press=self.take_picture)
        layout.add_widget(self.save_img_button)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.load_video, 1.0/30.0)
        return layout
    def load_video(self, *args):
        ret, frame = self.capture.read()
        frame = cv2.flip(frame,1)
        #frame initialized
        self.image_frame = frame
        buffer = cv2.flip(frame,0).tostring()
        texture = Texture.create(size=(frame.shape[1],frame.shape[0]),colorfmt='bgr')
        texture.blit_buffer(buffer,colorfmt='bgr',bufferfmt='ubyte')
        self.image.texture = texture
    def take_picture(self,*args):
        segmentor = SelfiSegmentation()
        backremove=segmentor.removeBG(self.image_frame,(255,255,255),threshold=0.5)
        image_name = f"picture_1.png"
        cv2.imwrite(image_name, backremove)

    
if __name__ == "__main__":
    MainApp().run()