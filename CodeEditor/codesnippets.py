'''
 Test Snippets
'''

C_CODE = '''
#include <stdio.h>
int main(){
    printf("hello world\n");
    return 0;
}
'''

CPP_CODE = '''
#include <iostream>
using namespace std;

int main(){
    cout << "Hello world" << endl;
    return 0;
}
'''

JAVA_CODE = '''
import java.io.*;

class Test{
    public static void main(String args[]){
        System.out.println("Hello world");
    }
}
'''


PYTHON_CODE = '''
print "Hello world"
'''




CODE_SNIPPETS = {
    'C' : C_CODE,
    'C++' : CPP_CODE,
    'JAVA' : JAVA_CODE,
    'PYTHON' : PYTHON_CODE
}