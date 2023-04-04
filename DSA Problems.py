# class Solution(object):
#     def maximumWealth(self, accounts):
#         max_wealth = 0
#         for customer in accounts:
#             total = 0
#             for single_customer_wealth in customer:
#                 total += single_customer_wealth
#             if total >= max_wealth:
#                 max_wealth = total
#         return max_wealth
#
#
# sol = Solution()
# print(sol.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

# class Solution(object):
#     def shuffle(self, nums, n):
#         diff = n
#         index = 0
#
#         for i in range(n-1):
#             nums.insert(index+1, nums[index+diff])
#             nums.pop(index+diff+1)
#
#             diff -= 1
#             index += 2
#
#         return nums
#
#
# sol = Solution()
# print(sol.shuffle([2,5,1,3,4,7], 3))

# class Solution(object):
#     def countConsistentStrings(self, allowed, words):
#         result_not_match = 0
#         for word in words:
#             for character in word:
#                 if character not in allowed:
#                     result_not_match += 1
#                     break
#
#         return len(words) - result_not_match
#
#
# sol = Solution()
# print(sol.countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))

# def rev(list1):
#   index = len(list1)-1
#   for i in range(int(len(list1)/2)):
#     temp = list1[index]
#     list1[index] = list1[i]
#     list1[i] = temp
#     list1[index] ^ 1
#     list1[i] ^ 1
#     index -= 1
#
#   return list1
#
# print(rev([1,0,1,0,1,0]))

# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         main_list = [i for i in range(1,len(nums)+1)]
#         new_list = []
#         set1 = set()
#         for num in nums:
#             set1.add(num)
#
#         for num in set1:
#             new_list.append(num)
#
#         for num in new_list:
#             main_list.remove(num)
#
#         return main_list
#
#
# sol = Solution()
# print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))

# class Solution(object):
#     def luckyNumbers(self, matrix):
#         min_list = []
#         result = []
#         max_col = 0
#         for row in matrix:
#             min_list.append(row[0])
#             for each_element_row in row:
#                 if each_element_row < min_list[-1]:
#                     min_list[-1] = each_element_row
#
#
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 if matrix[j][i] > max_col:
#                     max_col = matrix[j][i]
#
#             for each in min_list:
#                 if max_col == each:
#                     result.append(each)
#
#
#
# sol = Solution()
# sol.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]])


# class Solution(object):
#     def middleNode(self, head):
#
#         middle_point = int(len(head))
#         result = []
#
#         current_node = head[0]
#         for i in range(middle_point):
#             current_node = current_node.next
#
#         while current_node is not None:
#             result.append(current_node.val)
#             current_node = current_node.next
#
#         return result


# treat head like actual linked list head, not list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def middleNode(self, head):
#         node = head
#         count = 0
#         while node is not None:
#             count += 1
#             node = node.next
#
#         middle_point = int(count / 2)
#         result = []
#
#         current_node = head
#         for i in range(middle_point):
#             current_node = current_node.next
#
#         # while current_node is not None:
#         #     result.append(current_node.val)
#         #     current_node = current_node.next
#
#         return current_node


# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         node = list2 if list2.val <= list1.val else list1
#
#         if node == list2:
#             while node is not None and list1 is not None:
#                 if list2 <= list1 <= list2.next:
#                     temp_node = list1
#                     list1 = list1.next
#                     temp_node.next = list2.next
#                     list2.next = temp_node
#
#                 node = node.next

# class Solution(object):
#     def isPowerOfTwo(self, n):
#         if n == 1:
#             return True
#         if n % 2 != 0:
#             return False
#         return isPowerOfTwo(n/2)
#
# class Solution(object):
#     def numIdenticalPairs(self, nums):
#         dict = {}
#         for num in nums:
#             if num not in dict.keys():
#                 dict[num] = 0
#             else:
#                 if dict[num] == 0:
#                     dict[num] = 1
#                 else:
#                     dict[num] = dict[num]*2
#                     dict[num] = dict[num]+1
#
#         return sum(dict.values())
#
#
# sol = Solution()
# print(sol.numIdenticalPairs([1,2,3,1,1,,3]))


# class Solution(object):
#     def checkIfPangram(self, sentence):
#         alph = set()
#         for a in sentence:
#             alph.add(a)
#         if len(alph) == 26:
#             return True
#         else:
#             return False
#
# sol = Solution()
# print(sol.checkIfPangram("twnfoxjumpsoverthelazydog"))

# class Solution(object):
#     def sortPeople(self, names, heights):
#         people = {}
#         output = []
#         for i in range(len(names)):
#             people[names[i]] = heights[i]
#
#         for key, value in sorted(people.items(), key=lambda v: v[1],reverse=True):
#             output.append(key)
#
#         return output
#
#
# sol = Solution()
# print(sol.sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))

# class Solution(object):
#     def destCity(self, paths):
#         path_dictionary = {}
#         for path in paths:
#             path_dictionary[path[0]] = path[1]
#
#         for value in path_dictionary.values():
#             if value not in path_dictionary.keys():
#                 return value
#
# sol = Solution()
# print(sol.destCity([["B","C"],["D","B"],["C","A"]]))

