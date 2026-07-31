class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        sorted_freqs = sorted(counts.values(), reverse=True)
        total_pushes = 0

        for index, freq in enumerate(sorted_freqs):
            presses_needed = (index // 8) + 1
            total_pushes += freq * presses_needed
        return total_pushes    
        