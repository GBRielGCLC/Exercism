class Lasagna
{
    public int ExpectedMinutesInOven() => 40;

    public int RemainingMinutesInOven(int time) => ExpectedMinutesInOven() - time;

    public int PreparationTimeInMinutes(int layers) => layers * 2;

    public int ElapsedTimeInMinutes(int layers, int minutes) => minutes + PreparationTimeInMinutes(layers);
}
