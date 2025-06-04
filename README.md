This is a simple set of scripts to test if a problem is separable in univariate functions.
For a given problem (combinatorial or continuous), it tells you how independently optimisable each variable is (0 = independent, 1 = beheviour has changed every time it was looked at)
My motivation behind this is that I am skeptical of variable importance, since I believe that in many problems it is somewhat deceptive or irrelevant.

Therefore, I came up with this relatively simple approach of measuring how "marginal" a problem is on each variable.
**A variable is marginal if it can be optimised independently of the solution**.


To test this, consider a combinatorial problem where variable v_i has possible values A, B, C and D.
In a solution s_1, I can change the value of v_i and measure the resulting fitness, which is called the Ceteris Paribus (taken from (here)[https://christophm.github.io/interpretable-ml-book/ceteris-paribus.html, a very good website!!]).
Let's say that the fitnesses when setting v_i to the different values in s_1 are A->4, B->1, C-> 10, D->3. Therefore, when optimising you should use C.

Now let's consider the solution s_2, where I do the same process and I get A->100, B->2, C-> 4, D->5. Now, A is clearly the best option.
What this means is that the **effect of the value of v_i appears to be dependent on something else within the solution**, and if a variable importance was attributed to this variable it would make it deceptive. 
In the case of a continuos problem (v_i is a float), instead of a table of values we get a function that for each value of v_i assigns a fitness (a true CP plot!).
If v_i is independently optimisable, then this plot should behave "similarly" everywhere (grows and decreases in the same places, but let's be careful!)


Now, I am not checking if the problem is linear or anything similar, because that would be an assumption that the objective is additively separable.
In theory x + y + z is as separable as x * y * z, but linearity testing won't tell you that! I also don't use a ML model, because I don't want to introduce more indirection)
In theory, my method works on linear things as well as discontinuous functions etc...


Now, consider the function f(x, y, x) = x + y + z.
* In (1, y, 3), the Ceteris paribus plot is 1 + y + 3, and will look like a straight line that grows as y grows.
* In (0.2, y, 0.8), the plot will be 0.2 + y + 0.8, another straight line that grows as y grows.
  
Therefore, here y can be optimised independently! (because the effect of y is consistent)


Now consider the function f(x, y, z) = x * y * z. (and their domains are between 0 and 5, **always positive**!!!)
* In (1, y, 3), the Ceteris paribus plot is 4 * y , and it is increasing as y increases
* In (0.2, y, 0.8), the plot will be 0.16 * y, and it is increasing as y increases (although they are lines with different angles).
  
Therefore, here y can be optimised independently! (because the effect of y is consistent, in some way)


Now consider the function f(x, y, z) = x * y * z (but their domains are -5, 5... this is the only difference).
* In (1, y, 3), same as above
* In (0.2, y, 0.8), same as above
- (all good so far)
* In (-1, y, 1), the plot will be -1 * y, and it is **decreasing** as y increases.
  
Therefore, the behaviour of y depends on something else (in this case, the sign of x * z).





