# task 1
nums = [2, 7, 11, 15]
target = 9

def two_sum(nums, target):
    prev_map = {}
    for i in range(len(nums)):
        n = nums[i]
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []

print(two_sum(nums, target))


# task 2
s = "leetcode"

def first_uniq_char(s):
    count_map = {}
    for i in range(len(s)):
        char = s[i]
        if char in count_map:
            count_map[char] = count_map[char] + 1
        else:
            count_map[char] = 1
            
    for i in range(len(s)):
        if count_map[s[i]] == 1:
            return i
    return -1

print(first_uniq_char(s))


# task 3
s = "egg"
t = "add"

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    map_s_to_t = {}
    map_t_to_s = {}
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        else:
            map_s_to_t[char_s] = char_t
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
        else:
            map_t_to_s[char_t] = char_s
    return True

print(is_isomorphic(s, t))


# task 4
n = 19

def is_happy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        string_n = str(n)
        new_sum = 0
        for i in range(len(string_n)):
            digit = int(string_n[i])
            new_sum = new_sum + (digit * digit)
        n = new_sum
    return True

print(is_happy(n))


# task 5
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

def level_order(root):
    if not root:
        return []
    res = []
    queue = [root]
    while len(queue) > 0:
        level = []
        for i in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res

print(level_order(root))


# task 6
def max_depth(root):
    if not root:
        return 0
    left_side = max_depth(root.left)
    right_side = max_depth(root.right)
    if left_side > right_side:
        return left_side + 1
    else:
        return right_side + 1

print(max_depth(root))


# task 7
root_sym = TreeNode(1)
root_sym.left = TreeNode(2, TreeNode(3), TreeNode(4))
root_sym.right = TreeNode(2, TreeNode(4), TreeNode(3))

def is_symmetric(root):
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)
    
    return is_mirror(root, root)

print(is_symmetric(root_sym))


# task 8
root_seq = TreeNode(1)
root_seq.right = TreeNode(3)
root_seq.right.left = TreeNode(2)
root_seq.right.right = TreeNode(4)
root_seq.right.right.right = TreeNode(5)

def longest_consecutive(root):
    res = [0]
    def dfs(node, parent, cur_len):
        if not node:
            return
        if parent and node.val == parent.val + 1:
            cur_len = cur_len + 1
        else:
            cur_len = 1
        if cur_len > res[0]:
            res[0] = cur_len
        dfs(node.left, node, cur_len)
        dfs(node.right, node, cur_len)
        
    dfs(root, None, 0)
    return res[0]

print(longest_consecutive(root_seq))


# task 9
nums = [2, 0, 2, 1, 1, 0]

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low = low + 1
            mid = mid + 1
        elif nums[mid] == 1:
            mid = mid + 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high = high - 1
            
    return nums

print(sort_colors(nums))


# task 10
nums_quick = [5, 1, 1, 2, 0, 0]

def quick_sort(nums):
    def partition(low, high):
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] <= pivot:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    sort(0, len(nums) - 1)
    return nums

print(quick_sort(nums_quick))


# task 11
nums_merge = [5, 2, 3, 1]

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        L = nums[:mid]
        R = nums[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i = i + 1
            else:
                nums[k] = R[j]
                j = j + 1
            k = k + 1

        while i < len(L):
            nums[k] = L[i]
            i = i + 1
            k = k + 1

        while j < len(R):
            nums[k] = R[j]
            j = j + 1
            k = k + 1
    return nums

print(merge_sort(nums_merge))


# task 12
nums_heap = [5, 1, 1, 2, 0, 0]

def heap_sort(nums):
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and nums[i] < nums[l]:
            largest = l
        if r < n and nums[largest] < nums[r]:
            largest = r
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(n, largest)

    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(i, 0)
    return nums

print(heap_sort(nums_heap))