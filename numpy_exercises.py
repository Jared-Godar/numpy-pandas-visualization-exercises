#!/usr/bin/env python
# coding: utf-8

# <h2 id="exercises">Exercises</h2>
# <p>In your <code>numpy-pandas-visualization-exercises</code> repo, create a file named <code>numpy_exercises.py</code> for this exercise.</p>
# <p>Use the following code for the questions below:</p>
# <div class="highlight"><pre><span></span>a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
# </pre></div>
# 
# <ol>
# <li>
# <p>How many negative numbers are there?</p>
# </li>
# <li>
# <p>How many positive numbers are there?</p>
# </li>
# <li>
# <p>How many even positive numbers are there?</p>
# </li>
# <li>
# <p>If you were to add 3 to each data point, how many positive numbers would
#    there be?</p>
# </li>
# <li>
# <p>If you squared each number, what would the new mean and standard deviation
#    be?</p>
# </li>
# <li>
# <p>A common statistical operation on a dataset is <strong>centering</strong>. This means to
#    adjust the data such that the mean of the data is 0. This is done by
#    subtracting the mean from each data point. Center the data set. See <a href="https://www.theanalysisfactor.com/centering-and-standardizing-predictors/">this link</a> for more on centering.</p>
# </li>
# <li>
# <p>Calculate the z-score for each data point. Recall that the z-score is given
#    by:</p>
# <div>
# <div class="MathJax_Preview">
# Z = \frac{x - \mu}{\sigma}
# </div>
# <script type="math/tex; mode=display">
# Z = \frac{x - \mu}{\sigma}
# </script>
# </div>
# </li>
# <li>
# <p>Copy the setup and exercise directions from <a href="https://gist.github.com/ryanorsinger/c4cf5a64ec33c014ff2e56951bc8a42d">More Numpy Practice</a> into your <code>numpy_exercises.py</code> and add your solutions.</p>
# </li>
# </ol>
# <p><strong> Awesome Bonus </strong>
# For much more practice with numpy, Go to <code>https://github.com/rougier/numpy-100</code> and clone the repo down to your laptop. Next, go to <code>https://github.com/new</code> to make a new repo. Name it <code>numpy-100</code>, and follow the directions to "push an existing repository from the command line" so that you can push up your changes to your own account.</p>
#                 
#                   
#                 
#               

# In[1]:


import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# 1. How many negative numbers are there?
# 

# In[ ]:


1. How many negative numbers are there


# In[8]:


a[a<0]


# In[15]:


len(a[a<0])


# 2. How many positive numbers are there?

# In[10]:


a[a>0]


# In[16]:


len(a[a<0])


# 3. How many even positive numbers are there?

# In[11]:


a[(a > 0) & (a % 2 ==0)]


# In[17]:


len(a[(a > 0) & (a % 2 ==0)])


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[12]:


b=a+3
b[b>0]


# In[18]:


len(b[b>0])


# 5. If you squared each number, what would the new mean and standard deviation be?

# In[14]:


c = a **2
c.mean(), c.std()


# In[ ]:





# 6. A common statistical operation on a dataset is <strong>centering</strong>. This means to
#    adjust the data such that the mean of the data is 0. This is done by
#    subtracting the mean from each data point. Center the data set. See <a href="https://www.theanalysisfactor.com/centering-and-standardizing-predictors/">this link</a> for more on centering.

# In[3]:


np.mean(a)


# In[12]:


a -=3 
a


# In[13]:


a.mean()


# 7. Calculate the z-score for each data point. Recall that the z-score is given
#    by:</p>
# <div>
# <div class="MathJax_Preview">
# Z = \frac{x - \mu}{\sigma}
# </div>
# <script type="math/tex; mode=display">
# Z = \frac{x - \mu}{\sigma}
# </script>
# </div>
# </li>

# In[14]:


(a-a.mean())/a.std()


# In[ ]:





# 8. <p>Copy the setup and exercise directions from <a href="https://gist.github.com/ryanorsinger/c4cf5a64ec33c014ff2e56951bc8a42d">More Numpy Practice</a> into your <code>numpy_exercises.py</code> and add your solutions.</p>

# In[5]:


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
# 

# In[17]:


sum_of_a = np.sum(a)
sum_of_a


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
# 

# In[18]:


min_of_a = np.min(a)
min_of_a


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
# 

# In[19]:


max_of_a = np.max(a)
max_of_a


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
# 

# In[21]:


mean_of_a = np.mean(a)
mean_of_a


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

# In[29]:


product_of_a = np.product(a)
product_of_a


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
# 

# In[21]:


squares_of_a = a**2
squares_of_a


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
# 

# In[7]:


is_odd = a % 2 == 1
odds_in_a = a[is_odd]
odds_in_a


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

# In[9]:


is_even = a % 2 == 0
evens_in_a = a[is_even]
evens_in_a


# ---

# What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
# Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
# 
# b = [ [3, 4, 5], [6, 7, 8] ]

# In[10]:


b = np.matrix([ [3, 4, 5], [6, 7, 8] ])


# In[11]:


b


# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. Hint, you'll first need to make sure that the "b" variable is a numpy array
# 
#       sum_of_b = 0
#           for row in b:
#       sum_of_b += sum(row)

# In[14]:


sum_of_b=np.sum(b)
sum_of_b


# - Exercise 2 - refactor the following to use numpy. 
# 
#         min_of_b = min(b[0]) 
#             if min(b[0]) <= min(b[1]) 
#         else min(b[1])  

# In[15]:


min_of_b = np.min(b)
min_of_b


# - Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
#         max_of_b = max(b[0]) 
#             if max(b[0]) >= max(b[1]) 
#             else max(b[1])

# In[17]:


max_of_b = np.max(b)
max_of_b


# - Exercise 4 - refactor the following using numpy to find the mean of b
#     mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

# In[18]:


mean_of_b = np.mean(b)
mean_of_b


# - Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# 
#       product_of_b = 1
#       for row in b:
#           for number in row:
#               product_of_b *= number

# In[19]:


product_of_b = np.product(b)
product_of_b


# - Exercise 6 - refactor the following to use numpy to find the list of squares
# 
#          squares_of_b = []
#          for row in b:
#              for number in row:
#                  squares_of_b.append(number**2)

# In[23]:


squares_of_b = np.square(b)
squares_of_b


# - Exercise 7 - refactor using numpy to determine the odds_in_b
#           odds_in_b = []
#           for row in b:
#               for number in row:
#                   if(number % 2 != 0):
#                       odds_in_b.append(number)

# In[25]:


is_odd = b % 2 == 1
odds_in_b = b[is_odd]
odds_in_b


# - Exercise 8 - refactor the following to use numpy to filter only the even numbers
# 
#          evens_in_b = []
#          for row in b:
#              for number in row:
#                  if(number % 2 == 0):
#                      evens_in_b.append(number)

# In[26]:


is_even = b % 2 == 0
evens_in_b = b[is_even]
evens_in_b


# - Exercise 9 - print out the shape of the array b.

# In[27]:


np.shape(b)


# - Exercise 10 - transpose the array b.

# In[28]:


np.transpose(b)


# - Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

# In[29]:


get_ipython().run_line_magic('pinfo', 'np.reshape')


# In[30]:


np.reshape(b,(1,6))


# - Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

# In[31]:


np.reshape(b,(6,1))


# ---

# ### Setup 3
#     c = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
# 
# ### HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.

# In[32]:


c = np.matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# - Exercise 1 - Find the min, max, sum, and product of c.

# In[33]:


np.min(c)


# In[34]:


np.max(c)


# In[35]:


np.sum(c)


# In[36]:


np.product(c)


# - Exercise 2 - Determine the standard deviation of c.

# In[37]:


np.std(c)


# - Exercise 3 - Determine the variance of c.

# In[38]:


np.var(c)


# - Exercise 4 - Print out the shape of the array c

# In[40]:


np.shape(c)


# - Exercise 5 - Transpose c and print out transposed result.

# In[41]:


np.transpose(c)


# - Exercise 6 - Get the dot product of the array c with c.

# In[42]:


get_ipython().run_line_magic('pinfo', 'np.dot')


# In[44]:


np.dot(c,c)


# - Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# In[52]:


np.sum(np.multiply(c, np.transpose(c)))


# - Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

# In[56]:


np.product(np.multiply(c, np.transpose(c)))


# ---

# ### Setup 4
#         d = [
#             [90, 30, 45, 0, 120, 180],
#             [45, -90, -30, 270, 90, 0],
#             [60, 45, -45, 90, -45, 180]
#         ]

# In[57]:


d = np.matrix([
        [90, 30, 45, 0, 120, 180],
        [45, -90, -30, 270, 90, 0],
        [60, 45, -45, 90, -45, 180]
    ])


# - Exercise 1 - Find the sine of all the numbers in d

# In[59]:


np.sin(d)


# - Exercise 2 - Find the cosine of all the numbers in d

# In[61]:


np.cos(d)


# - Exercise 3 - Find the tangent of all the numbers in d

# In[62]:


np.tan(d)


# - Exercise 4 - Find all the negative numbers in d

# In[63]:


d[d<0]


# - Exercise 5 - Find all the positive numbers in d
# 

# In[64]:


d[d>0]


# - Exercise 6 - Return an array of only the unique numbers in d.

# In[65]:


np.unique(d)


# - Exercise 7 - Determine how many unique numbers there are in d.

# In[68]:


np.shape(np.unique(d))


# - Exercise 8 - Print out the shape of d.

# In[70]:


np.shape(d)


# - Exercise 9 - Transpose and then print out the shape of d.

# In[71]:


np.shape(np.transpose(d))


# - Exercise 10 - Reshape d into an array of 9 x 2

# In[72]:


np.reshape(d, (9,2))


# <strong> Awesome Bonus </strong>
# For much more practice with numpy, Go to <code>https://github.com/rougier/numpy-100</code> and clone the repo down to your laptop. Next, go to <code>https://github.com/new</code> to make a new repo. Name it <code>numpy-100</code>, and follow the directions to "push an existing repository from the command line" so that you can push up your changes to your own account.</p>

# In[ ]:





# In[ ]:




