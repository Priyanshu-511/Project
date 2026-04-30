#include<iostream>
#include<fstream>
#include<string.h>
#include<sstream>
using namespace std;

int main(){
    string str1,str2;
    ifstream out1,out2;
    out1.open("output.txt");
    // FIXED: Use getline instead of eof() - eof() is unreliable
    while(getline(out1,str1)){ 
        // Read last line
    }
    out1.close();
    
    out2.open("run.txt");
    // FIXED: Use getline instead of eof() - eof() is unreliable
    while(getline(out2,str2)){ 
        // Read last line
    }
    out2.close();

    // FIXED: Removed unused stringstream objects s1 and s2
    
    if(str1==str2){
        cout<<"Test-case passed:\n";
    }
    else{
        cout<<"Test-case failed:\n";
    }
}