class MatchParameters:
    def __init__(self, field):
        self.__field = field
        self.blueRobotValues = field["blue"]
        self.yellowRobotValues = field["yellow"]
        self.ballValues = field["ball"]
        self.isYellowTeam = field["mray"]
