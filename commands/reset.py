import sublime
import sublime_plugin
from threading import Thread


from ..lib.ycmd_handler import server
from ..lib.ycmd_handler import deleteSingleton
from ..lib.utils import check_ycmd_server

output_panel = None


def reset_func():
    if not check_ycmd_server():
        sublime.message_dialog('Ycmd is not found, see https://github.com/glymehrvrd/CppYCM#installation for install instructions.')
        return

    try:
        server().Shutdown()
    except:
        pass
    deleteSingleton()
    a = server()



class CppycmResetCommand(sublime_plugin.WindowCommand):
    '''
    Restart ycmd server

    Last resort when server is down, user can manually restart it.
    '''

    def run(self):
        # start goto thread
        t = Thread(None, reset_func, 'ResetAsync' )
        t.daemon = True
        t.start()



    def is_enabled(self):
        return True

    def is_visible(self):
        return True

