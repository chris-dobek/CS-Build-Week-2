import UIKit

func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
       var dict = [Int: Int]()

        for (i, num) in nums.enumerated() {
            if let lastIndex = dict[target - num] {
                return [lastIndex, i]
            }
            dict[num] = i
        }
        return []
}

print(twoSum([1,2,3,4], 7))
print("--------")
print(twoSum([6, 4, 3, 9, 10], 19))
print("--------")
print(twoSum([4, 7, 8, 9, 1], 20))

