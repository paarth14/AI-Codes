# Expert System - Airline System

# pip install experta
from experta import *
from random import randint
# from collections.abc import Mapping
# from collections import Mapping


class windSpeed(Fact):
    """ info of wind speed"""
    pass


class ATS(KnowledgeEngine):

    @Rule(windSpeed(P(lambda x: x < 5)))
    def perfect(self):

        print("Perfect wind speed to land go ahead !")

    @Rule(windSpeed(P(lambda x: x >= 5) & P(lambda x: x <= 10)))
    def caution(self):
        print("Wind speed is bit high. Proceed with caution")

    @Rule(windSpeed(P(lambda x: x > 10)))
    def dont(self):
        print("Wind Speed to high do not try to land.. Crash imminent ")


engine = ATS()
engine.reset()
engine.declare(windSpeed(randint(0, 12)))
engine.run()
