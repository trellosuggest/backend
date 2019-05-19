from typing import List


class BusynessCalculation:
    @staticmethod
    def calculate(people: List[List[int]]):
        people.sort(key=lambda x: sum(x), reverse=True)

        print(people)

        for person in people:
            person.sort()

        sum_max = sum(people[0])
        sum_min = sum(people[-1])

        while (sum_max != sum_min and (sum_max - people[0][0] != sum_min + people[0][0])
               and sum_max > sum_min + people[0][0]):
            people[-1].append(people[0][0])
            del people[0][0]

            people.sort(key=lambda x: sum(x), reverse=True)

            for person in people:
                person.sort()

            sum_max = sum(people[0])
            sum_min = sum(people[-1])

        print(people)

        return people
