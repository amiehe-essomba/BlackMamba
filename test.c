#include <stdio.h>
#include <unistd.h>
#include <termios.h>

void enableRawMode(){
    struct termios row;
    tcgetattr(STDIN_FILENO, &raw)
    raw.v_lflag &= ~(ECHO)
    tcgetattr(STDIN_FILENO, TCSAFLUSH, &raw)
}

int main(){
    enableRawMode()
    char c;
    while(read(STDIN_FILENO, &c, 1) == 1 && c != 'q');
    return 0;
}