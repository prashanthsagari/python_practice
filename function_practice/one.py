def lesser_of_two_evens(a,b):
    result = 0
    if a %2 == 0 and b%2 == 0:
        if a < b:
            result = a
        else:
            result = b
    else:
        if a > b:
            result = a
        else:
            result = b
    return result

print('Basic version')
print(lesser_of_two_evens(2,6))
print(lesser_of_two_evens(2,5))
print(lesser_of_two_evens(3,3))

# improvement
def lesser_of_two_evens_improved(a,b):
    result = 0
    if a %2 == 0 and b%2 == 0:
        # if a < b:
        #     result = a
        # else:
        #     result = b
        result = min(a,b)
    else:
        # if a > b:
        #     result = a
        # else:
        #     result = b
        result = max(a,b)
    return result
print('Improved version')
print(lesser_of_two_evens_improved(2,6))
print(lesser_of_two_evens_improved(2,5))
print(lesser_of_two_evens_improved(3,3))

# further improvement
def lesser_of_two_evens_improved_further(a,b):
    result = 0
    if a %2 == 0 and b%2 == 0:
        # if a < b:
        #     result = a
        # else:
        #     result = b
        return min(a,b)
    else:
        # if a > b:
        #     result = a
        # else:
        #     result = b
        return max(a,b)
    
print('Further Improved version')
print(lesser_of_two_evens_improved_further(2,6))
print(lesser_of_two_evens_improved_further(2,5))
print(lesser_of_two_evens_improved_further(3,3))