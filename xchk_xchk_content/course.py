from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('xchk',
                'Xchk',
                [(ModularCourseMaterialView,[DependencyStructureView,InstructionsView]),
                 (InstructionsView,[KeyElementsView]),
                 (EssentialNonEssentialsView,[DependencyStructureView]),
                 (DependencyStructureView,[SharedNodesView]),
                 (SharedNodesView,[KeyElementsView]),
                 (UndecidedStrategyView,[KeyElementsView]),
                 (GitBenefitsView,[KeyElementsView]),
                 (KeyElementsView,[MotivationView]),
                 (MotivationView,[])])
