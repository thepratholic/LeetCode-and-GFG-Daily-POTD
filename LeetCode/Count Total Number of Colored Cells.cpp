class Solution
{
public:
    long long coloredCells(int n)
    {
        long long res = n;
        return 1 + (res - 1) * res * 2;
    }
};