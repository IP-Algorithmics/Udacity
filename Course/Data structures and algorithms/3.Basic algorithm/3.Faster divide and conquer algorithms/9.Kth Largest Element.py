#!/usr/bin/env python
# coding: utf-8

# ### Problem Statement
# Given an unsorted array `Arr` with `n` positive integers. Find the $k^{th}$ smallest element in the given array, using Divide & Conquer approach. 
# 
# **Input**: Unsorted array `Arr` and an integer `k` where $1 \leq k \leq n$ <br>
# **Output**: The $k^{th}$ smallest element of array `Arr`<br>
# 
# 
# **Example 1**<br>
# Arr = `[6, 80, 36, 8, 23, 7, 10, 12, 42, 99]`<br>
# k = `10`<br>
# Output = `99`<br>
# 
# **Example 2**<br>
# Arr = `[6, 80, 36, 8, 23, 7, 10, 12, 42, 99]`<br>
# k = `5`<br>
# Output = `12`<br>
# 
# ---
# 
# ### The Pseudocode - `fastSelect(Arr, k)`
# 1. Break `Arr` into $\frac{n}{5}$ (actually it is $\left \lceil{\frac{n}{5}} \right \rceil $) groups, namely $G_1, G_2, G_3...G_{\frac{n}{5}}$
# 
# 
# 2. For each group $G_i, \forall 1 \leq i \leq \frac{n}{5} $, do the following:
#  - Sort the group $G_i$
#  - Find the middle position i.e., median $m_i$ of group $G_i$
#  - Add $m_i$ to the set of medians **$S$**
# 
# 
# 3. The set of medians **$S$** will become as $S = \{m_1, m_2, m_3...m_{\frac{n}{5}}\}$. The "good" `pivot` element will be the median of the set **$S$**. We can find it as $pivot = fastSelect(S, \frac{n}{10})$. 
# 
# 
# 4. Partition the original `Arr` into three sub-arrays - `Arr_Less_P`, `Arr_Equal_P`, and `Arr_More_P` having elements less than `pivot`, equal to `pivot`, and bigger than `pivot` **respectively**.
# 
# 
# 5. Recurse based on the **sizes of the three sub-arrays**, we will either recursively search in the small set, or the big set, as defined in the following conditions:
#  - If `k <= length(Arr_Less_P)`, then return `fastSelect(Arr_Less_P, k)`. This means that if the size of the "small" sub-array is at least as large as `k`, then we know that our desired $k^{th}$ smallest element lies in this sub-array. Therefore recursively call the same function on the "small" sub-array. <br><br>
#  
#  - If `k > (length(Arr_Less_P) + length(Arr_Equal_P))`, then return `fastSelect(Arr_More_P, (k - length(Arr_Less_P) - length(Arr_Equal_P)))`. This means that if `k` is more than the size of "small" and "equal" sub-arrays, then our desired $k^{th}$ smallest element lies in "bigger" sub-array. <br><br>
#  
#  - Return `pivot` otherwise. This means that if the above two cases do not hold true, then we know that $k^{th}$ smallest element lies in the "equal" sub-array.
#  
# ---
# ### Exercise - Write the function definition here

# In[ ]:


def fastSelect(Arr, k):
    '''TO DO'''
    # Implement the algorithm explained above to find the k^th lasrgest element in the given array
    pass


# <span class="graffiti-highlight graffiti-id_dsq4qxt-id_29dh0dm"><i></i><button>Hide Solution</button></span>

# In[ ]:


def fastSelect(Arr, k):                         # k is an index
    n = len(Arr)                                # length of the original array
    
    if(k>0 and k <= n):                         # k should be a valid index         
        # Helper variables
        setOfMedians = []
        Arr_Less_P = []
        Arr_Equal_P = []
        Arr_More_P = []
        i = 0
        
        # Step 1 - Break Arr into groups of size 5
        # Step 2 - For each group, sort and find median (middle). Add the median to setOfMedians
        while (i < n // 5):                     # n//5 gives the integer quotient of the division 
            median = findMedian(Arr, 5*i, 5)    # find median of each group of size 5
            setOfMedians.append(median)         
            i += 1

        # If n is not a multiple of 5, then a last group with size = n % 5 will be formed
        if (5*i < n): 
            median = findMedian(Arr, 5*i, n % 5)
            setOfMedians.append(median)
        
        # Step 3 - Find the median of setOfMedians
        if (len(setOfMedians) == 1):            # Base case for this task
            pivot = setOfMedians[0]
        elif (len(setOfMedians)>1):
            pivot = fastSelect(setOfMedians, (len(setOfMedians)//2))
        
        # Step 4 - Partition the original Arr into three sub-arrays
        for element in Arr:
            if (element<pivot):
                Arr_Less_P.append(element)
            elif (element>pivot):
                Arr_More_P.append(element)
            else:
                Arr_Equal_P.append(element)
        
        # Step 5 - Recurse based on the sizes of the three sub-arrays
        if (k <= len(Arr_Less_P)):
            return fastSelect(Arr_Less_P, k)
        
        elif (k > (len(Arr_Less_P) + len(Arr_Equal_P))):
            return fastSelect(Arr_More_P, (k - len(Arr_Less_P) - len(Arr_Equal_P)))
            
        else:
            return pivot     

# Helper function
def findMedian(Arr, start, size): 
    myList = [] 
    for i in range(start, start + size): 
        myList.append(Arr[i]) 
          
    # Sort the array  
    myList.sort() 
  
    # Return the middle element 
    return myList[size // 2] 


# ### Test - Let's test your function

# In[ ]:


Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42]
k = 5
print(fastSelect(Arr, k))        # Outputs 12


# In[ ]:


Arr = [5, 2, 20, 17, 11, 13, 8, 9, 11]
k = 5
print(fastSelect(Arr, k))        # Outputs 11


# In[ ]:


Arr = [6, 80, 36, 8, 23, 7, 10, 12, 42, 99]
k = 10
print(fastSelect(Arr, k))        # Outputs 99

