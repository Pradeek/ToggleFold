import sublime, sublime_plugin

class ToggleFoldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view

        if any(not view.fold(sel) for sel in view.sel()):
            map(view.unfold, view.sel())
