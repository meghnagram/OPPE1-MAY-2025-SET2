def average(marks):
    return sum(marks)/len(marks)


def filter_students(data: dict, criteria: str) -> set:
    '''
    Takes a dictionary where keys are student names and values are lists of scores, filters names based on the given criteria
     - "excellent" - average score >= 85.
     - "good" - average score >= 50 and < 85.
     - "all_pass" - all scores >= 50.
     - "balanced" - difference between min and max is <= 10.
   
    Args:
        scores(dict)  : keys are student names and values are lists of scores

    Returns:
        set: Set of roll numbers matching the criteria
    '''
    
    
    if criteria == 'excellent':
        return {
            name for name, marks in data.items() 
            if average(marks) >= 85
        }
    elif criteria == 'good':
        return {
            name for name, marks in data.items() 
            if 50 <= average(marks) < 85
        }
    elif criteria == 'all_pass':
        return {
            name for name, marks in data.items() 
            if all(map(lambda x: x >= 50, marks))
        }
    elif criteria == 'balanced':
        return {
            name for name, marks in data.items() 
            if max(marks)-min(marks) <= 10
        }


#     #Another Method:




# def filter_students(data: dict, criteria: str) -> set:
#     '''
#     Takes a dictionary where keys are student names and values are lists of scores, filters names based on the given criteria
#      - "excellent" - average score >= 85.
#      - "good" - average score >= 50 and < 85.
#      - "all_pass" - all scores >= 50.
#      - "balanced" - difference between min and max is <= 10.
   
#     Args:
#         scores(dict)  : keys are student names and values are lists of scores

#     Returns:
#         set: Set of roll numbers matching the criteria
#     '''
#     l=[]
#     check=1
#     if criteria=='excellent':
#         for k,v in data.items():
#             if sum(v)/len(v) >=85:
#                 l.append(k)
#     elif criteria=='good':
#         for k,v in data.items():
#             if 50<=sum(v)/len(v) <85:
#                 l.append(k)
#     elif criteria=='all_pass':
#         for k,v in data.items():
#             check=1
#             for i in v:
#                 if i>=50:
#                     pass
#                 else:
#                     check=0
#                     break
#             if check==1:
#                 l.append(k)
#     elif criteria=='balanced':
#         for k,v in data.items():
#             a=max(v)
#             b=min(v)
#             if a-b <=10:
#                 l.append(k)
                
#     return set(l)


# Student Score Filter
# Given the data of student scores in a dictionary where keys are student names and values are lists of scores. write a function filter_students to filter student roll names based on the following criteria:

# 'excellent': Students with average score >= 85.
# 'good': Students with average score between 50(inclusive) and 85(exclusive).
# 'all_pass': Students with all scores >= 50.
# 'balanced': Students whose difference between max score and min score is <= 10
# NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition. You can define helper functions if needed, but the actual solution should be in the given function template.

# Example

# data = {
#     "Alice": [90, 80, 85],
#     "Bob": [40, 50, 60],
#     "Charlie": [30, 40, 20], 
#     "Ram": [78, 92, 85, 79, 81],
#     "Babu": [67, 70, 75],
#     "Kumar": [ 100, 100, 100, 100, 100, 100, 40]
# }
# print(filter_students(data, 'excellent')) # Output: {'Alice', 'Kumar'}
# print(filter_students(data, 'good')) # Output: {'Babu', 'Bob', 'Ram'}
# print(filter_students(data, 'all_pass')) # Output: {'Alice', 'Babu', 'Ram'}
# print(filter_students(data, 'balanced')) # Output: {'Alice', 'Babu'}
    
