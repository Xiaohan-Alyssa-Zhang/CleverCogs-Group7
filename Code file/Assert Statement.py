#!/usr/bin/env python
# coding: utf-8

# In[ ]:


assert not ccdate['ExternalID'].isnull().all(), "As invalid data, the null value should not exist in the 'ExternalID' column"
assert not ccdate['Time'].isnull().all(), "As invalid data, the null value should not exist in the 'Time' column"
assert not user['ExternalID'].isnull().all(), "As invalid data, the null value should not exist in the 'ExternalID' column"
assert not user['Gender'].isnull().all(), "As invalid data, the null value should not exist in the 'Gender' column"
assert not medical['ExternalID'].isnull().all(), "As invalid data, the null value should not exist in the 'ExternalID' column"
assert not medical['Age'].isnull().all(), "As invalid data, the null value should not exist in the 'Age' column"

assert ccdate['ExternalID'].min()>0, "The ExternalID should be recorded as a positive number, not a negative number"
assert medical['Age'].min()>0, "The Age should be recorded as a positive number, not a negative number"

assert user['Gender'].isin(['M', 'F','U']).all(), "Only 'Male(M)',Female(F)' and'Unspecified(U)' exist in the 'Gender' column as uniformly formatted data"
assert medical['Gender'].isin(['M', 'F','U']).all(), "Only 'Male(M)',Female(F)' and'Unspecified(U)' exist in the 'Gender' column as uniformly formatted data"