# class Solution(object):
#     def repeatedCharacter(self, s):
#         set1 = set()
#         for char in s:
#             if char not in set1:
#                 set1.add(char)
#             else:
#                 return char
#
#
# sol = Solution()
# print(sol.repeatedCharacter("abcdd"))


# class Solution(object):
#     def divideArray(self, nums):
#         arr_total = int(len(nums))
#         dict_total = 0
#         d = {}
#         for num in nums:
#             if num not in d:
#                 d[num] = 1
#             else:
#                 d[num] += 1
#         print(d)
#         for val in d.values():
#             if val%2 != 0:
#                 return False
#             else:
#                 dict_total += val
#
#         if arr_total == dict_total:
#             return True
#         else:
#             return False
#
# sol = Solution()
# print(sol.divideArray([3,2,3,2,2,3]))


# class Solution(object):
#     def uniqueOccurrences(self, arr):
#         dict1 = {}
#         set1 = set()
#         for ele in arr:
#             if ele not in dict1:
#                 dict1[ele] = 1
#             else:
#                 dict1[ele] += 1
#
#         for val in dict1.values():
#             set1.add(val)
#
#         if len(dict1) == len(set1):
#             return True
#         else:
#             return False
#
# sol = Solution()
# print(sol.uniqueOccurrences([1,2,2,1,3]))

# class Solution(object):
#     def countCharacters(self, words, chars):
#         total = 0
#         chars_dir = {}
#         for char in chars:
#             if char not in chars_dir:
#                 chars_dir[char] = 1
#             else:
#                 chars_dir[char] += 1
#         print(chars_dir)
#         for word in words:
#             new_dir = chars_dir.copy()
#             for char in word:
#                 if char not in new_dir and new_dir[char] <= 0:
#                     break
#                 else:
#                     new_dir[char] -= 1
#             total += len(char)
#
#         return total
#
#
# sol = Solution()
# print(sol.countCharacters(["cat","bt","hat","tree"], "atach"))

# class Solution(object):
#     def twoOutOfThree(self, nums1, nums2, nums3):
#         print(nums2)
#         set1 = set(nums1)
#         set2 = set(nums2)
#         set3 = set(nums3)
#         new_dict = {}
#         result = []
#         for num in set1:
#             if num not in new_dict:
#                 new_dict[num] = 1
#             else:
#                 if new_dict[num] == 1:
#                     new_dict[num] += 1
#                     result.append(num)
#                 else:
#                     new_dict[num] += 1
#         for num in set2:
#             if num not in new_dict:
#                 new_dict[num] = 1
#             else:
#                 if new_dict[num] == 1:
#                     new_dict[num] += 1
#                     result.append(num)
#                 else:
#                     new_dict[num] += 1
#         for num in set3:
#             if num not in new_dict:
#                 new_dict[num] = 1
#             else:
#                 if new_dict[num] == 1:
#                     new_dict[num] += 1
#                     result.append(num)
#                 else:
#                     new_dict[num] += 1
#         print(new_dict)
#         return result
# sol = Solution()
# print(sol.twoOutOfThree([3,1],[2,3],[1,2]))


# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         dict1 = {}
#         for letter in magazine:
#             if letter not in dict1:
#                 dict1[letter] = 1
#             else:
#                 dict1[letter] += 1
#         print(dict1)
#         for char in ransomNote:
#             if char not in dict1 or dict1[char] == 0:
#                 return False
#             else:
#                 dict1[char] -= 1
#
#         return True
#
# sol = Solution()
# print(sol.canConstruct("aa","ab"))

# class Solution(object):
#     def findTheDifference(self, s, t):
#         set_s = set(s)
#         for char in t:
#             if char not in set_s:
#                 return char
#
#
# sol = Solution()
# print(sol.findTheDifference("abcd", "abcde"))

# class Solution(object):
#     def findRestaurant(self, list1, list2):
#         set1 = set(list1)
#         set2 = set(list2)
#         result = []
#         count_dir = {}
#         common_set = set1 & set2
#
#         if len(common_set) == 1:
#             return [common_set.pop()]
#         else:
#             for element in common_set:
#                 count_dir[element] = list1.index(element) + list2.index(element)
#
#         min_index_count = min(count_dir.values())
#         print(min_index_count)
#
#         for key in count_dir:
#             if count_dir[key] == min_index_count:
#                 result.append(key)
#
#         return result
#
# sol = Solution()
# print(sol.findRestaurant(["happy","sad","good"],["sad","happy","good"]))


# class Solution(object):
#     def searchInsert(self, nums, target):
#         result = None
#         low = nums[0]
#         high = nums[len(nums) - 1]
#
#         if low == target:
#             return 0
#         if high == target:
#             return len(nums) - 1
#         if len(nums) == 2:
#             return 1
#
#         medium = int(len(nums) / 2)
#         print(nums[medium])
#         if target == nums[medium]:
#             return medium
#         elif target < nums[medium]:
#             result = self.searchInsert(nums[:medium + 1], target)
#         else:
#             result = self.searchInsert(nums[medium:len(nums) - 1], target)
#
#         return result
#
# sol = Solution()
# print(sol.searchInsert([1, 2,3,4,5,6,7,8], 7))


