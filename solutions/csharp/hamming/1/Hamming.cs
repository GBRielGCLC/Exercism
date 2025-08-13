public static class Hamming
{
    public static int Distance(string firstStrand, string secondStrand)
    {
        if (firstStrand.Length != secondStrand.Length) throw new ArgumentException();

        int count = 0;
        int i = 0;
        foreach (char letter in firstStrand)
        {
            if (firstStrand[i] != secondStrand[i]) count++;
            i++;
        }

        return count;
    }
}