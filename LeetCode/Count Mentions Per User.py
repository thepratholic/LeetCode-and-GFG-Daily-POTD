from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        n = numberOfUsers
        mentions = [0] * n
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        online = set(range(n))
        offline = {}  # id -> timestamp + 60

        for msg, time_stamp, ids in events:
            time_stamp = int(time_stamp)

            # bring all expired offline users back
            to_add = []
            for k, v in offline.items():
                if v <= time_stamp:
                    to_add.append(k)

            for u in to_add:
                online.add(u)
                del offline[u]

            if msg == "OFFLINE":
                uid = int(ids)
                if uid in online:
                    online.discard(uid)
                offline[uid] = time_stamp + 60

            else:  # MESSAGE
                if ids == "ALL":
                    for i in range(n):
                        mentions[i] += 1

                elif ids == "HERE":
                    for i in online:
                        mentions[i] += 1

                else:
                    users = ids.split()
                    for s in users:
                        if s.startswith("id"):
                            cur = int(s[2:])
                            mentions[cur] += 1

        return mentions
