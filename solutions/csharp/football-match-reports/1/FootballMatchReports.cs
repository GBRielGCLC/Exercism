public static class PlayAnalyzer
{
    public static string AnalyzeOnField(int shirtNum)
    {
        switch (shirtNum)
        {
            case 1:
                return "goalie";
            case 2:
                return "left back";
            case 3:
            case 4:
                return "center back";
            case 5:
                return "right back";
            case 6:
            case 7:
            case 8:
                return "midfielder";
            case 10:
                return "striker";
            case 11:
                return "right wing";

            default:
                return "UNKNOWN";
        }
    }

    public static string AnalyzeOffField(object report)
    {
        switch (report)
        {
            case int integerReport:
                return $"There are {integerReport} supporters at the match.";
            case string stringReport:
                return stringReport;
            case Foul foulReport:
                return "The referee deemed a foul.";
            case Injury injuryReport:
                return $"Oh no! {injuryReport.GetDescription()} Medics are on the field.";
            case Incident incidentReport:
                return incidentReport.GetDescription();
            case Manager managerReport:
                string team = managerReport.Club == null ? "" : $" ({managerReport.Club})";
                return $"{managerReport.Name}{team}";

            default:
                return "";
        }
    }
}