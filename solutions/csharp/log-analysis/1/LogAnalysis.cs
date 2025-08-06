public static class LogAnalysis
{
    // Retorna a substring depois do delimitador
    public static string SubstringAfter(this string str, string delimiter)
    {
        int index = str.IndexOf(delimiter);
        if (index == -1) return "";
        return str.Substring(index + delimiter.Length);
    }

    // Retorna a substring entre dois delimitadores
    public static string SubstringBetween(this string str, string start, string end)
    {
        int startIndex = str.IndexOf(start);
        if (startIndex == -1) return "";
        startIndex += start.Length;

        int endIndex = str.IndexOf(end, startIndex);
        if (endIndex == -1) return "";

        return str.Substring(startIndex, endIndex - startIndex);
    }

    // Retorna a mensagem do log (após ":")
    public static string Message(this string str)
    {
        return str.SubstringAfter(": ").Trim();
    }

    // Retorna o nível do log (entre "[", "]", e em minúsculas)
    public static string LogLevel(this string str)
    {
        return str.SubstringBetween("[", "]");
    }
}