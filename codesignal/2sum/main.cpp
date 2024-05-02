#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>

using namespace std;

vector<int> solution(vector<int>& a, vector<int>& b, vector<vector<int>>& queries) {
    // Preprocess frequency maps for both a and b lists
    unordered_map<int, int> freq_a, freq_b;
    for (int num : a) {
        freq_a[num]++;
    }
    for (int num : b) {
        freq_b[num]++;
    }

    // Function to count pairs for a given x
    auto countPairs = [&](int x) {
        int count = 0;
        for (auto& [num, freq] : freq_a) {
            int target = x - num;
            count += freq * freq_b[target];
        }
        return count;
    };

    vector<int> result;
    for (auto& query : queries) {
        if (query[0] == 0) {
            // Update b list
            int idx = query[1], val = query[2];
            int v = b[idx];
            freq_b[v]--;
            v += val;
            if (!freq_b.count(v)) freq_b[v] = 0;
            freq_b[v]++;
        } else if (query[0] == 1) {
            // Query for number of pairs
            int x = query[1];
            result.push_back(countPairs(x));
        }
    }

    return result;
}

int main() {
    vector<int> a = {1, 2, 2};
    vector<int> b = {2, 4};
    vector<vector<int>> queries = {{1, 4}, {0, 0, 3}, {1, 6}, {1, 7}};

    vector<int> expected = {2, 3, 2};
    vector<int> result = solution(a, b, queries);
    for (auto x : result) cout << x << " ";
    cout << endl;
    assert(result == expected);
    cout << "Test passed!" << endl;

    return 0;
}
