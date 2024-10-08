from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import os

class SelfieCameraApp(App):
    def build(self):
        self.camera_obj = Camera()
        self.camera_obj.resolution = (800, 800)

        
        button_obj = Button(text="Click")
        button_obj.size_hint = (.5, .2)
        button_obj.pos_hint = {'x': .25, 'y': .25}
        button_obj.bind(on_press=self.take_selfie)

        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_obj)

        return layout

    def take_selfie(self, *args):
        
        file_path = os.path.join(os.getcwd(), "selfie.png")
        self.camera_obj.export_to_png(file_path)
        print(f"Selfie saved to {file_path}")

if __name__ == "__main__":
    SelfieCameraApp().run()

else:
    print("not working")