# class Solution(object):
#     def searchInsert(self, nums, target):
#         low = 0
#         high = len(nums) - 1
#         medium = int(len(nums)/2)
#         if nums[low] == target:
#             return low
#         if nums[high] == target:
#             return high
#
#         while low+1 != high:
#             if nums[medium] == target:
#                 return medium
#
#             if target < nums[medium]:
#                 high = medium
#             if target > nums[medium]:
#                 low = medium
#
#         return low+1
#
# sol = Solution()
# print(sol.searchInsert([1,3,5,6],4))


# class Solution(object):
#     def checkStraightLine(self, coordinates):
#         for i in range(len(coordinates)-1):
#             if coordinates[i+1][0] - coordinates[i][0] == coordinates[i+1][1] - coordinates[i][1]:
#                 continue
#             else:
#                 return False
#         return True
#
#
#
# sol = Solution()
# print(sol.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))


# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         flower = n
#         counter = 0
#         for i in range(1,len(flowerbed)):
#             if flowerbed[i] == 0:
#                 if flowerbed[i-1] == 1:
#                     counter = 1
#                 else:
#                     counter += 1
#                     if counter == 3:
#                         counter = 0
#                         flower -= 1
#
#         if flower == 0:
#             return True
#         else:
#             return False
#
#
#
# sol = Solution()
# print(sol.canPlaceFlowers([1,0,1,0,1],1))

# class Solution(object):
#     def findJudge(self, n, trust):
#         dict = {}
#         set1 = set()
#         for i in range(len(trust)):
#             dict[trust[i][0]] = trust[i][1]
#             set1.add(trust[i][1])
#
#         if len(set1) == 1:
#             set_element = set1.pop()
#             if set_element not in dict:
#                 return set_element
#             else:
#                 return -1
#         else:
#             return -1
#
#
# sol = Solution()
# print(sol.findJudge(3, [[1,3],[2,3],[3,1]]))
# import math
# class Solution(object):
#     def targetIndices(self, nums, target):
#         result = []
#         no_of_buckets = round(math.sqrt(len(nums)))
#         max_no = max(nums)
#         buckets = []
#
#         for i in range(no_of_buckets):
#             buckets.append([])
#
#         for i in nums:
#             index = math.ceil(i*no_of_buckets/max_no) - 1
#             buckets[index].append(i)
#
#         for bucket in buckets:
#             for i in range(len(bucket)-1):
#                 for j in range(len(bucket)-1-i):
#                     if bucket[j] > bucket[j+1]:
#                         bucket[j], bucket[j+1] = bucket[j+1], bucket[j]
#
#         print(buckets)
#         k = 0
#         for bucket in buckets:
#             for element in bucket:
#                 nums[k] = element
#                 if element == target:
#                     result.append(k)
#                 k += 1
#
#         return result
#
#
# sol = Solution()
# print(sol.targetIndices([1,2,5,2,3], 3))


# class Solution(object):
#     def missingNumber(self, nums):
#         num_list = [i for i in range(len(nums)+1)]
#         print(num_list)
#         for i in range(len(nums)):
#             num_list.remove(nums[i])
#         return num_list.pop()
#
# sol = Solution()
# print(sol.missingNumber([0,1]))


# class Solution(object):
#     def countStudents(self, students, sandwiches):
#         rotate = 0
#         while len(students) != 0:
#             if sandwiches[0] == students[0]:
#                 sandwiches.pop(0)
#                 students.pop(0)
#             else:
#                 if rotate == len(students):
#                     return len(students)
#                 else:
#                     std = students[0]
#                     students.pop(0)
#                     students.append(std)
#                     rotate += 1
#
#         return 0
#
#
# sol = Solution()
# print(sol.countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))

# class Solution(object):
#     def nextGreaterElement(self, nums1, nums2):
#         result = []
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i] == nums2[j]:
#                     for k in range(j+1, len(nums2)):
#                         if nums2[k] > nums2[j]:
#                             result.append(nums2[k])
#                             break
#             if len(result) != i+1:
#                 result.append(-1)
#
#
#         return result
#
#
# sol = Solution()
# print(sol.nextGreaterElement([2,4], [1,2,3,4]))


# def monotonic_stack(list1):
#     stack = []
#     dic = dict()
#
#     for element in list1:
#         print(stack)
#         if not stack:
#             stack.append(element)
#         else:
#             if element < stack[-1]:
#                 stack.append(element)
#             else:
#
#                 while stack and stack[-1] < element:
#                     print(stack[-1])
#                     dic[stack[-1]] = element
#                     stack.pop()
#                 stack.append(element)
#
#     if not stack:
#         for ele in stack:
#             dic[ele] = -1
#
#     print(dic)
#
#
# monotonic_stack([5,2,1,6,10])


# class Solution(object):
#     def finalPrices(self, prices):
#         stack = []
#         dic = dict()
#         result = []
#
#         for element in prices:
#             if not stack:
#                 stack.append(element)
#             else:
#                 if element > stack[-1]:
#                     stack.append(element)
#                 else:
#                     while stack and stack[-1] > element:
#                         dic[stack[-1]] = element
#                         stack.pop()
#                     stack.append(element)
#
#         if stack:
#             for ele in stack:
#                 dic[ele] = 0
#
#         for i in range(len(prices)):
#             prices[i] -= dic[prices[i]]
#
#         return prices
#
#
# sol = Solution()
# sol.finalPrices([8,4,6,2,3])

