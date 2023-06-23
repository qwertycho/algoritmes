class Node
{
    public int value;
    public Node? left;
    public Node? right;

    public Node(int newVal)
    {
            value = newVal;
    }

    public void Append(int newVal)
    {
        if(newVal > value)
        {
            if(right == null)
            {
                right = new Node(newVal);
                return;
            }
            right.Append(newVal);
        } else if(newVal < value)
        {
            if(left == null)
            {
                left = new Node(newVal);
                return;
            }
            left.Append(newVal);
        } else if(newVal == value)
        {
            throw new Exception(newVal + " bestaat al!");
        }
    }
// get self for recursive traversal
    public void Traverse(Node node = null) 
    {
        if(node == null)
        {
            node = this;
        }

        if(node.left != null)
        {
            Console.WriteLine("left: " + node.left.value);
            node.Traverse(node.left);
        }
        if(node.right != null)
        {
            Console.WriteLine("         right: " + node.right.value);
            node.Traverse(node.right);
        }
        if(node.left == null && node.right == null)
        {
            Console.WriteLine("end of branch");
        }
    }

    public int Find(int findval)
    {
        if(findval == value)
        {
            return value;
        }
        if(findval > value)
        {
            if(right == null)
            {
                throw new Exception("not found");
            }
            return right.Find(findval);
        } else if(findval < value)
        {
            if(left == null)
            {
                throw new Exception("not found");
            }
            return left.Find(findval);
        }
        throw new Exception("not found");
    }
}