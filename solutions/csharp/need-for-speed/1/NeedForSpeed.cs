class RemoteControlCar(int speed, int batteryDrain)
{
    public int meters = 0;
    public int battery = 100;
    public int speed = speed;
    public int batteryDrain = batteryDrain;

    public bool BatteryDrained() => battery <= 0 || batteryDrain > battery;

    public int DistanceDriven() => meters;

    public void Drive()
    {
        if (!BatteryDrained())
        {
            meters += speed;
            battery -= batteryDrain;
        }
    }

    public static RemoteControlCar Nitro() => new RemoteControlCar(50, 4);
}

class RaceTrack
{
    public int distance;

    public RaceTrack(int distance)
    {
        this.distance = distance;
    }

    public bool TryFinishTrack(RemoteControlCar car)
    {
        double drivenTimes = car.battery / car.batteryDrain;
        double distanceDriven = drivenTimes * car.speed;

        return distanceDriven >= distance;
    }
}