# from collections import deque
# class MyStack(object):
#
#     def __init__(self):
#         self.q = deque()
#
#     def push(self, x):
#         self.q.append(x)
#
#     def pop(self):
#         for i in range(len(self.q)-1):
#             self.q.append(self.q.popleft())
#         return self.q.popleft()
#
#     def top(self):
#         return self.q[-1]
#
#     def empty(self):
#         return len(self.q) == 0
#
#
# my_stack = MyStack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# my_stack.push(4)
# print(my_stack.top())
# print(my_stack.pop())
# print(my_stack.q)


# class MyQueue(object):
#
#     def __init__(self):
#         self.stack1 = list()
#         self.stack2 = list()
#
#     def push(self, x):
#         self.stack1.append(x)
#
#     def pop(self):
#         for i in range(-1, -1, -1):
#             self.stack2.append(self.stack1[i])
#         self.stack1.pop(0)
#         return self.stack2.pop()
#
#     def peek(self):
#         for i in range(len(self.stack1)-1, -1, -1):
#             self.stack2.append(self.stack1[i])
#         return self.stack2[-1]
#
#     def empty(self):
#         return len(self.stack1) == 0
#
#
# my_queue = MyQueue()
# my_queue.push(1)
# my_queue.push(2)
# my_queue.push(3)
# my_queue.push(4)
# print(my_queue.peek())
# print(my_queue.pop())
# print(my_queue.peek())

# class Solution(object):
#     def makeGood(self, s):
#         stack = list()
#         for chara in s:
#             if not stack:
#                 stack.append(chara)
#             else:
#                 if chara == chara.upper():
#                     stack.pop()
#                 else:
#                     stack.append(chara)
#
#         return "".join(stack)
#
#
# sol = Solution()
# print(sol.makeGood("s"))

# class Solution(object):
#     def backspaceCompare(self, s, t):
#         stack_s = []
#         stack_t = []
#
#         for element in s:
#             if not stack_s:
#                 stack_s.append(element)
#             else:
#                 if element == "#":
#                     stack_s.pop()
#                     continue
#                 else:
#                     stack_s.append(element)
#
#         for element in t:
#             if not stack_t:
#                 stack_t.append(element)
#             else:
#                 if element == "#":
#                     stack_t.pop()
#                     continue
#                 else:
#                     stack_t.append(element)
#
#         if "".join(stack_s) == "".join(stack_t):
#             return True
#         else:
#             return False
#
#
# sol = Solution()
# print(sol.backspaceCompare("a#c", "b"))


# class Solution(object):
#     def checkTree(self, root):
#         if root.val == (root.left.val + root.right.val):
#             return True
#         else:
#             return False

# class Solution(object):
#     def getTargetCopy(self, original, cloned, target):
#         stack = []
#         stack.append(cloned)
#         while stack:
#             popped_node = stack.pop()
#             if popped_node.val == target.val:
#                 return popped_node
#             if popped_node.right:
#                 stack.append(popped_node.right)
#             if popped_node.left:
#                 stack.append(popped_node.left)


# class Solution(object):
#     def mergeTrees(self, root1, root2):
#         if not root1 and not root2:
#             return
#         node = TreeNode()
#         if root1 and root2:
#             node.val = root1.val + root2.val
#         elif root1 and not root2:
#             node.val = root1.val
#         else:
#             node.val = root2.val
#
#         node.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
#         node.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
#
#         return node

# class Solution(object):
#     def maxDepth(self, root):
#         depth = 0
#         if root:
#             depth += 1
#
#         stack = []
#         stack.append(root)
#         while stack:
#             popped_node = stack.pop()
#             if popped_node.left or popped_node.right:
#                 depth += 1
#                 if popped_node.right:
#                     stack.append(popped_node.right)
#                 if popped_node.left:
#                     stack.append(popped_node.left)
#
#         return depth

# from queue import Queue
# class Solution(object):
#     def averageOfLevels(self, root):
#         avg_list = []
#         que = Queue()
#         if root:
#             avg_list.append(root.val)
#         que.put(root)
#         while not que.empty():
#             popped_node = que.get()
#             if popped_node.left and popped_node.right:
#                 avg = ((popped_node.left.val + popped_node.right.val)/2)
#                 avg_list.append(avg)
#                 que.put(popped_node.left)
#                 que.put(popped_node.right)
#                 continue
#             if popped_node.left:
#                 avg_list.append(popped_node.left.val)
#                 que.put(popped_node.left)
#                 continue
#             if popped_node.right:
#                 avg_list.append(popped_node.right.val)
#                 que.put(popped_node.right)
#                 continue
#         return avg_list

# class Solution(object):
#     def isUnivalTree(self, root):
#         unival = root.val
#         stack = []
#         stack.append(root)
#
#         while stack:
#             popped_node = stack.pop()
#             if popped_node.val != unival:
#                 return False
#             if popped_node.right:
#                 stack.append(popped_node.right)
#             if popped_node.left:
#                 stack.append(popped_node.left)
#
#         return True

