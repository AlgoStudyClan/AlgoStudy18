class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        # for loof 2ea -> for for? O(n^2)
        # 가능한 두 수의 조합을 찾고 그 합이 target과 같은 경우 index를 return
        for i in range(n):
            for j in range(i + 1, n):  # i 다음부터 n까지
                if nums[i] + nums[j] == target:  # i번째 index의 숫자와 j번째 index의 숫자의 합이 target과 같으면
                    return [i, j]  # i, j return
        return []

# python dictinary vs for for? O(n^2)
# 해쉬개념 -- k in lisk? k라는 값이 list 안에 있냐
# k in dict.keys()? --> O(1) // 메모리 사용 증가
# 일반적으로 k in list? --> O(n) // 메모리 사용 감소



