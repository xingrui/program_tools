#include<map>
#include<string>
#include<iostream>
using namespace std;
class A{
public:
    int a;
    int b;
    A(int t_a,int t_b):a(t_a), b(t_b) {}
    A(int t_b):A(0, t_b) {}
};
int main(){
    auto i = 1;
    map<string, int> m{{"a", 1}, {"b", 2}, {"c", 3}};  
    for (auto p : m){  
            cout<<p.first<<" : "<<p.second<<endl;  
    } 
}