# class Solution(object):
#     def leafSimilar(self, root1, root2):
#         t1 = []
#         t2 = []
#
#         stack1 = []
#         stack2 = []
#
#         stack1.append(root1)
#
#         while stack1:
#             popped_node = stack1.pop()
#             if not popped_node.left and not popped_node.right:
#                 t1.append(popped_node.val)
#                 continue
#             if popped_node.right:
#                 stack1.append(popped_node.right)
#             if popped_node.left:
#                 stack1.append(popped_node.left)
#
#         stack2.append(root2)
#
#         while stack2:
#             popped_node = stack2.pop()
#             if not popped_node.left and not popped_node.right:
#                 t2.append(popped_node.val)
#                 continue
#             if popped_node.right:
#                 stack2.append(popped_node.right)
#             if popped_node.left:
#                 stack2.append(popped_node.left)
#
#         if t1 == t2:
#             return True
#         else:
#             return False

# class Solution(object):
#     def isSameTree(self, p, q):
#         if not p and not q:
#             return True
#         if p and not q:
#             return False
#         if not p and q:
#             return False
#         if p.val != q.val:
#             return False
#
#         a = self.isSameTree(p.left, q.left)
#         b = self.isSameTree(p.right, q.right)
#
#         return a and b

from multiprocessing import Queue

# class Solution(object):
#     def invertTree(self, root):
#         if not root:
#             return root
#
#         q = Queue()
#         q.put(root)
#         while not q.empty():
#             popped_node = q.get()
#             if popped_node.left and popped_node.right:
#                 swapped_node = popped_node.left
#                 popped_node.left = popped_node.right
#                 popped_node.right = swapped_node
#                 q.put(popped_node.left)
#                 q.put(popped_node.right)
#
#             else:
#                 if popped_node.left:
#                     q.put(popped_node.left)
#
#                 if popped_node.right:
#                     q.put(popped_node.right)
#
#         return root
#
#
# class Solution(object):
#     def invertTree(self, root):
#         if root is None:
#             return None
#
#         swapped = root.left
#         root.left = root.right
#         root.right = swapped
#
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#
#         return root


# class Solution(object):
#     def findCenter(self, edges):
#         graph_dict = {}
#         for edge in edges:
#             if edge[0] not in graph_dict:
#                 graph_dict[edge[0]] = []
#             if edge[1] not in graph_dict:
#                 graph_dict[edge[1]] = []
#             graph_dict[edge[0]].append(edge[1])
#             graph_dict[edge[1]].append(edge[0])
#
#         print(len(graph_dict))
#
#         for v in graph_dict:
#             if len(graph_dict[v]) > 1 and len(graph_dict[v]) == len(graph_dict) - 1:
#                 return v
#
#         return False
# sol = Solution()
# print(sol.findCenter([[1,2],[2,3],[4,2]]))

# class Solution(object):
#     def allPathsSourceTarget(self, graph):
#         graph_dict = {}
#         result = []
#         dest = len(graph) - 1
#
#         for i in range(len(graph)):
#             graph_dict[i] = graph[i]
#
#         def path_finder(v1, path):
#             if v1 == dest:
#                 a = path.copy()
#                 result.append(a)
#
#                 return
#             for neighbour in graph_dict[v1]:
#                 path.append(neighbour)
#                 path_finder(neighbour, path)
#                 path.pop()
#
#         path_finder(0, [0])
#         return result
#
#
#
# sol = Solution()
# print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))


# class Solution(object):
#     def findSmallestSetOfVertices(self, n, edges):
#         vlist = [i for i in range(n)]
#         vdict = {}
#
#         for edge in edges:
#             vdict[edge[1]] = edge[0]
#
#         return list(set(vlist) ^ set(list(key for key in vdict.keys())))
#
# sol = Solution()
# print(sol.findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]))


# class Solution(object):
#     def canVisitAllRooms(self, rooms):
#         room_set = set(rooms[0])
#
#
#         for room_num in range(1, len(rooms)):
#             print(room_set)
#             if room_num not in room_set:
#                 return False
#             room_set = room_set.union(set(rooms[room_num]))
#
#         return True
#
# sol = Solution()
# print(sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])
#
# class Solution(object):
#     def regionsBySlashes(self, grid):
#         total = 1
#         cur = 0
#         new_list = []
#         for i in grid:
#             for j in i:
#                 new_list.append(j)
#
#         grid_matrix = [[0]*3]*3
#
#         for i in range (0,2):
#             for j in range(0,3):
#                 if new_list[cur] == " ":
#                     continue
#                 else:
#                     if new_list[cur]
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # class Solution(object):
#     def flipAndInvertImage(self, image):
#         for img in image:
#             low = 0
#             high = len(img)-1
#
#             while not ((low == high) or high < low):
#                 img[low],img[high] = img[high],img[low]
#                 low += 1
#                 high -= 1
#
#             for i in range(len(img)):
#                 img[i] = int(not(img[i]))
#
#         return image
#
#
# sol = Solution()
# print(sol.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

# class Solution(object):
#     def reversePrefix(self, word, ch):
#         word_list = list(word)
#         low = 0
#         high = 0
#         if ch not in word_list:
#             return "".join(word_list)
#         else:
#             high = word_list.index(ch)
#
#             while not ((low == high) or (high < low)):
#                 word_list[low], word_list[high] = word_list[high], word_list[low]
#                 low += 1
#                 high -= 1
#         return "".join(word_list)
#
#
# sol = Solution()
# print(sol.reversePrefix(word = "abcd", ch = "z"))


