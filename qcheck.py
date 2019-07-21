import time

def quick_sort(nums, start, end):
    if start >= end:
        return
    pivot = nums[start]  # base
    low = start  # left
    high = end  # right
    while low < high:
        while low < high and nums[high] >= pivot:
            high -= 1
        nums[low] = nums[high]

        while low < high and nums[low] < pivot:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot
    quick_sort(nums, start, low - 1)
    quick_sort(nums, low + 1, end)


if __name__ == '__main__':
	print("--Quick Sorting Method--")
	print("*Enter the number to sort*")
	print("*Separate by spaces*")
	num = [int(n) for n in input().split()] 
	lenA = len(num)-1
	print("before:"num)
	#print(lenA)
	
#start = time.time()
quick_sort(num, 0, lenA)
print("after:",num)
#end = time.time() - start
#print("Time used:",end)

