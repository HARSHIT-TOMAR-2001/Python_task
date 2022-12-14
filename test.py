import unittest
import calculation


class TestCalc(unittest.TestCase):
    def test_calculate1(self):
        self.assertEqual(calculation.CalcTotalSeatCount([[3,4], [4,5], [2,3], [3,4]]),50)
        self.assertEqual(calculation.CalculateSeatDistribution([[3,4], [4,5], [2,3], [3,4]]),(18,6,26))
        self.assertEqual(calculation.CalculateSeatDistributionAmongPassenger([[3,4], [4,5], [2,3], [3,4]],30),(18,6,6))

    def test_calculate2(self):
        self.assertEqual(calculation.CalcTotalSeatCount([[3,2], [4,3], [2,3], [3,4]]),36)
        self.assertEqual(calculation.CalculateSeatDistribution([[3,2], [4,3], [2,3], [3,4]]),(18,6,12))
        self.assertEqual(calculation.CalculateSeatDistributionAmongPassenger([[3,2], [4,3], [2,3], [3,4]],30),(18,6,6))


if __name__=="__main__":
    unittest.main()


