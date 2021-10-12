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

# In[2]:


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

# In[ ]:





# In[ ]:





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

# In[ ]:





# In[ ]:





# 8. <p>Copy the setup and exercise directions from <a href="https://gist.github.com/ryanorsinger/c4cf5a64ec33c014ff2e56951bc8a42d">More Numpy Practice</a> into your <code>numpy_exercises.py</code> and add your solutions.</p>

# In[ ]:





# In[ ]:





# <strong> Awesome Bonus </strong>
# For much more practice with numpy, Go to <code>https://github.com/rougier/numpy-100</code> and clone the repo down to your laptop. Next, go to <code>https://github.com/new</code> to make a new repo. Name it <code>numpy-100</code>, and follow the directions to "push an existing repository from the command line" so that you can push up your changes to your own account.</p>

# In[ ]:





# In[ ]:




