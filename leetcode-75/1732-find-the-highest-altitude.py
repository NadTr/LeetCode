class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_altitude = altitude = 0

        for i in range(len(gain)):
            altitude += gain[i]
            max_altitude = max(altitude, max_altitude)
            
        return max_altitude