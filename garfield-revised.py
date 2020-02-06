from time import sleep
from termcolor import colored

class Bot:
    
    wait = 1
    
    def __init__(self):
        self.q = ''
        self.a = ''
        
    def _think(self, s):
        return s
    
    def _format(self, s):
        return colored(s, 'green')
    
    def run(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        sleep(Bot.wait)
        print(self._format(self._think(self.a)))
        
class HelloBot(Bot):
    def __init__(self):
        self.q = "Hi, what is your name?"
        
    def _think(self, s):
        return f"Hello {s}"
    
class GreetingBot(Bot):
    def __init__(self):
        self.q = "How are you today?"
        
    def _think(self, s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too."
        else:
            return "Sorry to hear that."

import random

class FavoriteColorBot(Bot):
    def __init__(self):
        self.q = "What's your favorite color?"
        
    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"
    
from simpleeval import simple_eval

class CalcBot(Bot):
    def __init__(self):
        self.q = "Through recent upgrade I can do calculation now. Input some arithmetic expression to try, input 'q' 'x' 'quit' or 'exit' to quit:"

    def _think(self, s):
        result = simple_eval(s)
        return f"Done. Result = {result}"
    
    def run(self):
        sleep(Bot.wait)
        print(self._format(self.q))
        while True:
            self.a = input()
            if self.a.lower() in ['q', 'x', 'quit', 'exit']:
                break
            sleep(Bot.wait)
            print(self._format(self._think(self.a)))
            
class Garfield:
    
    def __init__(self, wait = 1):
        Bot.wait = wait
        self.bots = []
        
    def add(self, bot):
        self.bots.append(bot)
        
    def _prompt(self, s):
        print(s)
        print()
        
    def run(self):
        self._prompt("This is Garfield dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()
            
            
garfield = Garfield(1)

garfield.add(HelloBot())
garfield.add(CalcBot())
garfield.add(FavoriteColorBot())

garfield.run()