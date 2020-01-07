# -*- coding: utf-8 -*-
# @Time    : 1/6/20 11:01 PM
# @Author  : Yippee Song
# @Software: PyCharm
'''
我们买了一些糖果 candies，打算把它们分给排好队的 n = num_people 个小朋友。

给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 n 颗糖果。

然后，我们再回到队伍的起点，给第一个小朋友 n + 1 颗糖果，第二个小朋友 n + 2 颗，依此类推，直到给最后一个小朋友 2 * n 颗糖果。

重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。注意，就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。

返回一个长度为 num_people、元素之和为 candies 的数组，以表示糖果的最终分发情况（即 ans[i] 表示第 i 个小朋友分到的糖果数）。

 

示例 1：

输入：candies = 7, num_people = 4
输出：[1,2,3,1]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0,0]。
第三次，ans[2] += 3，数组变为 [1,2,3,0]。
第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。
示例 2：

输入：candies = 10, num_people = 3
输出：[5,2,3]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0]。
第三次，ans[2] += 3，数组变为 [1,2,3]。
第四次，ans[0] += 4，最终数组变为 [5,2,3]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/distribute-candies-to-people
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """

        times = 0

        def timesTotal(times=0):
            return times * (times + 1) * num_people * num_people / 2 + (times + 1) * (num_people + 1) * num_people / 2

        while timesTotal(times) < candies:
            times += 1
        if times == 0:
            ans = [0 for i in xrange(num_people)]
            for i in xrange(num_people):
                ans[i] = i + 1
                candies -= ans[i]
                if candies < 0:
                    candies += ans[i]
                    ans[i] = candies
                    break
                if candies == 0:
                    break
        else:
            times -= 1
            ans = [(times * num_people * (times + 1)/2 + (times + 1) * i) for i in xrange(1, num_people + 1)]
            candies = candies - timesTotal(times)
            for i in xrange(num_people):
                append = (times + 1) * num_people + i + 1
                before = ans[i]
                ans[i] += append
                candies -= append
                if candies < 0:
                    candies += append
                    ans[i] = before + candies
                    break
                if candies == 0:
                    break
        return ans


if __name__ == "__main__":
    candies = 60
    people = 4
    print Solution().distributeCandies(candies, people)
