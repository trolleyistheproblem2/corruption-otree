from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import itertools


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        treatment_number = itertools.cycle(['t1_1', 't1_2', 't2_1', 't2_2', 't3_1', 't3_2'])
        for p in self.get_players():
            p.treatment_number = next(treatment_number)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment_number = models.StringField()

    intelligence_c1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1, 2 ,3 , 4 ,5 ,6 ,7 ,8 ,9 ,10])

    intelligence_c2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1, 2 ,3 , 4 ,5 ,6 ,7 ,8 ,9 ,10])

    competence_c1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1, 2 ,3 , 4 ,5 ,6 ,7 ,8 ,9 ,10])

    competence_c2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=[1, 2 ,3 , 4 ,5 ,6 ,7 ,8 ,9 ,10])

    vote = models.StringField(widget=widgets.RadioSelect, choices=['First candidate','Second candidate','Neither candidate','''Don't know/ Won't answer'''])

    winner = models.StringField(widget=widgets.RadioSelect, choices=['First candidate','Second candidate','Neither candidate','''Don't know/ Won't answer'''])

    trust_c1 = models.StringField(widget=widgets.RadioSelect, choices=['A lot', 'A little', 'Not at all'])

    trust_c2 = models.StringField(widget=widgets.RadioSelect, choices=['A lot', 'A little', 'Not at all'])

    loyalty_c1 = models.StringField(widget=widgets.RadioSelect, choices=['A lot', 'A little', 'Not at all'])

    loyalty_c2 = models.StringField(widget=widgets.RadioSelect, choices=['A lot', 'A little', 'Not at all'])

    contract_c1 = models.StringField(widget=widgets.RadioSelect, choices=['A lot', 'A little', 'Not at all'])

    contract_c2 = models.StringField(widget=widgets.RadioSelect, choices=['A lot', 'A little', 'Not at all'])

    name = models.StringField(blank=True)

    cell_number = models.StringField(blank=True)

