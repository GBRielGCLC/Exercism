using System;

public class Robot
{
    private static Random random = new Random();
    private const string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private const int nameLength = 5;
    private string name;

    public Robot()
    {
        Reset();
    }

    public string Name
    {
        get { return name; }
        private set { name = value; }
    }

    public void Reset()
    {
        Name = GenerateName();
    }

    static HashSet<string> usedNames = new HashSet<string>();

    private string GenerateName()
    {
        string newName;
        do
        {
            // monta o nome (duas letras + três números)
            var letterPart = $"{letters[random.Next(letters.Length)]}{letters[random.Next(letters.Length)]}";
            var numberPart = $"{random.Next(0, 1000):D3}";
            newName = letterPart + numberPart;
        }
        while (!usedNames.Add(newName)); // só sai do loop se for único

        return newName;
    }
}
