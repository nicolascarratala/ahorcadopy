import pandas as pd 
import numpy sas np


def __init__(self, nombre="", dificultad="", score=0, level=0):
        self.dificultad = dificultad
        self.score = score
        self.level = level

    def draw(self):
        i = 1
        while i <= 6:
            print(" ")
            i += 1
        self.a = ("|-----     ")
        self.b = ("|   ( )    ")
        self.c = ("|    |     ")
        self.d = ("|   /|\    ")
        self.e = ("|  / | \   ")
        self.f = ("|    |     ")
        self.g = ("|    |     ")
        self.h = ("|   / \    ")
        self.i = ("|  /   \   ")
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)
        print(self.e)
        print(self.f)
        print(self.g)
        print(self.h)
        print(self.i)
        return

    def loop(self):
        while True:
            print(" ")
            self.input = input("Escriba letra: ")
            Ahorcado().draw()
            Ahorcado().letters()
            print(self.input)
