#include "RankerFactory.h"
#include <iostream>

namespace ranker {
class ARanker : public IRanker {
public:
    ARanker() {std::cout << __FUNCTION__ << std::endl;}
};
class BRanker : public IRanker {
public:
    BRanker() {std::cout << __FUNCTION__ << std::endl;}
};
}

BEGIN_ADD_RANKER_TYPE
ADD_RANKER_TYPE(ARanker)
ADD_RANKER_TYPE(BRanker)
END_ADD_RANKER_TYPE

int main()
{
    using namespace ranker;
    RankerFactory factory;
    int res = factory.init_ranker_factory();
    factory.makeRanker("ARanker");
    factory.makeRanker("BRanker");
    factory.makeRanker("CRanker");
    return 0;
}
