import regex

from xchk_core.contentviews import ContentView
from xchk_core.strats import *
from xchk_regex_strategies.strats import RegexCheck
from xchk_multiple_choice_strategies.strats import MultipleChoiceAnswerCheck, MultipleChoiceFormatCheck

class MotivationView(ContentView):
     
    uid = 'xchk_xchk_content_motivation'
    template = 'xchk_xchk_content/motivation.html'
    title = 'Motivatie'
    _mc_data = [("Welke uitspraak of uitspraken zijn waar?",
                ("Studenten weten altijd precies wat verwacht wordt.",False,"Nog nooit foute bestanden gekregen? Zelfs geen foute bestandsnamen? Over het hoofd geziene leerstof?"),
                ("Onmiddellijke feedback is effectiever dan uitgestelde feedback.",True,"Kan je twee weken na datum het gedachtenproces dat tot een fout heeft geleid nog vlot herhalen?"),
                ("Lectoren wisselen probleemloos materiaal uit.",False,"Er zijn wel diensten zoals KlasCement, maar weet je altijd wat de verwachte voorkennis is,...?"),
                ("Studenten leren fouten vaak pas vermijden nadat ze zelf gemaakt hebben.",True,"Heeft het veel zin een lijst met \"frequently made mistakes\" zonder context te geven?"),
                ("Lectoren hebben meestal wel tijd voor differentiatie.",False,"Heb je rondgevraagd hoe veel collega's hier een prioriteit van kunnen maken?"))] 
    _mc_answer_check = MultipleChoiceAnswerCheck(filename=None,mc_data=_mc_data)
    custom_data = {'rendered_mc_qs': _mc_answer_check.render()}
    conditions = [FileExistsCheck(),MultipleChoiceFormatCheck(),_mc_answer_check]
    strat = Strategy(refusing_check=Negation(ConjunctiveCheck(conditions)),
                     accepting_check=TrueCheck())

class KeyElementsView(ContentView):
     
    uid = 'xchk_xchk_content_key_elements'
    template = 'xchk_xchk_content/key_elements.html'
    title = 'Sleutelementen van xchk'
    pattern = regex.compile(r'^\s*(2|[tT][wW][eE][eE])\s*$')
    conditions = [FileExistsCheck(),RegexCheck(pattern)]
    strat = Strategy(refusing_check=Negation(ConjunctiveCheck(conditions)),
                     accepting_check=TrueCheck())

class GitBenefitsView(ContentView):

    uid = 'xchk_xchk_content_git_benefits'
    template = 'xchk_xchk_content/git_benefits.html'
    title = 'Voordelen van Git bij het opbouwen van een portfolio'
    strat = Strategy(refusing_check=Negation(TrueCheck()),
                     accepting_check=TrueCheck())

class UndecidedStrategyView(ContentView):

    uid = 'xchk_xchk_content_undecided'
    template = 'xchk_xchk_content/undecided.html'
    title = 'Oefeningen waarover geen uitspraak gedaan kan worden'
    strat = Strategy(refusing_check=Negation(TrueCheck()),
                     accepting_check=Negation(TrueCheck()))

class UndecidedFollowupView(ContentView):

    uid = 'xchk_xchk_content_undecided_followup'
    template = 'xchk_xchk_content/undecided_followup.html'
    title = 'Het voordeel van de twijfel'
    strat = Strategy(refusing_check=Negation(TrueCheck()),
                     accepting_check=TrueCheck())

class SharedNodesView(ContentView):

    uid = 'xchk_xchk_content_shared_nodes'
    template = 'xchk_xchk_content/shared_nodes.html'
    title = 'Knooppunten gedeeld door meerdere cursussen'
    _mc_data = [("Kan één stukje informatie nuttig zijn op meerdere plaatsen?",
                  ("Ja",True,"Moet je bijvoorbeeld alleen kunnen vermenigvuldigen in de fysica, of heb je dat ook soms nodig in andere wetenschappen?"),
                  ("Nee",False,"Moet je bijvoorbeeld alleen kunnen vermenigvuldigen in de fysica, of heb je dat ook soms nodig in andere wetenschappen?"))] 
    _mc_answer_check = MultipleChoiceAnswerCheck(filename=None,mc_data=_mc_data)
    custom_data = {'rendered_mc_qs': _mc_answer_check.render()}
    conditions = [FileExistsCheck(),MultipleChoiceFormatCheck(),_mc_answer_check]
    strat = Strategy(refusing_check=Negation(ConjunctiveCheck(conditions)),
                     accepting_check=TrueCheck())

