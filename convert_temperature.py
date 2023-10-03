class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        convertions = []
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32
        convertions.append(kelvin)
        convertions.append(fahrenheit)
        return convertions


# link to question, https://leetcode.com/problems/convert-the-temperature/