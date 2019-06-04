class BusynessCalculation:
    @staticmethod
    def calculate(people):
        moves = []

        people.sort(key=lambda x: sum([y['story'] for y in x['cards']]), reverse=True)

        for person in people:
            person['cards'].sort(key=lambda x: x['story'])

        sum_max = sum([x['story'] for x in people[0]['cards']])
        sum_min = sum([x['story'] for x in people[-1]['cards']])

        while (sum_max != sum_min
               and sum_max > sum_min + people[0]['cards'][0]['story']):

            moves.append({'what': people[0]['cards'][0]['name'],
                          'from': people[0]['fullName'],
                          'to': people[-1]['fullName']})

            people[-1]['cards'].append(people[0]['cards'][0])
            del people[0]['cards'][0]

            people.sort(key=lambda x: sum([y['story'] for y in x['cards']]), reverse=True)

            for person in people:
                person['cards'].sort(key=lambda x: x['story'])

            sum_max = sum([x['story'] for x in people[0]['cards']])
            sum_min = sum([x['story'] for x in people[-1]['cards']])

        return moves
