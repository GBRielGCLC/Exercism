static class LogLine
{
    public static string GetMessage(string logLine) => logLine.Substring(logLine.IndexOf(':') + 1).Trim();

    public static string Message(string logLine) => GetMessage(logLine);

    public static string LogLevel(string logLine)
    {
        int startIndex = logLine.IndexOf('[');
        int endIndex = logLine.IndexOf(']');
        return logLine.Substring(startIndex + 1, endIndex - 1).ToLower();
    }

    public static string Reformat(string logLine)
    {
        string type = LogLevel(logLine);
        string message = GetMessage(logLine);
        return $"{message} ({type})";
    }

}