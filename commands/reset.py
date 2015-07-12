import sublime
import sublime_plugin

from ..lib.ycmd_handler import server
from ..lib.ycmd_handler import deleteSingleton
from ..lib.utils import check_ycmd_server

output_panel = None

class CppycmResetCommand(sublime_plugin.WindowCommand):
    '''
    Restart ycmd server

    Last resort when server is down, user can manually restart it.
    '''

    def run(self):
        if not check_ycmd_server():
            sublime.message_dialog('Ycmd is not found, see https://github.com/glymehrvrd/CppYCM#installation for install instructions.')
            return

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

