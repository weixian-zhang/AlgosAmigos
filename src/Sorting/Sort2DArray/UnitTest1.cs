namespace Sort2DArray;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        int[,] list = {{13,18}, {14,16}, {9,10}};

        for (int i = 0; i < list.GetLength(0); i++)
        {
            for (int x = i + 1; x < list.GetLength(0); x++)
            {
                int endTime = list[i,1];

                int nextEndtime = list[x,1];

                if(nextEndtime < endTime) {
                    var temp0 = list[i,0];
                    var temp1 = list[i,1];

                    list[i,0] = list[x,0];
                    list[i,1] = list[x,1];

                     list[x,0] = temp0;
                     list[x,1] = temp1;

                }
            }
        }

        for (int i = 0; i < list.GetLength(0); i++)
        {
            int val1 = list[i,0];
            int val2 = list[i,1];
            Console.WriteLine($"{{{val1.ToString()},{val2.ToString()}}}");
        }
    }
}