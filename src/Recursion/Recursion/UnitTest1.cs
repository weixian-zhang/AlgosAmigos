namespace Recursion;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        //var node = TestLocalVariableRecursion(0);

        //var r = TestLocalVariableRecursion2(3);

        // var inputNode = new Node(1);
        // inputNode.Left = new Node(2);
        // inputNode.Left.Left = new Node(2);
        // inputNode.Left.Left.Left = new Node(2);
        // inputNode.Left.Left.Left.Left = new Node(2);
        // var r3 = TestLocalVariableRecursionAddition(inputNode);

        //var r4 = RecursionPersonInLine(1);

        int r4 = Sum_Recursion(0, 3);
    }

    private int Sum_Recursion(int callnum, int n)
    {
        int total, newnum = 0;

        callnum++;

        if(n == 1)
            return total = 1;

        newnum = n - 1;
        total = n + Sum_Recursion(callnum, newnum);

        return total;
    }


    private Node TestLocalVariableRecursion(int start)
    {
        Node root = null;

        if(start < 5)
        {
            root = new Node(start);

            root.Left = TestLocalVariableRecursion(start + 1);

            root.Right = TestLocalVariableRecursion(start + 2);
        }
        
        return new Node(100);
    }
    

    private Person RecursionPersonInLine(int x)
    {
       Person person = null;

        if(x <= 5)
        {
            person = new Person(x);
            person.NextInLine = RecursionPersonInLine(x + 1);
        }

        return person;
    }

    private int TestLocalVariableRecursionAddition(Node node)
    {
        if(node.Left == null)
        {
            return 1;
        }
        return 1 + TestLocalVariableRecursionAddition(node.Left);
    }
}

public class Person
    {
        public Person(int queueNumber) {QueueNumber = queueNumber;}
        public Person NextInLine { get; set; }
        public int QueueNumber { get; set; }
    }

public class Node
{
    public Node(int value)
    {
        Value = value;
    }
    public int Value { get; set; }
    public Node Left { get; set; }
    public Node Right { get; set; }
}