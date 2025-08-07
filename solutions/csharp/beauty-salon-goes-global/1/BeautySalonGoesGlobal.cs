using System.Globalization;

public enum Location
{
    NewYork,
    London,
    Paris
}

public enum AlertLevel
{
    Early,
    Standard,
    Late
}

public static class Appointment
{
    public static TimeZoneInfo GetTimeZoneInfoByLocation(Location location) => location switch
    {
        Location.NewYork => TimeZoneInfo.FindSystemTimeZoneById("Eastern Standard Time"),
        Location.London => TimeZoneInfo.FindSystemTimeZoneById("GMT Standard Time"),
        Location.Paris => TimeZoneInfo.FindSystemTimeZoneById("Central European Standard Time"),
        _ => throw new ArgumentException("Invalid location"),
    };
    public static CultureInfo GetCutureInfoByLocation(Location location) => location switch
    {
        Location.NewYork => new CultureInfo("en-US"),
        Location.London => new CultureInfo("en-GB"),
        Location.Paris => new CultureInfo("fr-FR"),
        _ => throw new ArgumentException("Invalid location"),
    };

    public static DateTime ShowLocalTime(DateTime dtUtc) => dtUtc.ToLocalTime();

    // TimeZoneInfo.ConvertTimeFromUtc(dtUtc, TimeZoneInfo.FindSystemTimeZoneById("America/New_York"))

    public static DateTime Schedule(string appointmentDateDescription, Location location)
    {
        DateTime localTime = DateTime.Parse(appointmentDateDescription);

        return TimeZoneInfo.ConvertTimeToUtc(localTime, GetTimeZoneInfoByLocation(location));
    }

    public static DateTime GetAlertTime(DateTime appointment, AlertLevel alertLevel) => alertLevel switch
    {
        AlertLevel.Early => appointment.AddDays(-1),
        AlertLevel.Standard => appointment.AddHours(-1).AddMinutes(-45),
        AlertLevel.Late => appointment.AddMinutes(-30),
        _ => appointment
    };

    public static bool HasDaylightSavingChanged(DateTime dt, Location location)
    {
        bool dayLighthSavingLastWeek = GetTimeZoneInfoByLocation(location).IsDaylightSavingTime(dt.AddDays(-7));
        bool dayLighthSaving = GetTimeZoneInfoByLocation(location).IsDaylightSavingTime(dt);

        return dayLighthSavingLastWeek != dayLighthSaving;
    }

    public static DateTime NormalizeDateTime(string dtStr, Location location)
    {
        try
        {
            return DateTime.Parse(dtStr, GetCutureInfoByLocation(location));
        }
        catch (FormatException)
        {
            return new DateTime(1, 1, 1, 0, 0, 0);
        }
    }
}