import re

def arithmetic_arranger(problems, show=False):
    # Checks if there are more than 5 expression
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Initialize each part of the final string 
    top_str = ''
    bottom_str = ''
    line_str = ''
    answer_str = ''
    
    for expression in problems:
        op_and_nums = []
        
        # Checks if it is a plus or minus expressions
        if '+' not in expression and '-' not in expression:
            return 'Error: Operator must be \'+\' or \'-\'.'
        
        # Try to evaluate the string otherwise there is a non digit character
        try:
            answer = eval(expression)
    
        except:
            return 'Error: Numbers must only contain digits.'
        
        # Add to the list, operator, num1 and num2, in the form [operator, num1, num2]
        op_and_nums = re.findall('[+-]', expression) + re.findall('\d+', expression)
  
        # If the op_and_nums is bigger than 3 means the are two operators + and -
        if len(op_and_nums) > 3:
            return 'Error: two operators.'

        # Checks if num 1 or num 2 is bigger than 4 digits
        if len(op_and_nums[1]) > 4 or len(op_and_nums[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
    
        # See wich number has bigger lenght and add to de list in the form [operator, num1 , num2, biggest_lengh]
        if len(op_and_nums[1]) > len(op_and_nums[2]):
            op_and_nums.append(len(op_and_nums[1]))
    
        else:
            op_and_nums.append(len(op_and_nums[2]))

        # Add the answer to the list [operator, num1 , num2, biggest_lengh, answer]
        op_and_nums.append(answer)

        # Uses the list values and format the lines 
        top_str += '{:>{size}}    '.format(op_and_nums[1], size=op_and_nums[3] + 2)
        bottom_str += '{}{:>{size}}    '.format(op_and_nums[0] + ' ', op_and_nums[2], size=op_and_nums[3])
        line_str += '{}    '.format('-' * (op_and_nums[3] + 2))
        answer_str += '{:>{size}}    '.format(op_and_nums[4], size=op_and_nums[3] + 2)  
  
    # Checks if it has to show the answers or not
    if show:
        arranged_problems = '\n'.join([top_str.rstrip(), bottom_str.rstrip(), line_str.rstrip(), answer_str.rstrip()])
      
    else:
        arranged_problems = '\n'.join([top_str.rstrip(), bottom_str.rstrip(), line_str.rstrip()])
          
    
    return arranged_problems


print(arithmetic_arranger(["32 + 6989", "3801 - 2", "45 + 43", "123 + 49"], True))
      