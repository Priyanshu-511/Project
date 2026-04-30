#include<bits/stdc++.h>
#include"Timer.h"
using namespace std;
using namespace std::chrono;

template<typename T>
T fun(T inp){       /*If you change function then change line-32 also as requirement*/
 //type your code here
 return inp*2;
}

int main(){
    string str;
    ifstream file("input.txt");
    if(!file.is_open()){ 
        ofstream err("run.txt");
        string error = "input file isn't opened: \n";
        err<<error;
        err.close();
        return -1;
    }
    // FIXED: Use getline properly instead of eof() - eof() is unreliable
    while(getline(file,str)){ 
        // Now str contains each line - processes the last one
    }
    file.close();
    Timer T;
    T.start();
    stringstream ss(str);
    int test;
    char ch;
    ofstream ru("run.txt");
    while(ss>>test){
        ru<<to_string(fun(test))<<" "; /*If you change something in function then change here also*/
        ss>>ch;
    }
    ru.close();
    T.stop();
    cout<<T.duration()<<" microsecond:\n";
}