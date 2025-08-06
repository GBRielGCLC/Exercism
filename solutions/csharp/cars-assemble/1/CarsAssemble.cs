static class AssemblyLine
{
    public static double SuccessRate(int speed)
    {
        if (speed == 0) return 0;

        if (speed >= 1 && speed <= 4) return 1;

        if (speed >= 5 && speed <= 8) return 0.90;

        if (speed == 9) return 0.80;

        if (speed == 10) return 0.77;

        return 0;
    }

    public static double ProductionRatePerHour(int speed) => speed * SuccessRate(speed) * 221;

    public static int WorkingItemsPerMinute(int speed) => (int)(ProductionRatePerHour(speed) / 60.0);
}
