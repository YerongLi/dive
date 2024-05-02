#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <set>
using namespace std;

string binarySearch(vector<int>& obs, int pos, int size) {
    int start = 0;
    int end = obs.size() - 1;
    int ub = pos + size;
    if (ub <= obs[0] || pos > obs.back()) {
        return "1";
    }
    while (start <= end) {
        int mid = start + (end - start) / 2;
        if (pos <= obs[mid] && obs[mid] < ub) {
            return "0";
        } else if (obs[mid] < pos) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    return "1";
}

string solution1(vector<vector<int>>& operations) {
    vector<int> obs;
    string res;
    for (auto& op : operations) {
        if (op[0] == 1) {
            auto it = upper_bound(obs.begin(), obs.end(), op[1]);
            obs.insert(it, op[1]);
        }
        if (op[0] == 2) {
            res += binarySearch(obs, op[1], op[2]);
        }
    }
    return res;
}
string solution(vector<vector<int>> operations)
{
  vector<char> ans;
  set<int> xs;
  for (auto  o : operations)
  {
    if (o[0] == 1)
    {
      int x = o[1];
      xs.insert(x);
    }
    else {
      int x = o[1], sz = o[2];
      //  [x, x + sz - 1]
      auto a = lower_bound(xs.begin(), xs.end(), x);
      auto b = lower_bound(xs.begin(), xs.end(), x + sz -1);
      if (a == b && (a == xs.end() || *a != x ) && (a == xs.end() || *a != x+ sz -1))
      ans.push_back('1');
      else
       ans.push_back('0');

    }
  }
    return string(ans.begin(), ans.end());

}
int main() {
    vector<vector<int>> operations = {{1, 2}, {1, 5}, {2, 3, 2}, {2, 3, 3}, {2, 1, 1}, {2, 1, 2}};
    string expected = solution1(operations);
    string result = solution(operations);
    cout << expected << endl;
    cout << result << endl;

    // string result = "101";
    
    assert(result == expected);

    cout << "All test cases have passed." << endl;
    return 0;
}

