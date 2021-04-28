from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class bde(Page):
    def is_displayed(self):
        return self.player.treatment_number=='t1_1'


class aef(Page):
    def is_displayed(self):
        return self.player.treatment_number=='t1_2'


class kjd(Page):
    def is_displayed(self):
        return self.player.treatment_number=='t2_1'


class bhc(Page):
    def is_displayed(self):
        return self.player.treatment_number=='t2_2'


class iud(Page):
    def is_displayed(self):
        return self.player.treatment_number=='t3_1'


class nsa(Page):
    def is_displayed(self):
        return self.player.treatment_number=='t3_2'



class Questions_1(Page):
    def vars_for_template(self):
        return {
            'image_path': 'corruption/{}.png'.format(self.player.treatment_number) 
        }
    form_model = 'player'
    form_fields = ['intelligence_c1',
                   'intelligence_c2',
                   'competence_c1',
                   'competence_c2',
                   'contract_c1',
                   'contract_c2',
                   'vote',
                   ]

class Questions_2(Page):
    def vars_for_template(self):
        return {
            'image_path': 'corruption/{}.png'.format(self.player.treatment_number)
        }
    form_model = 'player'
    form_fields = ['trust_c1',
                   'trust_c2',
                   'loyalty_c1',
                   'loyalty_c2',
                   'winner',
                   ]

class Raffle(Page):
    def is_displayed(self):
        return True
    form_model = 'player'
    form_fields = ['name',
                   'cell_number']

class Conclusion(Page):
    def is_displayed(self):
    	return True

page_sequence = [
    bde,
    aef,
    kjd,
    bhc,
    iud,
    nsa,
    Questions_1,
    Questions_2,
    Raffle,
    Conclusion
    ]
