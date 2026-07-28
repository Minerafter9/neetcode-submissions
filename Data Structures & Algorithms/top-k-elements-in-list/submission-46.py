class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)

        for i in nums:
            store[i] += 1
        
        return sorted(store, key=store.get, reverse=True)[:k]

        