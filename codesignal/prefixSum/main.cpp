#include <iostream>
#include <cstring>
#include <unordered_set>
#include <unordered_map>
#include <vector>
using namespace std;

// I am took a codesignal that had a question where you had to count the total
 // number of words that are a suffix of another word in an array of strings. 
 // I did it n2 time using brute force approach but it wasn’t fast enough. 
// Does anyone know how to do it faster?
const int N = 100010, M = N * 27;


int tr[M][26], cnt[M], idx = 1;


// Insert a string into the Trie
void insert(string str)
{
   int p = 0;
   for (int i = str.length()- 1; i >= 0; i--)
   {
       int u = str[i] - 'a';
       if (!tr[p][u])
           tr[p][u] = ++idx;
       p = tr[p][u];
   }
   cnt[p]++;
}


// Search for a string or its suffix in the Trie
int search(string str)
{
   int p = 0;
   int res = 0;
   for (int i = str.length()- 1; i >= 0; i--)
   {
       int u = str[i] - 'a';
       if (!tr[p][u]) return 0;
       p = tr[p][u];
       res+= cnt[p];


   }
   return res - 1;
}

int solution(vector<string> &words)
{
   int n = sizeof(words) / sizeof(words[0]);
   memset(tr, 0, sizeof tr);
   memset(cnt, 0, sizeof cnt);
   int ans = 0;
   for (auto word : words) insert(word);
   for (auto word : words)
   {
       ans+= search(word);
   }
   cout << ans << endl;
   unordered_map<string, int> cmap;
   for (auto word : words)
   {
       if (!cmap.count(word)) cmap[word] = 0;
       cmap[word]++;
   }
   for (auto item : cmap)
   {
       ans-= (item.second * (item.second - 1)) /2;
   }
   return ans;
}


#include <cassert>

int main()
{
    vector<string> words;
    int expected, result;

    // Test Case 1: One word is a suffix of another
    words = {"apple", "banana", "orange", "e"};
    expected = 2;
    result = solution(words);
    assert(result == expected);
    cout << "Test Case 1 passed." << endl;

    // Test Case 2: Multiple words have the same suffix
    words = {"apple", "pineapple", "banana", "orange", "e"};
    expected = 4;
    result = solution(words);
    assert(result == expected);
    cout << "Test Case 2 passed." << endl;

    // Test Case 3: All words are suffixes of each other
    words = {"back", "backdoor", "door", "comeback", "door"};
    expected = 4;
    result = solution(words);
    assert(result == expected);
    cout << "Test Case 3 passed." << endl;

    // Test Case 4: Random case
    words = {"abcd", "bcde", "cdef", "defg", "efgh"};
    expected = 0; // No suffixes in this case
    result = solution(words);
    assert(result == expected);
    cout << "Test Case 4 passed." << endl;

    // Test Case 5: All words are the same
    words = {"same", "same", "same", "same"};
    expected = 6; // Combination of 4 choose 2
    result = solution(words);
    assert(result == expected);
    cout << "Test Case 5 passed." << endl;

    cout << "All test cases passed successfully." << endl;

    return 0;
}


// def count_suffix_pairs(words):
//     # Variable to store the count of pairs with shared suffixes
//     pairs_count = 0
//     # List to store all pairs
//     all_pairs = []

//     # Iterate over each word in the list of words
//     for i in range(len(words)):
//         for j in range(i+1, len(words)):
//             word1 = words[i]
//             word2 = words[j]
//             # Check if two words are identical
//             if word1 == word2:
//                 pairs_count += 1
//                 all_pairs.append((word1, word2))
//             else:
//                 # Check if one word is a suffix of the other
//                 if word1.endswith(word2) or word2.endswith(word1):
//                     pairs_count += 1
//                     all_pairs.append((word1, word2))

//     # Return the total count of pairs with shared suffixes and all pairs
//     return pairs_count, all_pairs

// # List of words to test the function
// words = ["back", "backdoor", "door", "comeback", "door"]
// # Call the function
// result_count, result_pairs = count_suffix_pairs(words)
// print("Number of pairs with shared suffixes:", result_count)
// print("All pairs with shared suffixes:", result_pairs)
