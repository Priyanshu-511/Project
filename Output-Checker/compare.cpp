#include<iostream>
#include<fstream>
#include<string.h>
#include<sstream>
using namespace std;

int main(){
    string str1,str2;
    ifstream out1,out2;
    out1.open("output.txt");
    while(!out1.eof()){
        getline(out1,str1);
    }
    out1.close();
     out2.open("run.txt");
     while(!out2.eof()){
        getline(out2,str2);
    }
    out2.close();

    stringstream s1(str1);
    stringstream s2(str2);
    
    if(str1==str2){
        cout<<"Test-case passed:\n";
    }
    else{
        cout<<"Test-case failed:\n";
    }
}