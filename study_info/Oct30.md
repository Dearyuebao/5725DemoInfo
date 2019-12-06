4.19.71…..19 series doesn't't work

4.14.91 kernel works well

blink.c:

wiring pi intro "hello world" of GPIO

blink_v3.c:

command line variable to change freuency

blink_v6.c:

should use!!! above use function from wiring pi delay function, it has bug in it

cause non linear shape. nano sleep



priority inversion:

round rolling, share time

level 0 : A 10 B 10 A 10 B 10…..

level 5: CD higher priority

assume: processA at priority 1 , processB at priority 5

between share variable

B is running acquire lock,  release lock, A cannot execute

priority 5, 3, 0

0 5 share variable

0 run and acquire lock-> 3 start to run->0 sleep, 3 run->5 start run-> 3 sleep 5 run

if 3 could block 5, priority inverse.

solution: priority inheritance:

preempt-RT:





