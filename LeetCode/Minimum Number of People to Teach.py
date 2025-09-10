from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        friendships.sort(key = lambda x : (x[0], x[1]))
        pairs = []
        size = len(friendships)

        for i in range(size):

            first_user = friendships[i][0] - 1
            second_user = friendships[i][1] - 1

            fl = False
            for lang in languages[first_user]:
                if lang in languages[second_user]:
                    fl = True
                    break

            if not fl:
                pairs.append([first_user, second_user])

        users_to_fix = set()

        for u, v in pairs:
            users_to_fix.add(u)
            users_to_fix.add(v)

        maxi = 0
        for lang in range(1, n + 1):
            count = 0
            for user in users_to_fix:
                if lang in languages[user]:
                    count += 1

            maxi = max(maxi, count)

        return len(users_to_fix) - maxi