// See https://aka.ms/new-console-template for more information
using System.Net.NetworkInformation;
using BFSN;


var graph1 = new Dictionary<int, List<int>>(){
            {0, new List<int>() {1,2} },
            {1, new List<int>() {0,2,3} },
            {2, new List<int>() {0,1,4} },
            {3, new List<int>() {1,4} },
            {4, new List<int>() {2, 3} },
        };


var bfs = new BFS();

//bfs.Traversal(graph, 0);

var result = bfs.FindShortestPath(graph1, 0, 4);

Console.WriteLine("done");


namespace BFSN
{

    public class BFSSearchResult {

        public BFSSearchResult(int distant, string path)
        {
            Distant = distant;
            Path = path;
        }

        public int Distant { get; set; }
        public string Path { get; set; } = "";
    }

    public class BFS {

        public int[] Traversal(Dictionary<int,List<int>> graph, int startNode)
        {
            var visited = new List<int>();
            var queue = new Queue<int>();

            int startKey = graph.Keys.FirstOrDefault(x => x == startNode);

            queue.Enqueue(startKey);

            while (queue.Count > 0) {
                int node = queue.Dequeue();

                visited.Add(node);

                var neighbours = graph[node];

                foreach (var n in neighbours) 
                {
                    if (visited.Contains(n)) { continue; }

                    queue.Append(n);
                }
            }

            return visited.ToArray();
        }

//https://www.youtube.com/watch?v=PQhMkmhYZjQ

        public BFSSearchResult FindShortestPath(Dictionary<int,List<int>> graph, int start, int end) {

            var visited = new List<int>();
            var queue = new Queue<int>();
            var parent = new Dictionary<int, int>();
            var level = new Dictionary<int, int>();

            foreach (var kv in graph) {
                level[kv.Key] = -1;
            }

            queue.Enqueue(start);
            visited.Add(start);
            level[start] = 0;
            
            while (queue.Count > 0) {

                int currentNode = queue.Dequeue();
                visited.Add(currentNode);

                foreach(int toVisitNode in graph[currentNode]) {

                    int originNode = currentNode;

                    if (visited.Contains(toVisitNode)) { continue ;}

                    visited.Add(toVisitNode);

                    parent.Add(toVisitNode, originNode);

                    level[toVisitNode] = level[originNode] + 1;

                    if (toVisitNode == end) {
                        int distant = level[toVisitNode];
                        string path = BacktrackToGetRouteToDestination(parent, end);
                        return new BFSSearchResult(distant, path);
                    }

                    queue.Enqueue(toVisitNode);
                }
            }

            return new BFSSearchResult(-1,"");
        }

        private string BacktrackToGetRouteToDestination(Dictionary<int,int> paths, int destination)
        {
            var result = new List<string>();

            string node = destination.ToString();

            result.Add(node);

            while (!string.IsNullOrEmpty(node)) {

                int nodeInt = Convert.ToInt32(node);

                if (paths.Keys.Contains(nodeInt)) {
                    node = paths[nodeInt].ToString();
                    result.Add(node);
                }
                else {
                    node = "";
                }
            }
            
            result.Reverse();
            
            return string.Join(",",result);
        }
    }
}











