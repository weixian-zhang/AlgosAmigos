using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using Xunit;

namespace GraphBFS;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var graph = new Graph();

        graph.Add("John", new string[] {"Peter", "Robert"});

        graph.Add("Peter", new string[] {"Jane", "Albert", "John"});

        graph.Add("Jane", new string[] {"Kay", "Loonie", "Peter"});

        graph.Add("Albert", new string[] {"Frankie", "Peter"});

        graph.Add("Loonie", new string[] {"Robert", "Mary", "Jane"});

        graph.Add("Robert", new string[] {"Loonie", "John"});

        graph.Add("Kay", new string[] {"Jane"});

        graph.Add("Frankie", new string[] {"Albert", "Mary"});

        graph.Add("Mary", new string[] {"Loonie", "Frankie"});


        var result = graph.BreadthFirstSearch("John", "Kay");

        Console.WriteLine(string.Join(",", result.PathToFriends));
    }
}

public class Graph
{
   private Dictionary<string, Node[]> people = new Dictionary<string, Node[]>();
   private Hashtable distantTracker;
   private Hashtable previousNodeTracker;

   public void Add(string name, params string[] friends)
   {
       var node = new Node(name);

       var nodes = new List<Node>();

       foreach(string f in friends) {
           nodes.Add(new Node(f));
       }

       node.Friends = nodes;

       people.Add(node.Name, node.Friends.ToArray());
   }

   //shortest path
   //https://www.youtube.com/watch?v=oDqjPvD54Ss

   public BFSResult BreadthFirstSearch(string startFromPerson, string personToFind)
   {
       var nextToVisitQueue = new Queue<string>();
       var visited = new List<string>();
       var searchPath = new List<string>();

       distantTracker = CreateNodeDistantTracker(people);
       previousNodeTracker = CreatePreviousNodeTracker(people);

       nextToVisitQueue.Enqueue(startFromPerson);

       SetDistantInTrackerIfNotExist(startFromPerson, 0);

       int distant = 1;
       while(nextToVisitQueue.Count > 0) {

           //track prev node
           
           string currentPersonInSearch = nextToVisitQueue.Dequeue();
           
           if(currentPersonInSearch == personToFind) {
               searchPath.Add(currentPersonInSearch);
               return new BFSResult(true, searchPath);
           }

           if((int)distantTracker[currentPersonInSearch] != -1)
                continue;

           searchPath.Add(currentPersonInSearch);

           foreach(Node friend in people[currentPersonInSearch]) {

               int prevPersonDistant = CheckPreviousPersonDistant(currentPersonInSearch);

               string nameOfFriend = friend.Name;

               nextToVisitQueue.Enqueue(nameOfFriend);

               SetDistantInTrackerIfNotExist(nameOfFriend, prevPersonDistant + 1);
           }
           distant++;
       }

       return new BFSResult(false);
   }

    #region Track distant between nodes

   private Hashtable CreateNodeDistantTracker(Dictionary<string, Node[]> people)
   {
       var distantTracker = new Hashtable();
       foreach(var k in people.Keys)
       {
           distantTracker[k] = -1;
       }

       return distantTracker;
   }

   private void SetDistantInTrackerIfNotExist(string person, int distant)
   {
       int currDist = (int)distantTracker[person];

       if(currDist == -1) {
           distantTracker[person] = distant;
       }
   }

   private int CheckPreviousPersonDistant(string person)
   {
       int distant = (int)distantTracker[person];
       return distant;
   }

   #endregion

   #region Track previous path
   
   private Hashtable CreatePreviousNodeTracker(Dictionary<string, Node[]> people)
   {
       var previousNodeTracker = new Hashtable();
       foreach(var k in people.Keys)
       {
           distantTracker[k] = "";
       }

       return distantTracker;
   }

}

public class Node 
{
    public string Name { get; set; } = "";
    public List<Node> Friends { get; set; } = new List<Node>();

    public Node(string name)
    {
        Name = name;
    }
}

public class BFSResult
{
    public bool Found { get; set; }
    public int NumberOfStepsToDestination { get; set; } = 0;
    public List<string> PathToFriends { get; set; } = new List<string>();

    public BFSResult(bool found) {
        Found = found;
    }

    public BFSResult(bool found, List<string> pathToFriends) {
        Found = found;
        PathToFriends = pathToFriends;
    }
}