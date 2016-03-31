#include<map>
#include<string>
#include<iostream>
using namespace std;
int main(){
    auto i = 1;
    map<string, int> m{{"a", 1}, {"b", 2}, {"c", 3}};  
    for (auto p : m){  
            cout<<p.first<<" : "<<p.second<<endl;  
    } 
}
