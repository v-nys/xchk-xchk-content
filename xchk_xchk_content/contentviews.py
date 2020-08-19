from xchk_core.contentviews import ContentView
from xchk_core.strats import *
from xchk_regex_strategies.strats import RegexCheck
from xchk_multiple_choice_strategies.strats import MultipleChoiceAnswerCheck, MultipleChoiceFormatCheck

class DemoXchkView(ContentView):
     
    uid = 'xchk_xchk_content_motivation'
    template = 'xchk_xchk_content/motivation.html'
    title = 'motivatie'
    mc_data = [("Welke uitspraak of uitspraken zijn waar?",
                ("Studenten weten altijd precies wat verwacht wordt.",False,"Nog nooit foute bestanden gekregen? Zelfs geen foute bestandsnamen? Over het hoofd geziene leerstof?"),
                ("Onmiddellijke feedback is effectiever dan uitgestelde feedback.",True,"Kan je twee weken na datum het gedachtenproces dat tot een fout heeft geleid nog vlot herhalen?"),
                ("Lectoren wisselen probleemloos materiaal uit.",False,"Er zijn wel diensten zoals KlasCement, maar weet je altijd wat de verwachte voorkennis is,...?"),
                ("Studenten leren fouten vaak pas vermijden nadat ze zelf gemaakt hebben.",True,"Heeft het veel zin een lijst met \"frequently made mistakes\" zonder context te geven?"),
                ("Lectoren hebben meestal wel tijd voor differentiatie.",False,"Heb je rondgevraagd hoe veel collega's hier een prioriteit van kunnen maken?"))] 
    _mc_answer_check = MultipleChoiceAnswerCheck(filename=None,mc_data)
    custom_data = {'rendered_mc_qs': _mc_answer_check.render()}
    conditions = [FileExistsCheck(),MultipleChoiceFormatCheck(),_mc_answer_check]
    strat = Strategy(refusing_check=Negation(ConjunctiveCheck(conditions)),
                     accepting_check=TrueCheck())

class KeyElementsView(ContentView):
     
    uid = 'xchk_xchk_content_key_elements'
    template = 'xchk_xchk_content/key_elements.html'
    title = 'Sleutelementen van xchk'
    conditions = [FileExistsCheck(),RegexCheck()]
    strat = Strategy(refusing_check=Negation(ConjunctiveCheck(conditions)),
                     accepting_check=TrueCheck())

 
