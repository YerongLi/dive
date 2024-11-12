#include <vector>
#include <cassert>
#include <iostream>
#include <algorithm>
using namespace std;
// Function prototype
vector<int> solution(const std::vector<int>& pairs)
{
    const int n = pairs.size();

    vector<vector<int>> pi;
    vector<int> ans(n, -0x7f7f7f7f);
    for (int i = 0; i < n; i++)
        pi.push_back({pairs[i], i});
    sort(pi.begin(), pi.end());
    int value = n;
    int found = 1, r = n;
    for (int l = 0; l < n; l++)
    {
        int c = pi[l][0], ii = pi[l][1];

        if (n - r  < c)
        {   
            while (n -r < c && value)
            {
                r--;
                ans[pi[r][1]] = value;
                value--;
            }

        }
        if (value)
        {
        
            if (r + 1 <= l)
                ans[pi[l][1]] = value;
            
            else
                ans[pi[l][1]] = -value;
             value--;

        }
        while (r >= 0 && r - 1 >= 0&& ans[pi[l][1]] + ans[pi[r - 1][1]] > 0)
        {
            r--;
        }
        if (n - r != c)
        {
            // cout << l << " c " << n - r << " " << c<<endl;
            found = 0;
            break;
        }
    }   
    if (!found) ans.clear();
    for (int x : ans) cout << x << " ";
    cout << endl;
    return ans;
}

int main() {
    // Test cases
    assert((solution({3, 2, 3}) == std::vector<int>{2, -1, 3}));
    assert((solution({0, 0, 0, 1}) == std::vector<int>{-4, -3, -2, 1}));
    assert((solution({6, 5, 5, 3, 3, 1}) == std::vector<int>{6, 3, 4, -2, -1, -5}));
    assert((solution({3, 3, 4, 1, 0}) == std::vector<int>{1, 2, 4, -3, -5}));
    assert((solution({1,1,1,1}) == std::vector<int>{}));

    std::cout << "All tests passed!" << std::endl;
    return 0;
}

