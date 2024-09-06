nums = input("Add meg a számokat: ")

def Main(nums):

    nums.strip()
    numlist = []

    for i in nums:
        numlist.append(int(i))

    for k in numlist:
        if k//2 != 0:
            numlist.remove(k)

    print(numlist)

Main(nums)