from xchk_core.contentviews import ContentView
from xchk_core.strats import *

class DemoXchkView(ContentView):
     
    uid = 'xchk_xchk_content_demo'
    template = 'xchk_xchk_content/xchk_xchk_content_demo.html'
    strat = Strategy(refusing_check=TrueCheck(),
                     accepting_check=Negation(TrueCheck()))
