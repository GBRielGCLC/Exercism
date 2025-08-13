public static class Dominoes
{
    public static bool CanChain(IEnumerable<(int, int)> dominoes)
    {
        var list = dominoes.ToList();
        if (list.Count < 2) return list.Count == 0 || list[0].Item1 == list[0].Item2;

        // Tenta começar a cadeia com cada peça possível
        for (int i = 0; i < list.Count; i++)
        {
            var remaining = list.ToList();
            var start = remaining[i];
            remaining.RemoveAt(i);

            if (SearchChain(start.Item1, start.Item2, remaining, start.Item1))
                return true;

            if (SearchChain(start.Item2, start.Item1, remaining, start.Item2))
                return true;
        }

        return false;
    }

    private static bool SearchChain(int start, int current, List<(int, int)> remaining, int target)
    {
        if (remaining.Count == 0)
            return current == target; // precisa fechar o ciclo

        for (int i = 0; i < remaining.Count; i++)
        {
            var (a, b) = remaining[i];
            if (a == current || b == current)
            {
                var next = (a == current) ? b : a;
                var nextRemaining = remaining.ToList();
                nextRemaining.RemoveAt(i);
                if (SearchChain(start, next, nextRemaining, target))
                    return true;
            }
        }
        return false;
    }
}