import unittest
from busyness_calculation.busyness_calculation import BusynessCalculation


class CalculatorTestingModule(unittest.TestCase):

    def get_dataset(self):
        return [
            {
                'fullName': 'a',
                'cards': [
                    {'name': 'aa', 'story': 2},
                    {'name': 'ab', 'story': 7},
                    {'name': 'ac', 'story': 2},
                    {'name': 'ad', 'story': 3}
                ]
            },
            {
                'fullName': 'b',
                'cards': [
                    {'name': 'ba', 'story': 1},
                    {'name': 'bb', 'story': 1},
                    {'name': 'bc', 'story': 3},
                    {'name': 'bd', 'story': 8}
                ]
            },
            {
                'fullName': 'c',
                'cards': [
                    {'name': 'ca', 'story': 5},
                    {'name': 'cb', 'story': 8},
                    {'name': 'cc', 'story': 1},
                    {'name': 'cd', 'story': 10}
                ]
            },
            {
                'fullName': 'd',
                'cards': [
                    {'name': 'da', 'story': 10},
                    {'name': 'db', 'story': 6},
                    {'name': 'dc', 'story': 1},
                    {'name': 'dd', 'story': 5}
                ]
            }
        ]

    def test_non_changing(self):
        dataset = self.get_dataset()
        length = len(dataset)
        BusynessCalculation.calculate(dataset)
        self.assertEqual(length, len(dataset))

        self.assertTrue('a' in [x['fullName'] for x in dataset])
        self.assertTrue('b' in [x['fullName'] for x in dataset])
        self.assertTrue('c' in [x['fullName'] for x in dataset])
        self.assertTrue('d' in [x['fullName'] for x in dataset])

    def test_correctness(self):
        dataset = self.get_dataset()
        dataset.sort(key=lambda x: sum([y['story'] for y in x['cards']]), reverse=True)
        delta_min_max = sum([x['story'] for x in dataset[0]['cards']]) - sum([x['story'] for x in dataset[-1]['cards']])
        BusynessCalculation.calculate(dataset)
        d1 = sum([x['story'] for x in dataset[0]['cards']]) - sum([x['story'] for x in dataset[-1]['cards']])
        self.assertTrue(delta_min_max > d1)
