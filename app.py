from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from bs4 import BeautifulSoup

class HTMLReaderApp(App):

    def build(self):
        layout = GridLayout(cols=1)
        self.filechooser = FileChooserListView()
        self.filechooser.path = 'content'
        layout.add_widget(self.filechooser)
        layout.add_widget(Button(text='Open HTML', on_press=self.open_html))
        layout.add_widget(Button(text='Exit', on_press=self.stop))
        return layout

    def open_html(self, instance):
        if not self.filechooser.selection:
            return
        html_file = self.filechooser.selection[0]
        with open(html_file, "r") as file:
            soup = BeautifulSoup(file, 'html.parser')
            html_text = soup.get_text()
        popup = Popup(title='HTML Text', content=Label(text=html_text), size_hint=(0.8, 0.8))
        popup.open()

    def stop(self, instance):
        App.get_running_app().stop()

if __name__ == '__main__':
    HTMLReaderApp().run()