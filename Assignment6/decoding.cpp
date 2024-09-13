#include <opencv2/opencv.hpp>
#include <bits/stdc++.h>
#include<fstream>
using namespace std;
using namespace cv;

class node {
    public:
    int value;
    long double probability;
    string symbol;
    node* left;
    node* right;
    node(){
        value=0;
        probability=0;
        symbol="";
        left=NULL;
        right=NULL;
    }
};
map<int,string>encoding;
node* createTree(vector<pair<long double, int>> probab,string code) {
    if (probab.empty()) {
        return NULL;
    }
    else if(probab.size()==1){
        node* leaf=new node();
        leaf->value=probab.front().second;
        leaf->probability=probab.front().first;
        leaf->symbol=code;
        leaf->left=NULL;
        leaf->right=NULL;
        encoding[leaf->value]=code;
        return leaf;
    }
    long double totalSum = 0;
    for (auto& p : probab) {
        totalSum += p.first;
    }
    vector<pair<long double, int>> group1, group2;
    double sum1 = 0, sum2 = 0;
    for (auto v : probab) {
        if (sum1 < totalSum / 2) {
            group1.push_back(v);
            sum1 += v.first;
        } else {
            group2.push_back(v);
            sum2 += v.first; // Initialize sum2
        }
    }
    node* root = new node();
    root->value = -1;
    root->probability = sum1 + sum2;
    root->left = createTree(group1,code+"0");
    root->right = createTree(group2,code+"1");
    return root;
}



int main() {
    Mat image = imread("../image.png");
    cout << image.size();
    cout << image.cols << "\n" << image.rows;
    Mat grayImage;
    cvtColor(image, grayImage, COLOR_BGR2GRAY);
    imshow("GrayImage", grayImage);
    waitKey(0);
    map<int, long double> freq;
    for (int i = 0; i < grayImage.rows; i++) {
        for (int j = 0; j < grayImage.cols; j++) {
            freq[grayImage.at<uchar>(i, j)] += 1;
        }
    }

    vector<pair<long double, int>> probab;
    for (int i = 0; i < 256; i++) {
        cout << "Value\t" << i << ":\t" << freq[i] << "\n";
        if (freq[i] != 0) {
            probab.push_back(make_pair(freq[i], i));
        }
    }
    sort(probab.rbegin(), probab.rend());
    int r = grayImage.rows;
    int c = grayImage.cols;
    int totalPixels = r * c;
    for (auto v : probab) {
        v.first /= totalPixels;
        cout << v.second << "\t" << v.first << "\n";
    }
    cout<<"\nTotal pixels"<<totalPixels;
    node* root = createTree(probab,"");
    for(auto v:encoding){
        cout<<"\n"<<v.first<<" "<<v.second;
    }
    ofstream file("imageEncoded.bin",ios::binary);
    if(!file){
        cerr<<"File not found"<<"\n";
        return 1;
    }
    for(auto v:encoding){
        file<<v.first<<" "<<v.second<<"\n";
    }
    int temp=0;int sizer=0;
    for (int i = 0; i < grayImage.rows; i++) {
        for (int j = 0; j < grayImage.cols; j++) {
          string code=encoding[grayImage.at<uchar>(i, j)];
          for(auto c:code){
            sizer++;
            if(sizer>24){
                char c1=0,c2=0,c3=0;
                for(int t=0;t<8;t++){
                    c1|=(temp&(1<<t));
                }
                for(int t=8;t<16;t++){
                    c2|=(temp&(1<<t));
                }
                for(int t=16;t<24;t++){
                    c3|=(temp&(1<<t));
                }
                temp=0;
                sizer=0;
                // file.write((char*)&c1,1);
                // file.write((char*)&c2,1);
                // file.write((char*)&c3,1);
                file<<c1<<c2<<c3;
            }
            if(c=='1'){
                temp<<=1;
                temp|=1;
            }else{
                temp<<1;
            }
           
            
          } 
        //   file<<code;  
        }
    }
    delete root;
    return 0;
}
