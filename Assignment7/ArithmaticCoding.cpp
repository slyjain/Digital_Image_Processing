#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;
    
    map<char, long double> freq;
    for (auto c : s) {
        freq[c] += 1;
    }
    
    long double totalLength = (long double) s.size();
    
    for (auto &v : freq) {
        v.second /= totalLength;
        cout << "Probability of " << v.first << ": " << v.second << endl;
    }
    
    long double prev = 0;
    map<char, long double> cumulativeFreq;
    for (auto &v : freq) {
        cumulativeFreq[v.first] = prev;
        prev += v.second;
    }
    
    cout << "\nCumulative frequencies:\n";
    for (auto &v : cumulativeFreq) {
        cout << v.first << ": " << v.second << endl;
    }
    
    long double lb = 0, ub = 1;
    
    for (int i = 0; i < s.size(); i++) {
        long double range = ub - lb;
        char currentChar = s[i];
        
        ub = lb + range * (cumulativeFreq[currentChar] + freq[currentChar]);
        lb = lb + range * cumulativeFreq[currentChar];
        
        cout << "Symbol: " << currentChar << " -> Range: [" << lb << ", " << ub << "]\n";
    }
    
    cout << "\nEncoded value: " << lb << endl;
    
    return 0;
}
