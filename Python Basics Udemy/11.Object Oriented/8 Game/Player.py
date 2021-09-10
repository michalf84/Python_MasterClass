class Player(object):

    def __init__(self,name):
        self.name=name
        self.lives1=3
        self._level=1

        #neew method of decoreting score
        self._score=0

        self._lives=3


    def _get_lives(self):
        return self._lives

    def _set_lives(self,lives):
        if lives>=0:
            self._lives=lives
        else:
            print("_lives cannot be negatie")
            self._lives=0

    def _get_level(self):
        return self._level

    def _set_level(self,level):
        if level>0:
            delta=level-self._level
            self.score+=delta*1000
            self._level=level


    lives= property(_get_lives,_set_lives)
    level=property(_get_level,_set_level)

    #neew method of decoreting score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,score):
        self._score=score


# explanation https://www.programiz.com/python-programming/property


    def __str__(self):
        return "_name: {0.name},Lives {0.lives}, Level: {0.level}, score:{0.score}".format(self)
