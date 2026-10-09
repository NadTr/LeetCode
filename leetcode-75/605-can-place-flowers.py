class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        safeplaces = 0
        
        for f in range(len(flowerbed)):
            left = 0 if f == 0 or flowerbed[f-1] == 0 else 1
            right = 0 if f == len(flowerbed) - 1 or flowerbed[f+1] == 0 else 1
            if flowerbed[f] == 0 and left == 0 and right == 0:
                safeplaces += 1
                flowerbed[f] = 1
        return safeplaces >= n