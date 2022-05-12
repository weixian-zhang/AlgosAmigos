using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace CPPDeque;

public class DoubleEndedQueue<T> : IDeque<T>
{
    private Node<T> _head;
    private Node<T> _tail;

    // public Node<T> Head { 
    //     get { return _head; }
    //     private set{ _head = value; }
    // }
    // public Node<T> Tail { 
    //     get { return _tail; }
    //     private set{ _tail = value; }
    // }

    public T PeekHead()
    {
        if(_head == null)
            return default(T);

        return _head.Data;
    }

    public T PeekTail()
    {
        if(_tail == null)
            return default(T);

        return _tail.Data;
    }

    public void Dequeue()
    {
        if(_head != null) {
            
            var prev = _head.Prev;

            if(prev != null) {
                _head = prev;
                _head.Next = null;
            }
            else
                _head = null;
        }
    }

    

    public void DequeueTail()
    {
        if(_tail != null) {
            var next = _tail.Next;
            if(next != null) {
                _tail = next;
                _tail.Prev = null;
            }
            else
                _tail= null;
        }
    }

    public void Enqueue(T data)
    {
        var newNode = new Node<T>(data);

        if(_head == null) {
            _head = new Node<T>(data);
            _tail = _head;
            return;
        }

        var oldHead = _head;
        
        //set new node prev to current head
        newNode.Prev = _head;

        //set cureent head next to new node
        oldHead.Next = newNode;

        //current head = new node
        _head = newNode;

        SetTailNode();
    }

    public void EnqueueTail(T data)
    {
        var newNode = new Node<T>(data);

        if(_tail == null) {
            _tail = newNode;
            if(_head == null) {
                _head = _tail;
            }
            return;
        }

        var oldTail = _tail;

        //current tail = new node
        _tail = newNode;

        _tail.Next = oldTail;
    }

    public IEnumerator<T> GetEnumerator()
    {
        if(_head != null)
            yield return _head.Data;

        var prev = _head.Prev;
        while(prev != null) {
            
            yield return prev.Data;

            prev = prev.Prev;
        }
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }

    public string ToString()
    {
        var strBuilder = new StringBuilder();
        strBuilder.Append($"{_tail.Data.ToString()},");

        var next = _tail.Next;

        while(next != null)
        {
            strBuilder.Append($"{next.Data.ToString()},");

            next = next.Next;
        }

        return strBuilder.ToString();

    }

    private void SetTailNode()
    {
        var prev = _head.Prev;
        while(prev != null)
        {
            if(prev.Prev == null) {
                _tail = prev;
            }

            prev = prev.Prev;
        }
    }

    public void Dequeue(T data)
    {
        var node = Find(data);

        if(node == null)
            return;

        var prev = node.Prev;
        var next = node.Next;

        if(prev != null)
            prev.Next = next;

        if(next != null)
            next.Prev = prev;
    }

    public Node<T> Find(T data)
    {
        if(_head.Data.Equals(data))
            return _head;

        var prev = _head.Prev;

        while(prev != null) {
            if(prev.Data.Equals(data))
                return prev;

            prev = prev.Prev;
        }
        return null;
    }

    public IEnumerable<T> ReverseEnumerate()
    {
        if(_tail != null)
            yield return _tail.Data;

        var next = _tail.Next;

        while(next != null) {
            yield return next.Data;

            next = next.Next;
        }
    }
}

public interface IDeque<T> : IEnumerable<T>
{
    public T PeekHead();
    public T PeekTail();
    public void Enqueue(T data);
    public void Dequeue();
    public void Dequeue(T data);
    public void EnqueueTail(T data);
    public void DequeueTail();
    public Node<T> Find(T data);
    public IEnumerable<T> ReverseEnumerate();

    public string ToString();
}

public class Node<T>
{
    public T Data { get; set; }
    //implementing Circular LinkedList where Next ref Head node if this is Tail
    public Node<T>? Next { get; set; }
    public Node<T>? Prev { get; set; }

    public Node(T data)
    {
        Data = data;
    }
}

public class UnitTest1
{
    DoubleEndedQueue<int> deque = new DoubleEndedQueue<int>();

    [Theory]
    [InlineData(new int[] {1, 2, 3, 4, 5, 6})]
    public void Test_EnqueueHead(int[] nums)
    {
        foreach(int x in nums) {
            deque.Enqueue(x);
        }

        Assert.True(deque.PeekHead() == 6);

        Assert.True(deque.PeekTail() == 1);

        Console.WriteLine(deque.ToString());
    }

    [Theory]
    [InlineData(new int[] {1, 2, 3, 4, 5, 6})]
    public void Test_EnqueueTail(int[] nums)
    {
        foreach(int x in nums) {
            deque.Enqueue(x);
        }

        deque.EnqueueTail(10);

        Assert.True(deque.PeekTail() == 10);

        Console.WriteLine(deque.ToString());
    }

    [Theory]
    [InlineData(new int[] {1, 2, 3, 4, 5, 6})]
    public void Test_Enumerate(int[] nums)
    {
        foreach(int x in nums) {
            deque.Enqueue(x);
        }

        //iterate over deque
        foreach(int x in deque) {
            Console.WriteLine(x.ToString());
        }

    }

    [Theory]
    [InlineData(new int[] {1, 2, 3, 4, 5, 6})]
    public void Test_DequeueByHeadAndTail(int[] nums)
    {
        foreach(int x in nums) {
            deque.Enqueue(x);
        }

        //remove 6
        deque.Dequeue();
        //remove 5
        deque.Dequeue();
        //remove 1
        deque.DequeueTail();
        //remove 2
        deque.DequeueTail();
        //remove 3
        deque.DequeueTail();

        Assert.True(deque.PeekHead() == 4);

        Console.WriteLine(deque.ToString());
    }

    [Theory]
    [InlineData(new int[] {1, 2, 3, 4, 5, 6})]
    public void Test_DequeueByValue(int[] nums)
    {
        foreach(int x in nums) {
            deque.Enqueue(x);
        }

        //remove 2, 4 and 5 which is in the moddle
        deque.Dequeue(2);
        deque.Dequeue(4);
        deque.Dequeue(5);


        Console.WriteLine(deque.ToString());
    }

    [Theory]
    [InlineData(new int[] {1, 2, 3, 4, 5, 6})]
    public void Test_ReverseEnumerate(int[] nums)
    {
        foreach(int x in nums) {
            deque.Enqueue(x);
        }

        foreach(int x in deque) {
            Console.WriteLine(x);
        }

        foreach(int x in deque.ReverseEnumerate()) {
            Console.WriteLine(x);
        }
    }
}