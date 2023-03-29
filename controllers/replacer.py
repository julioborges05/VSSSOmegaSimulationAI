from bridge.bridgeReplacer import BridgeReplacer

FREE_KICK = 0
PENALTY_KICK = 1
GOAL_KICK = 2
FREE_BALL = 3
KICKOFF = 4
STOP = 5
GAME_ON = 6
HALT = 7


class Replacer:
    def __init__(self, replacement):
        self.placementList = None
        self.replacement = replacement

    def setDefaultPositions(self, ref_data, myRobotsAreYellow):
        if ref_data["foul"] == PENALTY_KICK:
            self.replacePenaltyFoul(ref_data, myRobotsAreYellow)

        if ref_data["foul"] == GOAL_KICK:
            self.replaceGoalKick(ref_data, myRobotsAreYellow)

        if ref_data["foul"] == KICKOFF:
            self.replaceKickOff(ref_data, myRobotsAreYellow)
        BridgeReplacer.send(self.replacement)

    # Penalty
    def replacePenaltyFoul(self, ref_data, myRobotsAreYellow):
        # Penalty for yellow teams and my team is yellow
        if ref_data["yellow"] and myRobotsAreYellow:
            BridgeReplacer.place(self.replacement, 0, 75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, -35, 10, 90)
            BridgeReplacer.place(self.replacement, 2, -25, -10, 90)

        # Penalty for yellow teams and my team is blue
        elif ref_data["yellow"] and not myRobotsAreYellow:
            BridgeReplacer.place(self.replacement, 0, -75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, 35, 10, 90)
            BridgeReplacer.place(self.replacement, 2, 25, -10, 90)

        # Penalty for blue teams and my team is yellow
        elif not ref_data["yellow"] and myRobotsAreYellow:
            BridgeReplacer.place(self.replacement, 0, 75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, 35, 10, 90)
            BridgeReplacer.place(self.replacement, 2, 25, -10, 90)

        # Penalty for blue teams and my team is blue
        else:
            BridgeReplacer.place(self.replacement, 0, -75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, 35, 10, 90)
            BridgeReplacer.place(self.replacement, 2, 25, -10, 90)

    # Goal Kick
    def replaceGoalKick(self, ref_data, myRobotsAreYellow):
        # Penalty for yellow teams and my team is yellow
        if ref_data["yellow"] and myRobotsAreYellow:
            BridgeReplacer.place(self.replacement, 0, 75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, -35, 10, 90)
            BridgeReplacer.place(self.replacement, 2, -25, -10, 90)

        # Penalty for yellow teams and my team is blue
        elif ref_data["yellow"] and not myRobotsAreYellow:
            BridgeReplacer.place(self.replacement, 0, -75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, 20, 42, -45)
            BridgeReplacer.place(self.replacement, 2, 25, -40, 45)

        # Penalty for blue teams and my team is yellow
        elif not ref_data["yellow"] and myRobotsAreYellow:
            BridgeReplacer.place(self.replacement, 0, 75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, 35, 10, 90)
            BridgeReplacer.place(self.replacement, 2, 25, -10, 90)

        # Penalty for blue teams and my team is blue
        else:
            BridgeReplacer.place(self.replacement, 0, -75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, -68, 42, -45)
            BridgeReplacer.place(self.replacement, 2, 25, -10, 90)

    # KickOff
    def replaceKickOff(self, ref_data, myRobotsAreYellow):
        # KickOff for yellow teams and my team is yellow
        if ref_data["yellow"] and myRobotsAreYellow:
            BridgeReplacer.place(self.replacement, 0, 75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, 35, 10, 90)
            BridgeReplacer.place(self.replacement, 2, 25, -10, 90)

        # KickOff for yellow teams and my team is blue
        elif ref_data["yellow"] and not myRobotsAreYellow:
            BridgeReplacer.place(self.replacement, 0, -75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, -35, 20, 90)
            BridgeReplacer.place(self.replacement, 2, -25, -10, 90)

        # KickOff for blue teams and my team is yellow
        elif not ref_data["yellow"] and myRobotsAreYellow:
            BridgeReplacer.place(self.replacement, 0, 75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, 35, 10, 90)
            BridgeReplacer.place(self.replacement, 2, 25, -10, 90)

        # KickOff for blue teams and my team is blue
        else:
            BridgeReplacer.place(self.replacement, 0, -75, 0, 90)
            BridgeReplacer.place(self.replacement, 1, -35, 20, 90)
            BridgeReplacer.place(self.replacement, 2, -10, -7, 35)
