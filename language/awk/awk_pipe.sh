awk '{print $0|"grep 12"}' << EOF
1234
123
12
1
4321
432
43
4
21212
EOF

awk 'BEGIN{ "date" | getline d; print d}' << EOF
EOF
#可以在awk中打开一个管道，且同一时刻只能有一个管道存在。通过close()可关闭管道。如：$ awk '{print $1, $2 | "sort" }' test END {close("sort")}。awk把print语句的输出通过管道作为linux命令sort的输入,END块执行关闭管道操作。
awk '{print $1 | "xargs echo";print $1}' << EOF
121231233
121231233
121231233
121231233
121231233
121231233
121231233
121231233
121231233
121231233
121231233
EOF
exit 0
awk '{print $1;}' << EOF
EOF
awk '
{
    print $1 | "base64 -w 0"
}
'<< EOF
112312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312312323123123
EOF
