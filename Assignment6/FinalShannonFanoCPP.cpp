 
#include <opencv2/opencv.hpp>
#include <bits/stdc++.h>
using namespace std;
using namespace cv;
struct node{
  int value;
  long double probablity;
  node * left;
  node * right;
};
node* createTree(vector<pair<long double,int>>probab){
    if(probab.empty()){
      return NULL;
    }
    long double totalSum=0;
    for(auto &p:probab){
      totalSum+=p.first;
    }
    vector<pair<long double,int>>group1,group2;
    double sum1=0,sum2=0;
    for(auto v:probab){
      if(sum1<totalSum/2){
        group1.push_back(v);
        sum1+=v.first;
      }
      else{
        group2.push_back(v);
          sum2+v.first;
              }
    }
    node * root=new node();
    root->value=-1;
    root->probablity=sum1+sum2;
    root->left=createTree(group1);
    root->right=createTree(group2);
    return root;
}
void printTree(node * root,int level,string code){
  if(root==NULL){
    return;
  }
  for(int i=0;i<level;i++){
    cout<<" ";
  }
  if(root->left==NULL&&root->right==NULL){
    cout<<root->value<<"("<<root->probablity<<") -"<<code<<"\n";
  }
  else{
    cout<<root->value<<"("<<root->probablity<<")"<<"\n";

  }
  printTree(root->left,level+1,code+"0");
  printTree(root->right,level+1,code+"1");
}
int main() {
    
    Mat image = imread("../image.png");
    //cout<<image;
    cout<<image.size();
    cout<<image.cols<<"\n"<<image.rows;
    Mat grayImage;
    cvtColor(image,grayImage,COLOR_BGR2GRAY);
   imshow("GrayImage",grayImage);
   waitKey(0);
   map<int,long double>freq;
   for(int i=0;i<grayImage.rows;i++){
     for(int j=0;j<grayImage.cols;j++){
      freq[grayImage.at<uchar>(i,j)]+=1;
     }
   }

   vector<pair<long double,int>>probab;
   for(int i=0;i<256;i++){
     cout<<"Value\t"<<i<<":\t"<<freq[i]<<"\n";
     if(freq[i]!=0){
       probab.push_back(make_pair(freq[i],i));
     }
        
   }
   sort(probab.rbegin(),probab.rend());
   int r=grayImage.rows;
   int c=grayImage.cols;
   int totalPixels=r*c;
   for(auto v:probab){
     v.first/=totalPixels;
     cout<<v.second<<"\t"<<v.first<<"\n";
   }
   vector<pair<long double,int>>temp;
   temp.push_back({0.5,1});
   temp.push_back({0.25,2});
   temp.push_back({0.25,3});
   node* root=createTree(temp);
   
    return 0;
}

