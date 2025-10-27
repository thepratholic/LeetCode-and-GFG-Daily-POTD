from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)

        beams = 0

        for cur_row in range(m):
            cur_devices = 0
            
            for cell in range(len(bank[cur_row])):
                if bank[cur_row][cell] == '1':
                    cur_devices += 1

            if cur_devices > 0:

                for next_row in range(cur_row + 1, m):
                    other_floor_devices = 0

                    for cell_ in range(len(bank[next_row])):
                        if bank[next_row][cell_] == '1':
                            other_floor_devices += 1

                    if other_floor_devices > 0:
                        beams += (cur_devices * other_floor_devices)
                        break


        return beams
            