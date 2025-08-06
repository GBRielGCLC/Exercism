public static class Gigasecond
{
    public static DateTime Add(DateTime moment)
    {
        moment = moment.AddSeconds(1000000000);
        return moment;
    }
}