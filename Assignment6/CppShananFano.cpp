#include<bits/stdc++.h>
using namespace std;
void generateStrings(vector<pair<float,int>>&pp,vector<string>&encStrings,float totalSum, int start,int end,string adder){
  if(start==end){
    encStrings[pp[start].second]+=adder;
    return;
  }
    float sum=pp[start].first;
    int m=start+1;
    
    while(m<=end&&sum<totalSum/2){
      sum+=pp[m].first;
      m++;
    }
    generateStrings(pp,encStrings,sum,start,m-1,adder+'0');
    generateStrings(pp,encStrings,totalSum-sum,m,end,adder+'1');
}
int main(){
   vector<float> probab={0.12,0.15,0.25,0.3,0.08,0.1};
    vector<pair<float,int>>pp;
    for(int i=0;i<probab.size();i++){
      pp.push_back(make_pair(probab[i],i));
    }
    sort(pp.rbegin(),pp.rend());
    vector<string>encStrings(probab.size());
    generateStrings(pp,encStrings,1,0,probab.size()-1,"");
    for( int i=0;i<probab.size();i++){
      cout<<"Probablity :"<<probab[i]<<" -> Encoding: "<<encStrings[i]<<"\n";
    }
}
