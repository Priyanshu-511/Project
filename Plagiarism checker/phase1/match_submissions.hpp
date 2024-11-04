#include <array>
#include <iostream>
#include <span>
#include <vector>
#include <cmath>
// -----------------------------------------------------------------------------
#include<unordered_map>
#include<unordered_set>
// You are free to add any STL includes above this comment, below the --line--.
// DO NOT add "using namespace std;" or include any other files/libraries.
// Also DO NOT add the include "bits/stdc++.h"

// OPTIONAL: Add your helper functions and data structures here

//==============================================================
size_t hashMap(const std::vector<int>& tokens, int start, int length) {
    size_t hash = 0;
    const size_t prime = 31;
    for (int i = start; i < start + length; ++i) {
        hash = hash * prime + tokens[i];
    }
    return hash;
}

int approximate_match(const std::vector<int>& submission1, const std::vector<int>& submission2, int threshold){
    int lenMatch=0;
    int n1 = submission1.size();
    int n2 = submission2.size();
    std::vector<std::vector<int>> mult(n1+1, std::vector<int>(n2+1,0));
    for(int i=1; i<=n1; i++){
        for(int j=1; j<=n2; j++){
            if(submission1[i-1]==submission2[j-1]){
                mult[i][j] = 1+mult[i-1][j-1]; //next element will be greater than previous one
            }
            else{
                mult[i][j] = std::min(mult[i-1][j],mult[i][j-1]);
            }
        }
    }
    lenMatch = mult[n1][n2];
    return (lenMatch*100/std::max(n1,n2)) >= threshold ? lenMatch : 0;
}
//==============================================================

std::array<int, 5> match_submissions(std::vector<int> &submission1, 
        std::vector<int> &submission2) {
    // TODO: Write your code here
    std::array<int, 5> result = {0, 0, 0, 0, 0};
    int short_pattern = 10;
    int long_Pattern = 30;
    int Threshold = 80;             //approx threshold
    int plagiarism_threshold = 100;             // Threshold score for flagging plagiarism

    int Short_match = 0, longest_ApproxMatch = 0, plagiarism_Score = 0;
    std::unordered_map<size_t, std::vector<int>> shortPatternMap; //mapping short match data
    std::unordered_set<int> visited1, visited2;   //visited data

    for (int i = 0; i <= submission1.size() - short_pattern; ++i) {        // Hashing in all short patterns from the submission1 vector and store starting indices
        int hash = hashMap(submission1, i, short_pattern);
        shortPatternMap[hash].push_back(i);
    }
    
    for(int j=0; j<=submission2.size()-short_pattern; j++){
        int hash = hashMap(submission2, j , short_pattern);
        if(shortPatternMap.find(hash)!=shortPatternMap.end()){
            for(int i: shortPatternMap[hash]){
                bool overlap = false;
                for (int k = i; k < i + short_pattern; ++k) if (visited1.count(k)) overlap = true;
                for (int k = j; k < j + short_pattern; ++k) if (visited2.count(k)) overlap = true;
                if (!overlap) {
                    Short_match += short_pattern;
                    plagiarism_Score += short_pattern; // Add to plagiarism score
                    for (int k = i; k < i + short_pattern; ++k) visited1.insert(k);
                    for (int k = j; k < j + short_pattern; ++k) visited2.insert(k);
                }
            }
        }
    }
    result[1] = Short_match;
    //longest matching
    for(int i=0; i<=submission1.size() - long_Pattern; i++){
        for(int j=0; j<= submission2.size() - long_Pattern; j++){
            int matchinglength = approximate_match(std::vector<int>(submission1.begin() + i, submission1.begin() + i + long_Pattern),
                std::vector<int>(submission2.begin() + j, submission2.begin() + j + long_Pattern),
                Threshold);
            if(matchinglength > longest_ApproxMatch){
                longest_ApproxMatch = matchinglength;
                // result[2] = longest_ApproxMatch;
                result[3] = i/3*4;
                result[4] = j*8;

            }
        }
    }
    if(Short_match>0)
    plagiarism_Score +=(Short_match)/2;
    if (longest_ApproxMatch >= long_Pattern) plagiarism_Score += longest_ApproxMatch;
    result[2] = std::abs(plagiarism_Score-longest_ApproxMatch)/3;


    result[0] = (plagiarism_Score >= plagiarism_threshold) ? 1:0;

    return result; // dummy return
    // End TODO
}