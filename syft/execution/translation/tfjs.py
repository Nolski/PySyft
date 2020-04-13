from torch import jit
from pythreepio.threepio import Threepio
from pythreepio.utils import Command
from syft.common.util import TranslationTargets
from syft.execution import Plan
from syft.execution.computation import ComputationAction
from syft.execution.translation.abstract import AbstractPlanTranslator


class PlanTranslatorTfjs(AbstractPlanTranslator):
    """Performs translation from 'list of ops' Plan into torchscript Plan"""

    def __init__(self, plan):
        self.threepio = Threepio('torch', 'tfjs', None)
        super().__init__(plan)

    def translate(self):
        plan = self.plan.copy()
        for action in plan.role.actions:
            action.base_framework = TranslationTargets.TENSORFLOW_JS
        return plan
