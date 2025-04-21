from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from mood_analysis import analyze_mood
from SoulSync.database import save_journal_entry
from datetime import datetime

Builder.load_file("ui/home.kv")

class MainLayout(BoxLayout):
    def on_submit(self):
        text = self.ids.journal_input.text
        mood = analyze_mood(text)
        self.ids.mood_label.text = f"Mood: {mood}"

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_journal_entry(date, text, mood)

        self.ids.journal_input.text = ""

class SoulSyncApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    SoulSyncApp().run()
