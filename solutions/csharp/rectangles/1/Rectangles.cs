public static class Rectangles
{
    public static int Count(string[] rows)
    {
        int height = rows.Length;
        int count = 0;

        for (int r1 = 0; r1 < height; r1++)
        {
            var plusPositions = GetPlusPositions(rows[r1]);

            for (int i = 0; i < plusPositions.Count; i++)
            for (int j = i + 1; j < plusPositions.Count; j++)
            {
                int c1 = plusPositions[i], c2 = plusPositions[j];

                // ✅ Verifica se o topo entre c1 e c2 é válido
                if (!HorizontalOk(rows[r1], c1, c2))
                    continue;

                for (int r2 = r1 + 1; r2 < height; r2++)
                {
                    if (IsPlus(rows, r2, c1) && IsPlus(rows, r2, c2) &&
                        HorizontalOk(rows[r2], c1, c2) &&
                        VerticalOk(rows, r1, r2, c1) &&
                        VerticalOk(rows, r1, r2, c2))
                    {
                        count++;
                    }
                }
            }
        }

        return count;
    }

    private static List<int> GetPlusPositions(string row)
    {
        var result = new List<int>();
        for (int i = 0; i < row.Length; i++)
            if (row[i] == '+')
                result.Add(i);
        return result;
    }

    private static bool IsPlus(string[] rows, int r, int c) =>
        c < rows[r].Length && rows[r][c] == '+';

    private static bool HorizontalOk(string row, int c1, int c2)
    {
        if (c2 >= row.Length) return false;
        for (int c = c1 + 1; c < c2; c++)
            if (row[c] != '-' && row[c] != '+') return false;
        return true;
    }

    private static bool VerticalOk(string[] rows, int r1, int r2, int col)
    {
        for (int r = r1 + 1; r < r2; r++)
        {
            if (col >= rows[r].Length) return false;
            char ch = rows[r][col];
            if (ch != '|' && ch != '+') return false;
        }
        return true;
    }
}