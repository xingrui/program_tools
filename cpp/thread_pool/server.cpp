#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>
#include <boost/thread.hpp>
#include <boost/bind.hpp>
using namespace boost;
using namespace std;

const char ch = 'C';
int package_size = 1024 * 1024;


size_t read_n(int fd, void* void_buffer, size_t size)
{
    printf("%d\n", 1000);
    char* buffer = (char*)void_buffer;
    size_t read_num = 0;

    do {
        size_t new_read_num = read(fd, buffer + read_num, size - read_num);

        if (new_read_num <= 0)
            return read_num;

        read_num += new_read_num;
    } while (read_num < size);

    return read_num;
}
void runChild(const int n, const int a)
{
}

void process(const int client_sockfd)
{
    /*  If we're the child, we can now read/write to the client on client_sockfd.
	The five second delay is just for this demonstration.  */
    char *buffer = new char[package_size];

    int read_ret = read_n(client_sockfd, buffer, package_size);
    // fprintf(stdout, "read_ret : %s\n", buffer);
    sleep(5);
    int write_ret = write(client_sockfd, &ch, 1);
    close(client_sockfd);
    fprintf(stderr, "pthread_id%d: read_ret : %d\n write_ret:%d\n", pthread_self(), read_ret, write_ret);
}

int main(int argc, char** argv)
{
    if (argc >= 2) {
        char* endPtr = NULL;
        package_size = strtol(argv[1], &endPtr, 10);

        if (endPtr != NULL && *endPtr == '\0') {
            // VALID
        } else {
            fprintf(stderr, "%s", "argv[1] is not valid number.");
            return -1;
        }
    }

    printf("package_size:%d\n", package_size);
    thread_group threads;
    threads.create_thread(boost::bind(&runChild, 0));

    int server_sockfd, client_sockfd;
    int server_len;
    socklen_t client_len;
    struct sockaddr_in server_address;
    struct sockaddr_in client_address;

    server_sockfd = socket(AF_INET, SOCK_STREAM, 0);

    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = htonl(INADDR_ANY);
    server_address.sin_port = htons(9734);
    server_len = sizeof(server_address);
    bind(server_sockfd, (struct sockaddr*)&server_address, server_len);

    /*  Create a connection queue, ignore child exit details and wait for clients.  */

    listen(server_sockfd, 5);

    signal(SIGCHLD, SIG_IGN);

    while (1) {

        /*  Accept connection.  */

        client_len = sizeof(client_address);
        client_sockfd = accept(server_sockfd,
                               (struct sockaddr*)&client_address, &client_len);
        // boost::bind(&process, 0);
        // boost::bind(&runChild, 0);
        // threads.create_thread(boost::bind(&process, client_sockfd));
    }
    threads.join_all();
}

