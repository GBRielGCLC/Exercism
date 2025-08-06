public static class LogAnalysis
{
    public static string SubstringAfter(this string str, string delimiter)
    {
        int index = str.IndexOf(delimiter);
        if (index == -1) return "";
        return str.Substring(index + delimiter.Length);
    }

    public static string SubstringBetween(this string str, string start, string end)
    {
        int startIndex = str.IndexOf(start);
        if (startIndex == -1) return "";
        startIndex += start.Length;

        int endIndex = str.IndexOf(end, startIndex);
        if (endIndex == -1) return "";

        return str.Substring(startIndex, endIndex - startIndex);
    }

    public static string Message(this string str) => str.SubstringAfter(": ").Trim();

    public static string LogLevel(this string str) => str.SubstringBetween("[", "]");
}