import sublime
import sublime_plugin

from ..lib.ycmd_handler import server
from ..lib.ycmd_handler import deleteSingleton

output_panel = None

class CppycmResetCommand(sublime_plugin.WindowCommand):
    '''
    Restart ycmd server

    Last resort when server is down, user can manually restart it. 
    '''

    def run(self):
        try:
            server().Shutdown()
        except:
            pass
        deleteSingleton()
        a = server()


    def is_enabled(self):
        return True

    def is_visible(self):
        return True

