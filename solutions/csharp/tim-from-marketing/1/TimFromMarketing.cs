static class Badge
{
    public static string Print(int? id, string name, string? department)
    {
        string idString = "";

        if (id != null)
        {
            idString = $"[{id}] - ";
        }

        if (department == null)
        {
            department = "OWNER";
        }
        else
        {
            department = department.ToUpper();
        }

        return $"{idString}{name} - {department}";
    }
}