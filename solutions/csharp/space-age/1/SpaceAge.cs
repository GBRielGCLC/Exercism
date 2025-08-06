public class SpaceAge
{
    private readonly int seconds;
    private const double secondsInYear = 31557600;

    public SpaceAge(int seconds)
    {
        this.seconds = seconds;
    }

    private double EarthYears => seconds / secondsInYear;

    public double OnEarth() => Math.Round(EarthYears, 2);
    public double OnMercury() => Math.Round(EarthYears / 0.2408467, 2);
    public double OnVenus() => Math.Round(EarthYears / 0.61519726, 2);
    public double OnMars() => Math.Round(EarthYears / 1.8808158, 2);
    public double OnJupiter() => Math.Round(EarthYears / 11.862615, 2);
    public double OnSaturn() => Math.Round(EarthYears / 29.447498, 2);
    public double OnUranus() => Math.Round(EarthYears / 84.016846, 2);
    public double OnNeptune() => Math.Round(EarthYears / 164.79132, 2);
}