import sublime
import sublime_plugin
import os

SETTINGS_NAME = 'GotoOpenFile'
SETTINGS_FILE_NAME = '%s.sublime-settings' % SETTINGS_NAME


class GotoOpenFileCommand(sublime_plugin.TextCommand):

    def run(self, edit, active_group=False):
        window = sublime.active_window()

        selector = ViewSelector(window, active_group)
        window.show_quick_panel(selector.items, selector.select)


class ViewSelector(object):

    def __init__(self, window, active_group):
        self.window = window
        if active_group:
            self.views = window.views_in_group(window.active_group())
        else:
            self.views = window.views()
        self.items = [
            [
                self.__get_display_name(view),
                self.__get_path(view)
            ] for view in self.views
        ]
        if self.__get_setting('sort_views'):
            self.items = sorted(self.items)

    def select(self, index):
        if index != -1:
            self.window.focus_view(
                self.__get_view_by_path(self.items[index][1])
            )

    def __get_view_by_path(self, path):
        for view in self.views:
            if path == self.__get_path(view):
                return view

    def __get_display_name(self, view):
        mod_star = '*' if view.is_dirty() else ''

        if view.is_scratch() or not view.file_name():
            disp_name = view.name() if len(view.name()) > 0 else 'untitled'
        else:
            disp_name = os.path.basename(view.file_name())

        return '%s%s' % (disp_name, mod_star)

    def __get_path(self, view):
        if view.is_scratch():
            return ''

        if not view.file_name():
            return '<unsaved>'

        folders = self.window.folders()

        for folder in folders:
            if os.path.commonprefix([folder, view.file_name()]) == folder:
                relpath = os.path.relpath(view.file_name(), folder)

                if len(folders) > 1:
                    return os.path.join(os.path.basename(folder), relpath)

                return relpath

        return view.file_name()

    def __get_setting(self, key):
        view_settings = self.window.active_view().settings()
        if view_settings.has(SETTINGS_NAME):
            project_settings = view_settings.get(SETTINGS_NAME)
            for proj_setting_key in project_settings:
                if proj_setting_key == key:
                    return project_settings[proj_setting_key]

        plugin_settings = sublime.load_settings(SETTINGS_FILE_NAME)
        return plugin_settings.get(key, None)
