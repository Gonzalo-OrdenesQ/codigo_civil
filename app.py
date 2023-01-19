from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from PyPDF2 import PdfFileReader

class PDFReaderApp(App):

    def build(self):
        layout = GridLayout(cols=1)
        self.filechooser = FileChooserListView()
        self.filechooser.path = '/path/to/pdf/folder'
        layout.add_widget(self.filechooser)
        layout.add_widget(Button(text='Open PDF', on_press=self.open_pdf))
        return layout

    def open_pdf(self, instance):
        if not self.filechooser.selection:
            return
        pdf_file = self.filechooser.selection[0]
        pdf = PdfFileReader(open(pdf_file, 'rb'))
        pdf_text = pdf.getPage(0).extractText()
        popup = Popup(title='PDF Text', content=Label(text=pdf_text), size_hint=(0.8, 0.8))
        popup.open()

if __name__ == '__main__':
    PDFReaderApp().run()