# class Solution(object):
#     def sortArrayByParity(self, nums):
#         if len(nums) == 1:
#             return nums
#         else:
#             low = 0
#             high = 0
#             while high < len(nums):
#                 if nums[low]%2 != 0:
#                     if nums[high]%2 == 0:
#                         nums[low], nums[high] = nums[high], nums[low]
#                         low += 1
#                         high += 1
#                     else:
#                         high += 1
#
#
#             return nums
#
#
# sol = Solution()
# print(sol.sortArrayByParity([3,1,2,4]))


# class Solution(object):
#     def moveZeroes(self, nums):
#         if len(nums) == 1:
#             return nums
#         else:
#             low = 0
#             high = len(nums) - 1
#             while high >= low:
#                 if nums[low] == 0:
#                     while nums[high] == 0:
#                         high -= 1
#                     nums[low], nums[high] = nums[high], nums[low]
#                     low += 1
#                     high -= 1
#                 else:
#                     low += 1
#
#             return nums
#
#
# sol = Solution()
# print(sol.moveZeroes([0,1,0,3,12]))


# class Solution(object):
#     def moveZeroes(self, nums):
#         if len(nums) == 1:
#             return nums
#         else:
#             low = 0
#             high = 1
#
#             while high < len(nums):
#                 if nums[low] == 0:
#                     if nums[high] != 0:
#                         nums[low], nums[high] = nums[high], nums[low]
#                         low += 1
#                         high += 1
#                     else:
#                         high += 1
#                 else:
#                     low += 1
#
#             return nums
#
#
# sol = Solution()
# print(sol.moveZeroes([0,1,0,3,12]))


# class Solution(object):
#     def distinctAverages(self, nums):
#         nums.sort()
#         set1 = set()
#
#         while len(nums) > 0:
#             avg1 = (nums[0] + nums[-1]) / 2
#             set1.add(avg1)
#             nums.pop(0)
#             nums.pop(-1)
#
#         return len(set1)
#
#
#
#
# sol = Solution()
# print(sol.distinctAverages([1,100]))

# class Solution(object):
#     def xorOperation(self, n, start):
#         nums = []
#         xor_nums = 0
#         for i in range(n):
#             nums.append((start) + (2 * i))
#             xor_nums = xor_nums ^ ((start) + (2 * i))
#
#         return xor_nums


# class Solution(object):
#     def minBitFlips(self, start, goal):
#        return ((str(bin((start^goal))).count("1")))

# class Solution(object):
#     def countConsistentStrings(self, allowed, words):
#         const_str = 0
#         for i in range(len(words)):
#             for j in words[i]:
#                 if j not in allowed:
#                     const_str += 1
#                     break
#
#         return len(words) - const_str

# class Solution(object):
#     def singleNumber(self, nums):
#         set1 = set()
#         for element in nums:
#             if element not in set1:
#                 set1.add(element)
#             else:
#                 set1.remove(element)
#
#         return set1.pop()

# class Solution(object):
#     def addBinary(self, a, b):
#       decimal_sum = int(a,2) + int(b,2)
#       binary_sum = bin(decimal_sum)
#       return binary_sum[2:]

# class Solution(object):
#     def hasAlternatingBits(self, n):
#         binary_num = bin(n)[2:]
#         for i in range(len(binary_num) - 1):
#             print(binary_num[i], binary_num[i + 1])
#             if binary_num[i] == binary_num[i + 1]:
#                 return False
#         return True
#
#
# sol = Solution()
# print(sol.hasAlternatingBits(7))

##############################Medium##########################
# class Solution(object):
#     def groupThePeople(self, groupSizes):
#         dict1 = {}
#         result = []
#
#         for i in range(len(groupSizes)):
#             if groupSizes[i] not in dict1:
#                 dict1[groupSizes[i]] = []
#
#             dict1[groupSizes[i]].append(i)
#
#             if len(dict1[groupSizes[i]]) == groupSizes[i]:
#                 result.append(dict1[groupSizes[i]])
#                 dict1[groupSizes[i]] = []
#
#         return result
#
# sol = Solution()
# sol.groupThePeople([3,3,3,3,3,1,3])


# class Solution(object):
#     def garbageCollection(self, garbage, travel):
#         type = ["G","P","M"]
#         total = 0
#         for typ in type:
#             for i in range(len(garbage)):
#                 total = total + garbage[i].count(typ)
#                 if i < len(travel):
#                     total += travel[i]
#
#         return total
#
# sol = Solution()
# print(sol.garbageCollection(["G","P","GP","GG"], [2,4,3]))

# class Solution(object):
#     def wateringPlants(self, plants, capacity):
#         steps = 1
#         for i in range(len(plants)):
#             capacity -= plants[i]
#
#             if i < len(plants)-1:
#
#                 if capacity >= plants[i+1]:
#                     steps += 1
#                 else:
#                     steps += (2*abs(-1-i))
#                     steps += 1
#
#         return steps
#
#
# sol = Solution()
# print(sol.wateringPlants([2,2,3,3], 5))

