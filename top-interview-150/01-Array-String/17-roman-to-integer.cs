public class Solution {
    public int RomanToInt(string s) {
        int Numeral = 0;
        char[] letters = s.ToCharArray();
        Dictionary<char, int> RomanNumerals = new Dictionary<char, int>
        {
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }
        };
        
        for(int i = 0; i < letters.Length; i++)
        {
            if(i == letters.Length - 1)
            {
                Numeral += RomanNumerals[letters[i]];
            }
            else{
                if(RomanNumerals[letters[i]] < RomanNumerals[letters[i+1]])
                {
                    Numeral += RomanNumerals[letters[i+1]] - RomanNumerals[letters[i]];
                    i++;
                }
                else
                {
                    Numeral += RomanNumerals[letters[i]];
                }
            }
        }
        return Numeral;
    }
}