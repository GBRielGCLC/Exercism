public static class SimpleCalculator
{
    public static string Calculate(int operand1, int operand2, string? operation)
    {
        if (operation == null)
        {
            throw new ArgumentNullException("Division by zero is not allowed");
        }

        if (operation == "")
        {
            throw new ArgumentException("Invalid operation");            
        }

        if (operation != "+" && operation != "*" && operation != "/")
        {
            throw new ArgumentOutOfRangeException("Invalid operation");
        }

        double result = 0;
        switch (operation)
        {
            case "+":
                result = operand1 + operand2;
                break;
            case "*":
                result = operand1 * operand2;
                break;
            case "/":
                if (operand2 == 0)
                {
                    return "Division by zero is not allowed.";
                }

                result = operand1 / operand2;
                break;
        }

        return $"{operand1} {operation} {operand2} = {result}";
    }
}