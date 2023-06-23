Node root = new Node(0); //first
root.Append(1); //first-left
root.Append(2); //firtst-right
root.Append(3); //second-left
root.Append(4); //second-right
root.Append(5); //third-left

void traverseTree(Node root)
{
    if(root == null)
    {
        return;
    }

    Console.WriteLine(root.value);

    traverseTree(root.left);
    traverseTree(root.right);
}

Node searchVal(Node root, int val)
{
    if(root == null)
    {
        return null;
    }

    if(root.value == val)
    {
        return root;
    }

    Node left = searchVal(root.left, val);
    Node right = searchVal(root.right, val);

    if(left != null)
    {
        return left;
    }

    if(right != null)
    {
        return right;
    }

    return null;
}

Console.WriteLine("starting...");

traverseTree(root);

Console.WriteLine("searching...");
Node index = searchVal(root, 3);
Console.WriteLine(index.value);

Console.WriteLine("LinkedList starting...");

LinkedList list = new Linked(0);
list.Append(1);
list.Append(2);
list.Append(3);
Console.WriteLine(list.Find(2));
list.Remove(2);
Console.WriteLine("new " + list.Find(2));