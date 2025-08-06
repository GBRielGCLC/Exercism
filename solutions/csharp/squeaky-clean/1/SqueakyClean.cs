public static class Identifier
{
    public static char[] RemoveAtIndex(char[] array, List<int> index)
    {
        List<char> list = array.ToList();

        index.Reverse();

        foreach (int i in index)
        {
            list.RemoveAt(i);
        }

        return list.ToArray();
    }

    public static string Clean(string identifier)
    {
        string newIdentifier = "";

        // Start in -1 to count int the start of foreach
        int i = -1;

        foreach (char c in identifier)
        {
            i++;

            // Task 1
            if (c == ' ')
            {
                newIdentifier += '_';
                continue;
            }

            // Task 2
            if (char.IsControl(c))
            {
                newIdentifier += "CTRL";
                continue;
            }

            // Task 3 (CamelCase)
            if (i > 0 && identifier[i - 1] == '-')
            {
                newIdentifier += c.ToString().ToUpper();
                continue;
            }

            // Task 4 and 5
            bool isGreek = c >= '\u0370' && c <= '\u03FF' && c!='Ο';
            if (char.IsLetter(c) && !isGreek)
            {
                newIdentifier += c;
            }
        }

        return newIdentifier;
    }
}