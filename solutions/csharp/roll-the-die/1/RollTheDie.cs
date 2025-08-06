public class Player
{
    Random random = new Random();

    public int RollDie() => random.Next(1, 18);

    public double GenerateSpellStrength() => random.Next(0, 99) + random.NextDouble();
}
