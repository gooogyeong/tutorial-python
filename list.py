fruits=['apple', 'banana', 'orange', 'grape', 'kiwi']
fruit_to_eat = 'apple'

last_two_fruits=fruits[-2:]
print(last_two_fruits) # ['grape', 'kiwi']

all_fruits_but_first_fruits=fruits[1:]
print(all_fruits_but_first_fruits) # ['banana', 'orange', 'grape', 'kiwi']

# del fruits[fruits.index(fruit_to_eat)]
# # print(fruits) # ['banana', 'orange', 'grape', 'kiwi']

# # new_fruits=['passion_fruit'] + fruits
# new_fruits=['passion fruit', *fruits]
# print(new_fruits) # ['passion fruit', 'banana', 'orange', 'grape', 'kiwi']