# class Solution(object):
#     def minPairSum(self, nums):
#         list1 = []
#         low = 0
#         high = len(nums)-1
#         nums.sort()
#
#         for i in range(len(nums)//2):
#             ele = (nums[low],nums[high])
#             list1.append(sum(ele))
#             low += 1
#             high -= 1
#
#         return max(list1)


# class Solution(object):
#     def findWinners(self, matches):
#         players_record = {}
#         result = [[],[]]
#
#         for match in matches:
#             if match[1] not in players_record:
#                 players_record[match[1]] = []
#             players_record[match[1]].append(match[0])
#             if match[0] not in players_record:
#                 players_record[match[0]] = []
#
#         for key in players_record:
#             if len(players_record[key]) == 0:
#                 result[0].append(key)
#             if len(players_record[key]) == 1:
#                 result[1].append(key)
#
#
# sol = Solution()
# sol.findWinners([[2,3],[1,3],[5,4],[6,4]])


# class Solution(object):
#     def findTheWinner(self, n, k):
#         p = 0
#         list1 = list(range(1,n+1))
#
#         while len(list1) > 1:
#
#             for i in range(k-1):
#                 if p == len(list1)-1:
#                     p = 0
#                 else:
#                     p += 1
#
#             if p == len(list1) - 1:
#                 list1.pop(-1)
#                 p = 0
#             else:
#                 list1.pop(p)
#
#         return list1[0]
#
#
# sol = Solution()
# print(sol.findTheWinner(5,2))
#
#
# # Write your MySQL query statement below
#
# SELECT product_id
# FROM products
# WHERE low_fats = "Y" AND recyclable = "Y"
#
#
# SELECT date_id, make_name, COUNT(DISTINCT(lead_id)) AS unique_leads, COUNT(DISTINCT(partner_id))
# AS unique_partners
# FROM dailysales
# GROUP BY date_id, make_name


# from collections import deque
#
# class Solution(object):
#     def findCircleNum(self, isConnected):
#         graph_dict = {}
#         visited_vertex = []
#         total = 0
#         for i in range(len(isConnected)):
#             if i not in graph_dict:
#                 graph_dict[i] = []
#             for j in range(len(isConnected[i])):
#                 if isConnected[i][j] == 1 and i != j:
#                     graph_dict[i].append(j)
#         print(graph_dict)
#
#         for v in graph_dict:
#             if v not in visited_vertex:
#                 queue = deque()
#                 queue.append(v)
#                 while queue:
#                     popped_v = queue.popleft()
#                     visited_vertex.append(popped_v)
#                     if graph_dict[v]:
#                         for neighbour in graph_dict[v]:
#                             if neighbour not in visited_vertex:
#                                 queue.append(neighbour)
#                 total += 1
#         return total
#
#
#
# sol = Solution()
# sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]])


# class Solution(object):
#     def eventualSafeNodes(self, graph):
#         graph_dict = {}
#         dest_node = []
#         safe_node = []
#         for i in range(len(graph)):
#             if len(graph[i]) == 0:
#                 dest_node.append(i)
#             graph_dict[i] = graph[i]
#
#         for v in graph_dict:
#             if len(graph_dict[v]) == 1 and graph_dict[v][0] in dest_node:
#                 safe_node.append(v)
#
#         dest_node.extend(safe_node)
#         return dest_node.sort()
#
# sol = Solution()
# sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])


###################################### disjoin and union/find data structure ####################

# class Solution(object):
#     def findRedundantConnection(self, edges):
#         parent_nodes = [i for i in range(len(edges)+1)]
#
#         for edge in edges:
#             node1 = edge[0]
#             node2 = edge[1]
#
#             def find_parent_node(node):
#
#                 while node > 0 and node != parent_nodes[node]:
#                     node -= 1
#                 return node
#
#             node1_parent = find_parent_node(node1)
#             node2_parent = find_parent_node(node2)
#
#             if node1_parent != node2_parent:
#                 parent_nodes[node2] = node1
#             else:
#                 return edge
#
#
# sol = Solution()
# sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])


# class Solution(object):
#     def getAllElements(self, root1, root2):
#         """
#         :type root1: TreeNode
#         :type root2: TreeNode
#         :rtype: List[int]
#         """
#         result = []
#
#         def tree_rec(root1, root2, result):
#             if not root1 and not root2:
#                 return
#
#             tree_rec(None if not root1 else root1.left, None if not root2 else root2.left, result)
#
#             if root1 and root2:
#                 if root1.val < root2.val:
#                     result.append(root1.val)
#                     result.append(root2.val)
#                 else:
#                     result.append(root2.val)
#                     result.append(root1.val)
#             else:
#                 if root1:
#                     result.append(root1.val)
#                 else:
#                     result.append(root2.val)
#
#             tree_rec(None if not root1 else root1.right, None if not root2 else root2.right, result)
#
#         tree_rec(root1, root2, result)
#         return result


