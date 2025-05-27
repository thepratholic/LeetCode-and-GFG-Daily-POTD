class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        n_list = []
        for i in range(1, n + 1):
            if i % m != 0:
                n_list.append(i)

        m_list = []
        for i in range(1, n + 1):
            if i % m == 0:
                m_list.append(i)

        return sum(n_list) - sum(m_list)