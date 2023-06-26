from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.utils import platform
from Screens.HomeScreen.home import HomeScreen
from Screens.RootScreen.root import RootScreen


class BaseApp(MDApp):
    def build(self):
        self.title = "BaseApp"
        self.load_all_kv_files("Screens")
        if platform in ["win", "linux", "macosx"]:
            Window.size = (400, 600)
        return RootScreen()


if __name__ == "__main__":
    BaseApp().run()