# from collections import deque
#
#
# class Solution(object):
#     def constructMaximumBinaryTree(self, nums):
#
#         def build_tree(nums, root_node):
#             if not nums:
#                 return None
#             root_node = TreeNode(max(nums))
#             root_node.left = build_tree(nums[:nums.index(max(nums))], root_node)
#             root_node.right = build_tree(nums[nums.index(max(nums)) + 1:], root_node)
#
#             return root_node
#
#         node = build_tree(nums, None)
#
#         tree_queue = deque()
#         tree_queue.append(node)
#         result = []
#
#         while tree_queue:
#             popped_node = tree_queue.popleft()
#             result.append(popped_node)
#             if popped_node.left != None and popped_node.right != None:
#                 tree_queue.append(popped_node.left)
#                 tree_queue.append(popped_node.right)
#
#         return result


# class Solution(object):
#     def findDuplicate(self, nums):
#         k = None
#
#         for i in range(len(nums)):
#             k = nums[i]
#
#             for j in range(i+1, len(nums)):
#                 if nums[j] == k:
#                     return k
#
#
# sol = Solution()
# print(sol.findDuplicate([3,1,3,4,2]))


# class Solution(object):
#     def maxArea(self, height):
#         container_volume = 0
#
#         for i in range(len(height) - 1):
#             for j in range(len(height)):
#                 lowest_height = min(height[i], height[j])
#
#                 container_vol = (j - i) * lowest_height
#
#                 container_volume = container_vol if container_vol > container_volume else container_volume
#
#         return container_volume
#
#
# sol = Solution()
# print(sol.maxArea([1,1]))


# class Solution(object):
#     def topKFrequent(self, nums, k):
#
#         if len(nums) == 1 and k == 1:
#             return nums
#
#         dict1 = dict()
#         dict2 = dict()
#         result = list()
#
#         for i in nums:
#             if i not in dict1:
#                 dict1[i] = 1
#             else:
#                 dict1[i] += 1
#
#         for key in dict1:
#             dict2[dict1[key]] = key
#
#         dict2_list = list(key for key in dict2)
#
#         dict2_list.sort(reverse=1)
#
#         print(dict1)
#         print(dict2)
#         print(dict2_list)
#         for i in range(k):
#             result.append(dict2[dict2_list[i]])
#
#         return result
#
# sol = Solution()
# print(sol.topKFrequent([1,1,1,2,2,3],2))


# class Solution(object):
#     def majorityElement(self, nums):
#         k = len(nums)//2
#         dict1 = {}
#
#         for num in nums:
#             if num not in dict1:
#                 dict1[num] = 1
#             else:
#                 if dict1[num] == k:
#                     return num
#                 else:
#                     dict1[num] += 1
#
#         print(dict1, k)
#
#
# sol = Solution()
# print(sol.majorityElement([2,2,1,1,1,2,2]))
import string


# class Solution(object):
#     def titleToNumber(self, columnTitle):
#         alpha = list(string.ascii_uppercase)
#         alpha.insert(0, 0)
#         total = 0
#         p = 0
#
#         if len(columnTitle) == 1:
#             return alpha.index(columnTitle[-1])
#
#         else:
#             total = alpha.index(columnTitle[-1])
#             p = 1
#
#             for i in range(len(columnTitle) - 2, -1, -1):
#                 total += pow(26, p) * alpha.index(columnTitle[i])
#                 p += 1
#
#         return total
#
#
# sol = Solution()
# print(sol.titleToNumber("ZY"))



# class Solution(object):
#     def __init__(self):
#         self.total_step = 0
#         self.step_list = [1,2]
#
#     def climbStairs(self, n):
#         if n == 0:
#             self.total_step += 1
#             return
#
#         for i in range(len(self.step_list)):
#             if n - self.step_list[i] >= 0:
#                 self.climbStairs(n - self.step_list[i])
#
#         return self.total_step
#
# sol = Solution()
# print(sol.climbStairs(3))


# class Solution(object):
#     def letterCombinations(self, digits):
#         phone_dict = {"2": ["a","b","c"], "3": ["d","e","f"]}
#         result = []
#         if len(digits) == 0:
#             return result
#         if len(digits) == 1:
#             for i in phone_dict[digits]:
#                 result.append(i)
#             return result

from collections import deque

# class Solution(object):
#     def canFinish(self, numCourses, prerequisites):
#         directional_graph_dict = dict()
#         visited_nodes = []
#         for preq in prerequisites:
#             if preq[1] not in directional_graph_dict:
#                 directional_graph_dict[preq[1]] = []
#
#             directional_graph_dict[preq[1]].append(preq[0])
#         queue = deque()
#         queue.append(0)
#         while queue:
#             print(queue)
#             popped_node = queue.pop()
#             visited_nodes.append(popped_node)
#             if popped_node in directional_graph_dict:
#                 for neighbour in directional_graph_dict[popped_node]:
#                     if neighbour in visited_nodes:
#                         return False
#                     queue.append(neighbour)
#
#         return True
#
#
#
# sol = Solution()
# print(sol.canFinish(2, [[1,0],[0,1]]))

# class Solution(object):
#     def generate(self, numRows):
#         result = []
#         for i in range(1, numRows+1):
#             list1 = [1] * i
#             if i == 1 or i == 2:
#                 result.append(list1)
#             else:
#                 for i in range(1, len(list1)-1):
#                     last_row = result[-1]
#                     list1[i] = last_row[i] + last_row[i-1]
#
#                 result.append(list1)
#
#         return result
#
#
# sol = Solution()
# print(sol.generate(5))





















