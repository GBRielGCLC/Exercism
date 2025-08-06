public static class PhoneNumber
{
    public static (bool IsNewYork, bool IsFake, string LocalNumber) Analyze(string phoneNumber)
    {
        var splitedPhoneNumber = phoneNumber.Split('-');

        bool IsNewYork = splitedPhoneNumber[0] == "212";
        bool IsFake = splitedPhoneNumber[1] == "555";
        string LocalNumber = splitedPhoneNumber[2];

        return (IsNewYork, IsFake, LocalNumber);
    }

    public static bool IsFake((bool IsNewYork, bool IsFake, string LocalNumber) phoneNumberInfo)
    {
        return phoneNumberInfo.IsFake;
    }
}
