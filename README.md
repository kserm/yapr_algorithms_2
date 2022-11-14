# Basic data structures
links to tasks list at yandex.contest.ru:

[basic data structures](https://contest.yandex.ru/contest/23758/problems/)

[final tasks](https://contest.yandex.ru/contest/23759/problems/)

_________________________________________________

<details>
<summary>
Monitoring (<a href="1_monitoring.py">1_monitoring.py</a>) 
</summary>
There is an m × n matrix. You need to write a function that transposes it.
The transposed matrix is obtained from the original matrix by replacing rows with columns.

Input example:
|Input|Description|
|:-|:-|
|`4`|matrix rows number|
|`3`|matrix columns number|
|`1 2 3`|matrix row|
|`0 2 6`|matrix row|
|`7 4 1`|matrix row|
|`2 7 0`|matrix row|
|`1 0 7 2`|output|
|`2 2 4 7`|output|
|`3 6 1 0`|output|

</details>

_________________________________________________

<details>
<summary>
To-do list (<a href="2_todolist.py">2_todolist.py</a>) 
</summary>
You need to write a function that takes the head of the list as input and prints its elements.

Input example:

"test" function in 2_todolist.py file

</details>

_________________________________________________

<details>
<summary>
Unloved business (<a href="3_unlovedbussiness.py">3_unlovedbussiness.py</a>) 
</summary>
The to-do list is presented as a singly linked list. Write a solution function that takes as input the head of the list and the number of the case to be deleted and returns the head of the updated list.

Input example:

"test" function in 3_unlovedbussiness.py file

</details>

_________________________________________________

<details>
<summary>
Caring mother (<a href="4_carring_mother.py">4_carring_mother.py</a>) 
</summary>
Write a solution function that determines the index of the first occurrence of the value passed to it as input in the linked list, if the value is present.

Input example:

"test" function in 4_carring_mother.py file

</details>

_________________________________________________

<details>
<summary>
Other way around (<a href="5_other_way_around.py">5_other_way_around.py</a>) 
</summary>
Write a function that returns a list in reverse order.

Input example:

"test" function in 5_other_way_around.py file

</details>

_________________________________________________

<details>
<summary>
Stack Max (<a href="6_stek_max.py">6_stek_max.py</a>) 
</summary>
You need to implement a StackMax class that supports the operation of determining the maximum among all elements in the stack. The class must support the operations push(x), where x is an integer, pop() and get_max().

Input example:
|Input|Description|
|:-|:-|
|```8 get_max push 7 pop push -2 push -1 pop get_max get_max```|input|
|```None -2 -2```|output|

</details>

_________________________________________________

<details>
<summary>
Stack MaxEffective (<a href="7_stek_max_effective.py">7_stek_max_effective.py</a>) 
</summary>
Implement a StackMaxEffective class that supports the operation of determining the maximum among the elements on the stack. The complexity of the operation should be O(1). For an empty stack, the operation must return None. However, push(x) and pop() must also run in constant time.

Input example:
|Input|Description|
|:-|:-|
|```10 pop pop push 4 push -5 push 7 pop pop get_max pop get_max```|input|
|```error error 4 None```|output|

</details>

_________________________________________________

<details>
<summary>
Bracket sequence (<a href="8_bracket_sequence.py">8_bracket_sequence.py</a>) 
</summary>
Given a bracket sequence. We need to determine if it is correct.

* the empty string is a valid bracket sequence;
* a regular bracket sequence taken in brackets of the same type is a regular bracket sequence;
* a correct bracket sequence with a correct bracket sequence attached to the left or right is also correct.

Input example:
|Input|Description|
|:-|:-|
|`{[()]}`|input|
|`True`|output|

</details>

_________________________________________________

<details>
<summary>
Limited queue (<a href="9_limited_queue.py">9_limited_queue.py</a>) 
</summary>
You need to write a MyQueueSized class that takes a max_size parameter, which means the maximum allowed number of elements in the queue.

Commands can be of the following types:

* push(x) - add the number x to the queue;
* pop() - remove a number from the queue and print;
* peek() - print the first number in the queue;
* size() - return the size of the queue;

If the allowed queue size is exceeded, "error" should be displayed. When calling the pop() or peek() operations on an empty queue, output "None".

Input example:
|Input|Description|
|:-|:-|
|`8 2 peek push 5 push 2 peek size size push 1 size`|input|
|`None 5 2 2 error 2`|output|

</details>

_________________________________________________

<details>
<summary>
List queue (<a href="10_list_queue.py">10_list_queue.py</a>) 
</summary>
A queue using a linked list. The queue must support the execution of three commands:

* get() - get the element at the head of the queue and remove it. If the queue is empty, print "error".
* put(x) - add the number x to the queue
* size() - display the current size of the queue

Input example:
|Input|Description|
|:-|:-|
|`10 put -34 put -23 get size get size get get put 80 size`|input|
|`-34 1 -23 0 error error 1`|output|

</details>

_________________________________________________

<details>
<summary>
Recursive Fibonacci Numbers (<a href="11_fibo_recursion.py">11_fibo_recursion.py</a>) 
</summary>
Fibonacci Numbers. The solution must be implemented recursively.

Input example:
|Input|Description|
|:-|:-|
|`3`|input|
|`3`|output|
|||
|`0`|input|
|`1`|output|

</details>

_________________________________________________

<details>
<summary>
Fibonacci modulo (<a href="12_abs_fibo.py">12_abs_fibo.py</a>) 
</summary>
Find the last k digits of Fn.

How to find k last digits:
To calculate the last k digits of some number x, it is enough to take the remainder of its division by the number 10^k. This operation is denoted as x mod 10^k.

Input example:
|Input|Description|
|:-|:-|
|`3 1`|input|
|`3`|output|
|||
|`10 1`|input|
|`9`|output|

</details>

_________________________________________________
_________________________________________________

## Final tasks

<details>
<summary>
Deque (<a href="final_tasks_3/deck.py">deck.py</a>) 
</summary>
Write an efficient implementation of the deque data structure.
Attention: when implementing, use a ring buffer.

Input Format

The first line contains the number of commands n — an integer not exceeding 100000. The second line contains the number m — the maximum deque size. It does not exceed 50000. The next n lines contain one of the commands:

* push_back(value) - add an element to the end of the deque. If the deque already contains the maximum number of elements, print "error".
* push_front(value) - add an element to the front of the deque. If the deque already contains the maximum number of elements, print "error".
* pop_front() - Display the first element of the deque and remove it. If deque was empty, print "error".
* pop_back() - print the last element of the deque and remove it. If deque was empty, print "error".

Value is an integer, modulo not exceeding 1000.

Input example:
|Input|Description|
|:-|:-|
|`4 4 push_front 861 push_front -819 pop_back pop_back`|input|
|`861 -819`|output|

</details>

_________________________________________________

<details>
<summary>
Calculator (<a href="final_tasks_3/calculator.py">calculator.py</a>) 
</summary>
Write a calculator with reverse Polish notation.

To calculate the value of an expression written in reverse Polish notation, you need to read the expression from left to right and follow these steps:

1. Input character processing:
   * If an operand is given as input, it is pushed onto the top of the stack.
   * If an operation sign is given to the input, then this operation is performed on the required number of values ​​taken from the stack in the order of addition. The result of the performed operation is placed on the top of the stack.
2. If the input character set is not fully processed, go to step 1.
3. After the input character set has been completely processed, the result of the expression evaluation is at the top of the stack. If there are several numbers left on the stack, then only the top element should be displayed.

Input example:
|Input|Description|
|:-|:-|
|`2 1 + 3 *`|input|
|`9`|output|
|||
|`7 2 + 4 * 2 +`|input|
|`38`|output|

</details>