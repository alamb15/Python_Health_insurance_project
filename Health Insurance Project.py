#!/usr/bin/env python
# coding: utf-8

# In[1]:


#To start, lets important our insurance CSV file,and print it out to just take an overview of the data.
import csv


# In[2]:


with open("insurance copy.csv") as insurance_project:
    insurance_var = insurance_project.read()
    print(insurance_var)
    


# In[ ]:





# In[ ]:





# In[1]:


#First, to make this easier for me to manipulate, I'm going to convert this CSV data 
#to a list of (key:value) pairs that I can easily iterate through.


with open("insurance copy.csv") as insurance_data:
    insurance_costs = csv.DictReader(insurance_data)
    updated_ins_list = list((insurance_costs))
print(updated_ins_list)
    
    
#Let's see how many people are apart of our data set.


length_of_data = len(updated_ins_list)
print("There are " + str(length_of_data) + " people in this data set!")



#1,338 people, now i'm curious how much all of those charges add up to.
#lets first see if we can grab the charge of the very last person in our dataset
#and see what they paid


print(updated_ins_list[-1]['charges'])



#by using list_name[index][key] syntax, I can select an index in the list, and within
#that index I can then grab the key I want, in this case the "charges" key.

#Now lets make a list of all of those charges.



list_of_charges = []
length = len(updated_ins_list)
index = 0
while index < length:
    list_of_charges.append(updated_ins_list[index]['charges'])
    index +=1
print(list_of_charges)



#so first we create a empty list of charges were going to populate once we
#get our charge values, next we create two variables, one that is the length of our entire
#list and another that is the index starting at 0. Then, while our index value is lower than
#the length of our list, we want to take each index and we want to take the 'charges' key from those indexes
#and append that value to our list.


#Now that I have a list of charges, I wanna convert them all from strings to real values to add them up...
#I have to remember that these are float() values though, not int()


for i in range(len(list_of_charges)):
    list_of_charges[i] = float(list_of_charges[i])
print(list_of_charges)


#The rest should be easy! now lets add up all of our float values and then round it to the
#nearest tenth


sum_of_charges = sum(list_of_charges)
print(sum_of_charges)
    
Total_rounded_charges = round(sum_of_charges,2)
print(Total_rounded_charges)


#There's over 17 million dollars in total charges for all of these people combined. With this,
#we could choose to perform more complex aggregations and perform statistical analyses with this information.

#lets put some of these findings into a simple print statement:


print("In this Insurance dataset there is " + str(length_of_data) + " total people, and combined have been charged $" + str(Total_rounded_charges) + " dollars!")
    
    
#Could we calculate the average charge for each person?
#we need to take the sum of our charges and divide it by the number of charges in our dataset
#Now that we know both, this should be pretty easy.


Average_charge_per_person = Total_rounded_charges / length_of_data
print("The average charge per person in this dataset is $" + str(Average_charge_per_person) + " dollars.")


#We could still clean this statement up and round it to the nearest tenth, lets do that
#and then re-print our statement with the updated average charge.



rounded_average_charge = round(Average_charge_per_person,2)
print("The average charge per person in this dataset is $" + str(rounded_average_charge) + " dollars.")



#Now, out of our orginal list we created from our CSV file, lets see whos insurance was the cheapest and the highest.
#Then, lets look further into that persons information and see what conclusions we could draw about what
#factors are leading to those costs; bmi? age? smoker status?


max_charge = max(list_of_charges)
print(max_charge)


#$63,770 is the max charge. Now that we know out of all 1,338 people who has the highest charge, it would be  
#useful to look at this persons other information provided in our data set so later on we can compare against
#the person with the smallest charge in our data set...


def search(max_charge,our_ins_list):
    return [other_info for other_info in our_ins_list if other_info['charges'] == max_charge]

our_max_guy = search('63770.42801',updated_ins_list)
print(our_max_guy)



#above, we create a function that takes two parameters: max_charge, and our_ins_list.
#our function performs a list comprehension, and says: perform the expression of giving us the other info, 
#for the other info inside of our list if the other info's 'charges' key is equal to the value.
#we then call our function and pass the actual string max charge amount and we pass our 
#original updated insurance list to use as arguments for our parameters and
#as the function states, it returned that other info because it found which dictionary
#in our string matched the key 'charges' with our max_charge value of '63770.42801'

#Now lets repeat this process for finding the minimum charge, and next, i'll take a look at their other
#information provided to compare against our max value, and let's see what makes them so different...


min_charge = min(list_of_charges)
print(min_charge)


#Only, $1,121. Over $60,000 less than our_max_guy, now lets find the rest of their information...


def search_2(min_charge,ins_list):
    return [rest_of_dic for rest_of_dic in ins_list if rest_of_dic['charges'] == min_charge]

our_min_guy = search_2('1121.8739',updated_ins_list)
print(our_min_guy)


#Now that we have found both dictionaries for the highest charged person and the lowest, lets
#zip them together into a list to compare side by side


zipped_max_min = list(zip(our_max_guy,our_min_guy))
print(zipped_max_min)



#although both of these people are apart of the same region, and both have 0 kids, our higher charged
#person is a much older smoker who has a higher bmi, while our lowest charges peron is very young,
#does not smoke, and has a lower bmi.

#Although there are many more factors that may play an important role in evaluating ones insurance costs;
#as a final part of this project, i'd like to give a suggestion to our highest paying insurance cost person
#to consider quitting smoking.

#Because they dont have a name, lets add the name "Jane doe" to their information...


our_max_guy.append({"name":"Jane doe"})
print(our_max_guy)


#Great! because this is a list, even though we need two items (a key and a value) we
#pass it as one whole argument inside of our dictionary brackets {} because
#.append() only takes 1 argument, but an entire dictionary can be counted as 1 item


#Now, lets print our message to Jane Doe, and let them know how much they've spent (rounded to the nearest tenth)


smoker_name = our_max_guy[-1]['name']

print("Hey " + smoker_name + "! you should consider quitting smoking to potentially lower your insurance cost! it's $" + str(round(max_charge,2)) + " dollars for you")
    

    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




