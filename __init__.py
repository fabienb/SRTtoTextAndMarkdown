# __init__.py
import sublime
import sublime_plugin
from .srt_converter import convert_srt_to_text, convert_srt_to_markdown

class ConvertSrtToTextCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        srt_content = self.view.substr(sublime.Region(0, self.view.size()))
        text_content = convert_srt_to_text(srt_content)

        # Create a new view with the converted content
        new_view = self.view.window().new_file()
        new_view.set_name("Converted Text")
        new_view.set_scratch(True)
        new_view.run_command('insert_snippet', {'contents': text_content})

class ConvertSrtToMarkdownCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        srt_content = self.view.substr(sublime.Region(0, self.view.size()))
        md_content = convert_srt_to_markdown(srt_content)

        # Create a new view with the converted content
        new_view = self.view.window().new_file()
        new_view.set_name("Converted Markdown")
        new_view.set_scratch(True)
        new_view.run_command('insert_snippet', {'contents': md_content})
