def maxsubarray(nums):
    arrayofsums = [nums[0]]
    maxsum = nums[0]
    maxposition = 0
    for i in range(1, len(nums)):
        if arrayofsums[i - 1] > 0:
            arrayofsums.append(arrayofsums[i - 1] + nums[i])
        else:
            arrayofsums.append(nums[i])
        if arrayofsums[i] > maxsum:
            maxsum = arrayofsums[i]
            maxposition = i
    if maxsum < 0:
        return [nums[maxposition]]
    endofmaxsubarray = maxposition
    startofmaxsubarray = endofmaxsubarray
    while startofmaxsubarray >= 0 and arrayofsums[startofmaxsubarray] >= 0:
        startofmaxsubarray -= 1
    return nums[startofmaxsubarray + 1: endofmaxsubarray + 1]
sourcearray = [2, -5, 2, 2, -1, 3, -1, 2, -5, 4]
print(maxsubarray(sourcearray))
