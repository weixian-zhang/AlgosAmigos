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

    public void DnqueueHead(T data)
    {
        throw new System.NotImplementedException();
    }

    public void DnqueueTail(T data)
    {
        throw new System.NotImplementedException();
    }

    public void EnqueueHead(T data)
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
        throw new System.NotImplementedException();
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        throw new System.NotImplementedException();
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
}

public interface IDeque<T> : IEnumerable<T>
{
    public T PeekHead();
    public T PeekTail();
    public void EnqueueHead(T data);
    public void DnqueueHead(T data);
    public void EnqueueTail(T data);
    public void DnqueueTail(T data);

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

    public UnitTest1()
    {

    }

    [Theory]
    [InlineData(new int[] {1, 2, 3, 4, 5, 6})]
    public void Test_EnqueueHead(int[] nums)
    {
        foreach(int x in nums) {
            deque.EnqueueHead(x);
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
            deque.EnqueueHead(x);
        }

        deque.EnqueueTail(10);

        Assert.True(deque.PeekTail() == 10);

        Console.WriteLine(deque.ToString());
    }
}