import sublime, sublime_plugin, os

class GotoOpenFileCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    window = sublime.active_window()
    selector = ViewSelector(window)
    
    window.show_quick_panel(selector.get_items(), selector.select)

class ViewSelector(object):

  def __init__(self, window):
    self.window = window
    self.views = window.views()

  def select(self, index):
    if index != -1:
      self.window.focus_view(self.views[index])

  def get_items(self):
    return [[self.__get_display_name(view), self.__get_path(view)] for view in self.views]

  def __get_display_name(self, view):
    if view.is_scratch():
      return view.name()

    return os.path.basename(view.file_name())

  def __get_path(self, view):
    if view.is_scratch():
      return view.name()
    
    folders = self.window.folders()

    for folder in folders:
      if os.path.commonprefix([folder, view.file_name()]) == folder:
        relpath = os.path.relpath(view.file_name(), folder)
        
        if len(folders) > 1:
          return os.path.join(os.path.basename(folder), relpath)

        return relpath

    return view.file_name()
    