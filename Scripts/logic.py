import json
import os
class Logic():
    def __init__(self):
        self.current = None
        self.notes = {}
        self.init_file()
        self.filter = ''
        self.load()
        self.guide()

    def init_file(self):
        if not os.path.isfile("notes_data.json"):
            with open("notes_data.json", "a") as file:
                file.write("{}")

    def guide(self):
        self.notes["Welcome"] = {
            "text" : "Welcome to Smart Notes! This app will help you to keep all your notes with tags. Try to write your first note right now and don't forget to add some tags! \n\n Made by MaxxTheLightning, 2025" ,
            "tags" : ["Introducion", "Welcome"]
        }

    def save(self):
        with open("notes_data.json", "w", encoding='utf-8') as file:
            json.dump(self.notes , file)

    def load(self):
        with open("notes_data.json", "r") as file:
            self.notes = json.load(file)

    def select(self, note):
        if note in self.notes:
            self.current = note
        else:
            self.current = None
    
    def get_text(self):
        if self.current:
            return self.notes[self.current]["text"]
        return ""

    def get_tags(self):
        if self.current:
            return self.notes[self.current]["tags"]
        return []

    def get_notes(self):
        if self.filter == '' or self.filter[0] == ' ':
            return list(self.notes.keys())
        filtered_notes = []
        for note in self.notes:
            if self.filter in self.notes[note]['tags']:
                filtered_notes.append(note)
        return filtered_notes

    def set_filter(self, tag):
        self.filter = tag.lower()

    def create_note(self, name):
        self.notes[name] = {
            "text": "",
            "tags": []
        }
        self.save()

    def save_current_note(self, text):
        if not self.current:
            return
        
        self.notes[self.current] = {
            "text": text,
            "tags": self.get_tags()
        }
        self.save()

    def delete_current_note(self):
        if not self.current:
            return
        
        del self.notes[self.current]
        self.current = None
        self.save()

    def pin_tag_to_current_note(self, tag):
        if not self.current:
            return
        if tag == '' or tag[0] == ' ':
            return
        if tag in self.notes[self.current]["tags"]:
            return
        self.notes[self.current]["tags"].append(tag.lower())
        self.save()

    def unpin_tag_from_current_note(self, tag):
        if not self.current:
            return
        index = self.notes[self.current]["tags"].index(tag)
        if index == -1:
            return
        del self.notes[self.current]["tags"][index]
        self.save()