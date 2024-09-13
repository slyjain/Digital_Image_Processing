
#include<bits/stdc++.h>
using namespace std;

void generateStrings(vector<pair<float, int>>& pp, vector<string>& encStrings, float totalSum, int start, int end, string adder,bool oddSplit) {
    if (start == end) {
        // Assign the adder string when there's only one element left
        encStrings[pp[start].second] += adder;
        if(oddSplit&&end==pp.size()-1){
          encStrings[pp[start].second]+='0';
        }
        return;
    }

    float sum = pp[start].first;
    int m = start + 1;

    // Accumulate the sum until it's close to half of the total sum
    while (m <= end && sum <= totalSum / 2) {
        sum += pp[m].first;
        m++;
    }
    bool topSplit=(((m-1)-start+1)%2),bottomSplit=((end-m+1)%2);
    // Recursive calls for left and right splits
    
    generateStrings(pp, encStrings, sum, start, m - 1, adder + '0',topSplit);
    generateStrings(pp, encStrings, totalSum - sum, m, end, adder + '1',bottomSplit);
}

int main() {
    // Example probabilities
    int n;
    cin>>n;

    vector<float> probab;
    for(int i=0;i<n;i++){
      float x;
      cin>>x;
      probab.push_back(x);
    }
    vector<pair<float, int>> pp;

    // Pair the probabilities with their original indices
    for (int i = 0; i < probab.size(); i++) {
        pp.push_back(make_pair(probab[i], i));
    }

    // Sort the probabilities in descending order
    sort(pp.rbegin(), pp.rend());

    // Initialize the encoding strings
    vector<string> encStrings(probab.size());
    bool oddSplit;
    if(probab.size()%2==1){
      oddSplit=true;
    }
    // Generate the Shannon-Fano encodings
    generateStrings(pp, encStrings, 1, 0, probab.size() - 1, "",oddSplit);

    // Output the probabilities and their corresponding encodings
    for (int i = 0; i < probab.size(); i++) {
        cout << "Probability: " << probab[i] << " -> Encoding: " << encStrings[i] << "\n";
    }

    return 0;
}
