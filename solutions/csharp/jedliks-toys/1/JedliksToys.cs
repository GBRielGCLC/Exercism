class RemoteControlCar
{
    public int meters = 0;
    public int battery = 100;

    public static RemoteControlCar Buy() => new RemoteControlCar();

    public string DistanceDisplay() => $"Driven {meters} meters";

    public string BatteryDisplay()
    {
        if (battery == 0)
        {
            return "Battery empty";
        }

        return $"Battery at {battery}%";
    }

    public void Drive()
    {
        if (battery > 0)
        {
            meters += 20;
            battery -= 1;
        }
    }
}
