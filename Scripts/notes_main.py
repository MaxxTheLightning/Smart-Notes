from interface import Interface
from logic import Logic

def main():
    logic = Logic()
    interface = Interface(name = 'Smart notes')

    def on_item_click(note_name):
        logic.select(note_name)
        interface.update_note_fields(logic.get_text(), logic.get_notes(), logic.get_tags())

    def on_delete_click():
        logic.delete_current_note()
        interface.update_note_fields(logic.get_text(), logic.get_notes(), logic.get_tags())

    def on_create_click(note_name):
        logic.create_note(note_name)
        logic.select(note_name)
        interface.update_note_fields(logic.get_text(), logic.get_notes(), logic.get_tags())

    def on_save_click(note_text):
        logic.save_current_note(note_text)

    def unpin_tag_from_note(tag_name):
        logic.unpin_tag_from_current_note(tag_name)
        interface.update_note_fields(logic.get_text(), logic.get_notes(), logic.get_tags())

    def on_tag_pinned(tag_name):
        logic.pin_tag_to_current_note(tag_name)
        interface.update_note_fields(logic.get_text(), logic.get_notes(), logic.get_tags())

    def on_find_by_tag(tag_name):
        logic.set_filter(tag_name)
        interface.update_note_fields(logic.get_text(), logic.get_notes(), logic.get_tags())

    interface.accept_find_note(on_find_by_tag)
    interface.accept_delete_tag(unpin_tag_from_note)
    interface.accept_pin_tag(on_tag_pinned)
    interface.accept_delete_note(on_delete_click)
    interface.accept_select_note(on_item_click)
    interface.accept_save_note(on_save_click)
    interface.accept_create_note(on_create_click)
    interface.update_note_fields("", logic.get_notes(), logic.get_tags())
    interface.run()

if __name__ == '__main__':
    main()