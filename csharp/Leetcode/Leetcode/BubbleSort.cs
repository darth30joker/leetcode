namespace Leetcode;

public static class BubbleSort
{
    public static int[] Sort(int[] array)
    {
        Console.WriteLine($"Start: {string.Join(",", array)}");
        
        for (int i = 0; i <= array.Length - 2; i++)
        {
            for (int j = 0; j <= array.Length - 2 - i; j++)
            {
                if (array[j] > array[j + 1])
                {
                    (array[j], array[j + 1]) = (array[j + 1], array[j]);
                }
            }
            
            Console.WriteLine($"After {i} round: {string.Join(",", array)}");
        }

        return array;
    }
}