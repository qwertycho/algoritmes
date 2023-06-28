class Stack{
    private Node head;

    public Stack(string data = null)
    {
        if(data != null){
            head = new Node(data);
        }
    }

    public void Append(string data)
    {
        if(head == null){
            head = new Node(data);
        }else{
            head = new Node(data, head);
        }
    }

    public void DoWork()
    {
        if(head != null)
        {
            head.DoWork();
            Pop();
        }
    }

    public void Pop(int index = -1){
        if(head != null){
            if(index == -1 || index == 0)
            {
                head = head.GetNext();
            } else {
                head.Pop(index);
            }
        }
    }
}

class Node{
    private string data;

    private Node next;

    public Node(string data, Node next = null)
    {
        this.data = data;
        if(next != null)
        {
            this.next = next;
        }
    }

    public void DoWork(){
        Console.WriteLine("Doing work for " + data);
    }

    public Node GetNext()
    {
        return next;
    }

    public void Pop(int index)
    {
        index--;
        if(index == 0)
        {
            next = next.GetNext();
        }
    }
}