namespace DisjointSet_1;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        DisjointSet ds = new DisjointSet();
        ds.makeSet(1);
        ds.makeSet(2);
        ds.makeSet(3);
        ds.makeSet(4);
        ds.makeSet(5);
        ds.makeSet(6);
        ds.makeSet(7);

        ds.union(1, 2);
        ds.union(2, 3);
        // ds.union(4, 5);
        ds.union(6, 7);
        // ds.union(5, 6);
        //ds.union(3, 7);

        //Console.WriteLine(ds.findSet(1));
        Console.WriteLine(ds.findSet(2));
        Console.WriteLine(ds.findSet(3));
        // Console.WriteLine(ds.findSet(4));
        // Console.WriteLine(ds.findSet(5));
        Console.WriteLine(ds.findSet(6));
        Console.WriteLine(ds.findSet(7));
    }
}

  public class Node {
        public long id;
        public Node parent;
        public int rank;
    }

public class DisjointSet {

    private Dictionary<long, Node> map = new Dictionary<long, Node>();

    /**
     * Create a set with only one element.
     */
    public void makeSet(long id) {
        Node node = new Node();
        node.id = id;
        node.parent = node;
        node.rank = 0;
        map.Add(id, node);
    }

    /**
     * Combines two sets together to one.
     * Does union by rank
     *
     * @return true if id1 and id2 are in different set before union else false.
     */
    public bool union(long id1, long id2) {
        Node node1 = map[id1];
        Node node2 = map[id2];

        Node parent1 = findSet(node1);
        Node parent2 = findSet(node2);

        //same parent id means same set, return false because there is no disjoint set to union.
        //Already in same parent
        if (parent1.id == parent2.id) {
            return false;
        }

        //else whoever's rank is higher becomes parent of other
        if (parent1.rank < parent2.rank) {

            parent1.parent = parent2;
        }
        else if (parent1.rank > parent2.rank) {
            parent2.parent = parent1;
        
            //increment rank only if both sets have same rank
            // parent1.rank = (parent1.rank == parent2.rank) ? parent1.rank + 1 : parent1.rank;
            // parent2.parent = parent1;
        } else {
            parent2.parent = parent1;
            parent1.rank += 1;
        }

        return true;
    }

    /**
     * Finds the representative of this set
     */
    public long findSet(long id) {
        return findSet(map[id]).id;
    }

    /**
     * Find the representative recursively and does path
     * compression as well.
     */
    private Node findSet(Node node) {
        Node parent = node.parent;
        if (parent == node) {
            return parent;
        }
        node.parent = findSet(node.parent);
        return node.parent;
    }
}