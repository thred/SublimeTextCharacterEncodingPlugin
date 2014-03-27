import sublime, sublime_plugin, codecs
 
CHARACTER_ENCODINGS = [
    { "name": "UTF-8", "value": "utf-8" },
    { "name": "UTF-8 with BOM", "value": "utf-8 with bom" },
    { "name": "UTF-16 LE", "value": "utf-16 le" },
    { "name": "UTF-16 LE with BOM", "value": "utf-16 le with bom" },
    { "name": "UTF-16 BE", "value": "utf-16 be" },
    { "name": "UTF-16 BE with BOM", "value": "utf-16 be with bom" },
    { "name": "Western (Windows 1252)", "value": "Western (Windows 1252)" },
    { "name": "Western (ISO 8859-1)", "value": "Western (ISO 8859-1)" },
    { "name": "Western (ISO 8859-3)", "value": "Western (ISO 8859-3)" },
    { "name": "Western (ISO 8859-15)", "value": "Western (ISO 8859-15)" },
    { "name": "Western (Mac Roman)", "value": "Western (Mac Roman)" },
    { "name": "DOS (CP 437)", "value": "DOS (CP 437)" },
    { "name": "Arabic (Windows 1256)", "value": "Arabic (Windows 1256)" },
    { "name": "Arabic (ISO 8859-6)", "value": "Arabic (ISO 8859-6)" },
    { "name": "Baltic (Windows 1257)", "value": "Baltic (Windows 1257)" },
    { "name": "Baltic (ISO 8859-4)", "value": "Baltic (ISO 8859-4)" },
    { "name": "Celtic (ISO 8859-14)", "value": "Celtic (ISO 8859-14)" },
    { "name": "Central European (Windows 1250)", "value": "Central European (Windows 1250)" },
    { "name": "Central European (ISO 8859-2)", "value": "Central European (ISO 8859-2)" },
    { "name": "Cyrillic (Windows 1251)", "value": "Cyrillic (Windows 1251)" },
    { "name": "Cyrillic (Windows 866)", "value": "Cyrillic (Windows 866)" },
    { "name": "Cyrillic (ISO 8859-5)", "value": "Cyrillic (ISO 8859-5)" },
    { "name": "Cyrillic (KOI8-R)", "value": "Cyrillic (KOI8-R)" },
    { "name": "Cyrillic (KOI8-U)", "value": "Cyrillic (KOI8-U)" },
    { "name": "Estonian (ISO 8859-13)", "value": "Estonian (ISO 8859-13)" },
    { "name": "Greek (Windows 1253)", "value": "Greek (Windows 1253)" },
    { "name": "Greek (ISO 8859-7)", "value": "Greek (ISO 8859-7)" },
    { "name": "Hebrew (Windows 1255)", "value": "Hebrew (Windows 1255)" },
    { "name": "Hebrew (ISO 8859-8)", "value": "Hebrew (ISO 8859-8)" },
    { "name": "Nordic (ISO 8859-10)", "value": "Nordic (ISO 8859-10)" },
    { "name": "Romanian (ISO 8859-16)", "value": "Romanian (ISO 8859-16)" },
    { "name": "Turkish (Windows 1254)", "value": "Turkish (Windows 1254)" },
    { "name": "Turkish (ISO 8859-9)", "value": "Turkish (ISO 8859-9)" },
    { "name": "Vietnamese (Windows 1258)", "value": "Vietnamese (Windows 1258)" },
]

def update_character_encoding(view):
    encoding = view.encoding()

    if encoding == "Undefined":
        view.erase_status("Encoding")
    else:
        view.set_status("Encoding", view.encoding())

class CharacterEncodingListener(sublime_plugin.EventListener):
    def on_new(self, view):
        update_character_encoding(view)

    def on_new_async(self, view):
        update_character_encoding(view)

    def on_clone(self, view):
        update_character_encoding(view)

    def on_clone_async(self, view):
        update_character_encoding(view)

    def on_load(self, view):
        update_character_encoding(view)

    def on_load_async(self, view):
        update_character_encoding(view)

    def on_post_save(self, view):
        update_character_encoding(view)

    def on_post_save_async(self, view):
        update_character_encoding(view)

    def on_activated(self, view):
        update_character_encoding(view)

    def on_activated_async(self, view):
        update_character_encoding(view)

class CharacterEncodingCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        names = [item['name'] for item in CHARACTER_ENCODINGS]
        values = [item['value'] for item in CHARACTER_ENCODINGS]

        def select(index):
            self.view.set_encoding(values[index])
            update_character_encoding(self.view)

        self.view.window().show_quick_panel(names, select, 0, 0, None)
