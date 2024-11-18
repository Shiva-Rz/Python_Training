'''Create a function named get_results_range(result_dict) that accepts the following dictionary and 
returns the difference between the best and worst exam results.'''

exam_results = {
	'Ethan Hunt': 67,'Bruce Banner': 89,'Tyler Durden': 45,'Steve Rogers': 82,
    'Bruce Wayne': 98,'Oz Cob': 76,'Clarke Kent': 32,'Elon Musk': 28,
	'Tony Stark': 98,'Naval Ravikant': 34}

def get_result_range(exam_results):
    
    user_marks = exam_results.values()
    # print(sorted(user_marks))
    
    best_marks = max(user_marks)
    worst_marks = min(user_marks)
    print(best_marks - worst_marks)

get_result_range(exam_results)