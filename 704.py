# Binary Search
"""Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity."""
class Solution:
    def search(self, nums: List[int], target: int) -> 
        l = 0
        r = len(nums)-1
        while(l <= r):
            mid = (l+r) // 2 #amra akn a mid ber korar jnno (m=(r+l)//2) use korar kota kintu amra akn a (r-l)//2 use korci karon
            """mid = (left + right) // 2
যাইহোক, এটি সম্ভাব্যভাবে কিছু প্রোগ্রামিং ভাষায় একটি পূর্ণসংখ্যা ওভারফ্লো হতে পারে যখন এবং খুব বড়। উদাহরণস্বরূপ, যদি এবং বড় পূর্ণসংখ্যা হয়, তবে তাদের যোগফল () একটি পূর্ণসংখ্যা ধারণ করতে পারে এমন সর্বাধিক মান অতিক্রম করতে পারে, যার ফলে একটি উপচে পড়া প্রবাহ ঘটে। যদিও পাইথন বড় পূর্ণসংখ্যাগুলি সুন্দরভাবে পরিচালনা করে, অন্যান্য অনেক ভাষা (যেমন সি, সি ++, বা জাভা) পূর্ণসংখ্যার আকারের নির্দিষ্ট সীমা রয়েছে, তাই এই ওভারফ্লো ঝুঁকি সেই পরিবেশে একটি বাস্তব উদ্বেগ।


right - left: এটি এবং এর মধ্যে পরিসীমা। থেকে বিয়োগ করে, আমরা নিশ্চিত করি যে আমরা একটি ছোট সংখ্যা (পরিসরের দৈর্ঘ্য) নিয়ে কাজ করছি এবং এইভাবে ওভারফ্লো এড়াতে পারি।leftrightleftright
(right - left) // 2: এটি এবং এর মধ্যে বর্তমান পরিসরে "অর্ধেক পয়েন্ট" গণনা করে।leftright
left + (right - left) // 2: তারপরে আমরা অ্যারের সাপেক্ষে প্রকৃত মধ্যম সূচকটি পেতে এই অর্ধেক পয়েন্টে ফিরে যোগ করি।left
"""
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l= mid +1
            else:
                r = mid -1
        return -1