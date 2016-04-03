/***************************************************************************
 *
 * Copyright (c) 2015 Baidu.com, Inc. All Rights Reserved
 * $Id$
 *
 **************************************************************************/



/**
 * @file RankerFactory.h
 * @author magneto(magneto@mobvista.com)
 * @date 2015/06/25 13:07:43
 * @version $Revision$
 * @brief
 *
 **/
#ifndef __MOBVISTA_RANKERFACTORY_H_
#define __MOBVISTA_RANKERFACTORY_H_

#include <string>
#include <map>

namespace ranker {

class IRanker {
};

struct InfoForSelect;

typedef IRanker* (RankerCreator)();

template <typename T>
IRanker* createRanker()
{
    return new T;
}

class RankerFactory {

public:
    RankerFactory() {
    }
    ~RankerFactory() {}
    ranker::IRanker* makeRanker(const std::string& rankerName) const {
        std::map<std::string, RankerCreator*>::const_iterator it;
        it = m_nameCreaterMap.find(rankerName);

        if (it == m_nameCreaterMap.end()) {
            return NULL;
        }

        return it->second();
    }

    int init_ranker_factory();
    std::map<std::string, RankerCreator*> m_nameCreaterMap;
};
#define BEGIN_ADD_RANKER_TYPE \
    int ::ranker::RankerFactory::init_ranker_factory()\
    {

#define ADD_RANKER_TYPE(TYPE)\
    m_nameCreaterMap[#TYPE] = createRanker<TYPE>;\

#define END_ADD_RANKER_TYPE \
    return 0;\
    }
}
#endif
/* vim: set ts=4 sw=4 sts=4 tw=100 */