class DependencyStructureView(ContentView):

    uid = 'xchk_xchk_content_dependency_structure'
    template = 'xchk_xchk_content/dependency_structure.html'
    title = 'Een structuur van afhankelijkheden'
    _mc_data = [("Welke pijlen moet je afwerken vooraleer je een knooppunt mag gebruiken?",
                  ("Alle inkomende pijlen",False,"Als je in school A hebt vermenigvuldigen en je stapt over naar school B, moet je daar dan opnieuw leren vermenigvuldigen voor je kan leren machtsverheffen?"),
                  ("Minstens één inkomende pijl",False,"Kan je bv. appeltaart maken als je alleen vulling of alleen de deegkorst kan maken?"),
                  ("Alle inkomende pijlen binnen één cursus die de knoop bevat",True,"Eens je een competentie hebt, maakt het dan echt uit waar je die verworven hebt?"))] 
    _mc_answer_check = MultipleChoiceAnswerCheck(filename=None,mc_data=_mc_data)
    custom_data = {'rendered_mc_qs': _mc_answer_check.render()}
    conditions = [FileExistsCheck(),MultipleChoiceFormatCheck(),_mc_answer_check]
    strat = Strategy(refusing_check=Negation(ConjunctiveCheck(conditions)),
                     accepting_check=TrueCheck())

class EssentialNonEssentialsView(ContentView):

    uid = 'xchk_xchk_content_essentials_non_essentials'
    template = 'xchk_xchk_content/essentials_non_essentials.html'
    title = 'Basisdoelstellingen en differentiatie'
    strat = Strategy(refusing_check=Negation(TrueCheck()),
                     accepting_check=TrueCheck())

class InstructionsView(ContentView):

    uid = 'xchk_xchk_content_technical_requirements'
    template = 'xchk_xchk_content/technical_requirements.html'
    title = 'Technische vereisten'
    pattern = regex.compile(r'^.*[0-9].*$',flags=regex.DOTALL)
    chk = ConjunctiveCheck([FileExistsCheck(),Negation(RegexCheck(pattern,pattern_description="tekst met minstens één cijfer in"))])
    strat = Strategy(refusing_check=Negation(chk),
                     accepting_check=TrueCheck())

class ModularCourseMaterialView(ContentView):

    uid = 'xchk_xchk_content_modular_material'
    template = 'xchk_xchk_content/modular_material.html'
    title = 'Modulaire cursussen'
    strat = Strategy(refusing_check=Negation(TrueCheck()),
                     accepting_check=TrueCheck())

class ModularChecksView(ContentView):

    uid = 'xchk_xchk_content_modular_checks'
    template = 'xchk_xchk_content/modular_checks.html'
    title = 'Modulaire controleprocedures'
    # TODO iets complexer illustreren
    # bv. programma a berekent hetzelfde als programma b (Python?)
    strat = Strategy(refusing_check=Negation(TrueCheck()),
                     accepting_check=TrueCheck())

class RandomizedExercisesView(ContentView):

    uid = 'xchk_xchk_content_randomized_exercises'
    template = 'xchk_xchk_content/randomized_exercises.html'
    title = 'Willekeurige oefeningen'
    strat = Strategy(refusing_check=Negation(TrueCheck()),
                     accepting_check=TrueCheck())

class MCDemoView(ContentView):

    uid = 'xchk_xchk_content_mc_demo'
    template =  'xchk_xchk_content/mc_demo.html'
    title = 'Demonstratie multiple choice'
    _mc_data = [("Rozen zijn (meestal)",
                 ("rood",True,None),
                 ("groen",False,"De steel misschien, maar je weet dat dat niet is wat we bedoelen..."),
                 ("geel",False,"Gele rozen bestaan, maar zijn dat diegene die je het meeste ziet?"),
                 ("bloemen",True,None)),
                ("Spinazie is",
                 ("blauw",False,"Blauwe spinazie? Dat klinkt verontrustend."),
                 ("paars",False,"Je denkt misschien aan rode kool. Die niet echt rood is."),
                 ("groen",True,None))] 
    _mc_answer_check = MultipleChoiceAnswerCheck(filename=None,mc_data=_mc_data)
    custom_data = {'rendered_mc_qs': _mc_answer_check.render()}
    conditions = [FileExistsCheck(),MultipleChoiceFormatCheck(),_mc_answer_check]
    strat = Strategy(refusing_check=Negation(ConjunctiveCheck(conditions)),
                     accepting_check=TrueCheck())


