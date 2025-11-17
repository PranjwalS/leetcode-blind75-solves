def topKFrequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    top_k = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)[:k]
    return top_k

nums, k = [1,1,1,2,2,3], 2
print(topKFrequent(nums, k))