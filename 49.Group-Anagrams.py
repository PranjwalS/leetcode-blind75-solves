def groupAnagrams(strs):
    dic = {}
    for str in strs:
        inc = ("".join(sorted(str)))
        if inc not in dic:
            dic[inc] = [str]
        else:
            dic[inc].append(str)
    
    return list(dic.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))