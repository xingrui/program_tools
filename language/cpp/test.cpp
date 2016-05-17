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
    A a(1,2);
    std::cout << a.a << a.b << std::endl;
}
