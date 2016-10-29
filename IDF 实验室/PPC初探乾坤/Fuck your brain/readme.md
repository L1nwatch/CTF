## 题目

```ini
++++++++++++[>++++>+++++>++++++>+++++++>++++++++>+++++++++>++++++++++<<<<<<<-]>>>>+++.<-----.>---.<+++.>>>>+++.<<<<----.>>>++++++.<<<<<+++.--.>>>>>----.<<<++++.<<+++.>>>>+++.>---.>++.
```

## write up

Brain Fuck编程语言，利用C语言编译器即可，源码看main.cpp（由 http://blog.csdn.net/key1213/article/details/19247215 得）：

```c++
#include <stdio.h>  
int  p, r, q;  
char a[5000], f[5000], b, o, *s=f;  
void interpret(char *c)  
{  
    char *d;  
    r++;  
    while( *c ) {  
   
        switch(o=1,*c++) {  
            case '<': p--;        break;  
     case '>': p++;        break;  
            case '+': a[p]++;     break;  
            case '-': a[p]--;     break;  
            case '.': putchar(a[p]); fflush(stdout); break;  
            case ',': a[p]=getchar();fflush(stdout); break;  
            case '[':  
                for( b=1,d=c; b && *c; c++ )  
                b+=*c=='[', b-=*c==']';  
                if(!b) {  
                    c[-1]=0;  
                    while( a[p] )  
                    interpret(d);  
                    c[-1]=']';  
                    break;  
                }  
            case ']':  
                puts("UNBALANCED BRACKETS"), exit(0);  
            case '#':  
  if(q>2)  
                printf("- - - - - - - - - -/n%*s/n",*a,a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],3*p+2,"^");  
                break;  
            default: o=0;  
        }  
 if( p<0 || p>100)  
            puts("RANGE ERROR"), exit(0);  
    }  
    r--;  
     
}  
int main(int argc,char *argv[])  
{  
    FILE *z;  
    q=argc;  
    if(z=fopen(argv[1],"r")) {  
 while( (b=getc(z)) > 0 )  
            *s++=b;  
        *s=0;  
        interpret(f);  
    }  
return 0;  
}  
```

使用方法，编译完成后，输入一个文件，文件内容即题目给的那一堆。