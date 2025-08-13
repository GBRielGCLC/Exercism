public static class NucleotideCount
{
    public static IDictionary<char, int> Count(string sequence)
    {
        char[] chars = sequence.ToCharArray();

        if (chars.Any(c => c != 'A' && c != 'C' && c != 'G' && c != 'T')) throw new ArgumentException();

        Dictionary<char, int> dict = new Dictionary<char, int>
        {
            ['A'] = 0,
            ['C'] = 0,
            ['G'] = 0,
            ['T'] = 0
        };
        
        foreach (char c in chars)
        {
            dict[c] += 1;
        }
        return dict;
    }
}