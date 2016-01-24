/***************************************************************************
 * 
 * Copyright (c) 2015 Mobvista.com, Inc. All Rights Reserved
 * $Id$ 
 * 
 **************************************************************************/
 
 
 
/**
 * @file thread_pool.cpp
 * @author jackson(jackson@mobvista.com)
 * @date 2015/07/22 09:55:13
 * @version $Revision$ 
 * @brief 
 *  
 **/

#include <iostream>
#include <boost/thread.hpp>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <boost/thread.hpp>

using namespace boost;
using namespace std;
void runChild(const int n)
{
    cout << "我是第" << n << "个子线程" << endl;
    sleep(1);
    cout << "进程" << n <<  "退出" << endl;
}
int main(int argc, char** argv)
{
    int num;
    thread_group threads;
    if (argc < 2)
    {
        cout << "请提供一个要生成线程数的参数" << endl;
        exit(-1);
    }
    num = atoi(argv[1]);
    cout << "我是主程序,我准备产生" << num << "个子线程" << endl;
    for(int i = 0; i < num; i++)
    {
        threads.create_thread(bind(&runChild, i));
    }
    cout << "我是主程序，我在等子线程运行结束" << endl;
    threads.join_all();
    return 0;
}



/* vim: set ts=4 sw=4 sts=4 tw=100 noet: */
