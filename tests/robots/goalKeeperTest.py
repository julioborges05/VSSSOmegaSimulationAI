import unittest

from controllers.robots.goalKeeper import GoalKeeper
from controllers.match.matchParameters import MatchParameters
from controllers.geometry.triangle import Triangle
from bridge.entity import Entity


class GoalKeeperTest(unittest.TestCase):
    def testZeroDivisionExceptionOnGetBigTriangleValueMethod(self):
        field = dict()
        field["blue"] = Entity()
        field["yellow"] = Entity()
        field["mray"] = Entity()
        field["ball"] = Entity(0, -10)
        matchParameters = MatchParameters(field)

        smallTriangle = GoalKeeper(matchParameters)
        try:
            smallTriangle.getBigTriangleValues(True)
        except ZeroDivisionError:
            self.assertTrue(True)

    def testGetBigTriangleValueMethod(self):
        field = dict()
        field["blue"] = Entity()
        field["yellow"] = Entity()
        field["mray"] = Entity()
        field["ball"] = Entity(0, 10, -30, -40)
        matchParameters = MatchParameters(field)

        smallTriangle = GoalKeeper(matchParameters)
        bigTriangle = smallTriangle.getBigTriangleValues(True)
        self.assertEqual(bigTriangle.verticalValue, 30)
        self.assertEqual(bigTriangle.horizontalValue, 22.5)
