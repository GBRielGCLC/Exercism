public static class BottleSong
{
    public static string NumberToWord(int number, bool firstUpper = false)
    {
        var words = new[] { "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten" };

        string word = words[number];

        if (firstUpper)
        {
            word = char.ToUpper(word[0]) + word.Substring(1);
        }

        return word;
    }

    public static string PluralWord(int number) => number == 1 ? "" : "s";

    public static IEnumerable<string> Recite(int startBottles, int takeDown)
    {
        int lastBottle = startBottles - (takeDown - 1);

        List<string> poem = [];

        for (var i = startBottles; i >= lastBottle; i--)
        {
            poem.Add(
                $"{NumberToWord(i, true)} green bottle{PluralWord(i)} hanging on the wall,"
            );
            poem.Add(
                $"{NumberToWord(i, true)} green bottle{PluralWord(i)} hanging on the wall,"
            );

            poem.Add(
                $"And if one green bottle should accidentally fall,"
            );

            string remainingBottles = i == 1 ? "no" : $"{NumberToWord(i - 1)}";
            poem.Add(
                $"There'll be {remainingBottles} green bottle{PluralWord(i - 1)} hanging on the wall."
            );
            if (lastBottle != i)
            {
                poem.Add("");
            }
        }

        return poem.ToArray();
    }
}