static class Appointment
{
    public static DateTime Schedule(string appointmentDateDescription) => DateTime.Parse(appointmentDateDescription);

    public static bool HasPassed(DateTime appointmentDate) => appointmentDate < DateTime.Now;

    public static bool IsAfternoonAppointment(DateTime appointmentDate)
    {
        int hour = appointmentDate.Hour;

        return hour >= 12 && hour < 18;
    }

    public static string Description(DateTime appointmentDate)
    {
        string date = appointmentDate.ToString("M/d/yyyy");
        string time = appointmentDate.ToString("h:mm:ss");

        int hour = appointmentDate.TimeOfDay.Hours;

        return $"You have an appointment on {date} {time} {(hour >= 12 ? "PM" : "AM")}.";
    }

    public static DateTime AnniversaryDate() => new DateTime(DateTime.Now.Year, 9, 15);
}
