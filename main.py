#-----------------------------------------------------------------------------

# Lab 0
# Problem 1
"""
1. first_name, is a valid name in python, because it is snake case, which is when we use '_' instead of spaces between words.
2. 2nd_name, is invalid, this is because you are unable to use numbers inside of a variable name, snake case.
3. age, is a valid name in python, it is one word and does not need a '_', its also does not include numbers inside of name.
4. total_amount, is a valid name in python, it has a '_' space, snake case.
5. while, is a valid name in python, it is one word with no numbers or symbols.
6. Student, is a valid name in python, it is one word with no numbers of symbols.
7. my-variable, is invalid name in python, this is because they use '-' instead of '_', '-' treats the variable name as two different items, making it 'my' 'variable', a fix to this is to replace '-' with '_'.
8.for, is a valid name in python, it is one word and does not use snake case.
9. _temp, is a valid name in python, the "_" is a little unneeded, however if the name is still set to a value the print function still runs perfectly fine.
10.value#, is an invalid name in python, this is because the '#' at the end causes anything past it to not count in the code, if you set a number or value equal to this variable it will not count because '#' makes it not be visible/count to the code.


"""
# Problem 2
"""
1.calculate_total, is a valid name in python, it is using snake case and '_'.
2.3rd_function, is a invalid name in python, although it is using snake case it still has a number inside the variable name making it invalid.
3.print_values, is a valid name in python, although it includes the comand print it is still a value name because it including '_values', if the variable name were to just be print it would take away the print function and throught the rest of the program if the user include print it will only count as a variable.
4.find-item, this is an invalid name in python, this is because it has '-' which treats 'find' and 'item' as two completly different items which make it not 1 complete variable.
5.def, is an invalid name in python, this is because it is used to create functions, if you were to use this as a varible first off python does not let you, but it would also not allow you to create new function after making a varible called 'def', throughout the program it would treat 'def' as a varible.
6.updateProfile, is a valid name in python, this would work as a varible name however if you were to add '_' for spaces it would make this varible a lot cleaner.
7.my_function, is a valid name in python, this works as a variable because it uses snake case and includes '_'.
8.try, is a invalid name in python, this is because 'try' in python is used to test certain blocks of code, for that reason python reserves 'try' only to be used to test blocks of code, however if the user were to add more onto this name like 'try_test1' it would be a value name.
9.init_data, is a value name in python, it is a snake case and uses '_' to allow for a space making it a value name.
10.value@function, is an invalid name in python, this is because the symbol '@' creates a 'class' making value and function separate and making 'function' into a class destroying the variable name.


"""
# Problem 3
"""
1.'True and False' , this is a value expression, this results in a false outcome, this is because in an and gate both values must be true in order for the outcome to be true, if just one value is false it will lead to an outcome of false.
2. '5 > 3 or "apple" < "banana" , this is a value expression, this results in a true outcome, this is because it is an or gate meaning that just one true value will result in a outcome of true, in the expression 5 > 3 is true and with just 1 true value it is all you need to have a true outcome in an or gate.
3.'not 10 <= 20', is a value expression, this results in a false outcome, this is because 10 <= 20 has an outcome to true, however 'not' is an opperator that resultes in flipping values, in our case here it would flip the outcome for 10 <= 20 of true to false. 
4.'True or 5 = 4' is an invalide expression, this is because in the sub expression '5 = 4' the user is using the wrong opperator, the '=' opperator is setting a value of the left varible but is unable to because 5 is not a varible, a solution to this is to use the '==' this opperation compairs two values and would make the expression valid.
5."apple != "orange" and 5, is a valid expression, its result is 5, this is because if evauated apple != orange is true as '!=' means not true and apple and orange do not equal each other this leave the expression True and 5, 5 is look at as being true and results in 5 because both values are true, the and gate will release the outcome of 5.
6.'3 < 5 not True', is an invalid expression, this is because there is not seperating gate, there must be a 'and' or and 'or' gate/opperation or another opperation for it to be a value expression, this is becaue it can't compair the values together of 3 < 5 , not True.
7.'False == (3 > 4), is a valid expression, the outcome is true, this is because the '==' opperation is compairing 'False' and '(3 > 4)' this results in true because 3 > 4 is false and it results to 'False == False' with is equal and outcomes to true.
8.'10 <= "10", is an invalid expression, this is because "10" does not count in the code as a number, instead a string, because of this the expression is not able to calculate because one of the 10s is in a string.
9.'True or not False', is a valid expression, its outcome is True, this is because the expression uses and or gate, this means that just one True value is enough to resulte in a true outcome, it also include a not false which is also results in a true value, this makes the expression 'True or True' which just results to True.
10.'5 and or 4', this is an invalid expression, this is because it includes two opperators, it has nothing in the middle seperating them which results in a SyntaxError.


"""
#-----------------------------------------------------------------------------
# Homework 0
# Problem 1
def is_even(x):
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


# Problem 2
def split_dict_to_lists(some_dict: dict):
  
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
    return list_keys, list_values


# Problem 3
def evaluate_expression(boolean1, boolean2, string_operator)->bool:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.   
        

# Problem 4
def find_odd_numbers(a_list: list)-> list:
    """
    a_list is just one example of a the kind of input you could recieve
    a_list = [3,4,5,6,7]
    odd_list = [3,5,7]
    """
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.
        
# Problem 5
def calculate_average(numbers_list: list)-> int:
    pass # get rid of the pass when you implement your function. pass just serves as a placeholder for a partially filled in function.


import sys
def test(did_pass):
   """ Print the result of a test. """
   linenum = sys._getframe(1).f_lineno
   msg = "Test at line {0} {1}.".format(linenum, "ok" if did_pass else "FAILED")
   print(msg)



def test_is_even():
    test(is_even(4) == True)
    test(is_even(5) == False)
    test(is_even(0) == True)

def test_split_dict_to_lists():
    keys, values = split_dict_to_lists({'a': 1, 'b': 2})
    test(keys == ['a', 'b'])
    test(values == [1, 2])
    keys, values = split_dict_to_lists({'c': 3, 'd': 3})
    test(keys == ['c', 'd'])
    test(values == [3, 3])

def test_evaluate_expression():
    test(evaluate_expression(True, False, 'and') == False)
    test(evaluate_expression(True, True, 'and') == True)
    test(evaluate_expression(True, False, 'or') == True)
    test(evaluate_expression(False, True, 'not') == True)

def test_find_odd_numbers():
    test(find_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5])
    test(find_odd_numbers([2, 4, 6]) == [])

def test_calculate_average():
    test(calculate_average([10, 20, 30, 40, 50]) == 30.0)
    test(calculate_average([5, 5, 5, 5]) == 5.0)


def test_suite():
    test_is_even()
    test_split_dict_to_lists()
    test_evaluate_expression()
    test_find_odd_numbers()
    test_calculate_average()

test_suite()  # Here is the call to run the tests
