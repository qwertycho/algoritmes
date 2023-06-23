class Node
{
    public int value;
    public Node  left;
    public Node right;

    public Node(int newVal)
    {
            value = newVal;
    }

    public void Append(int newVal)
    {
        if(left == null)
        {
            left = new Node(newVal);
            return;
        }

        if(right == null)
        {
            right = new Node(newVal);
            return;
        }

        if(left != null && right != null)
        {
            if(left.left == null || left.right == null)
            {
                left.Append(newVal);
                return;
            }

            if(right.left == null || right.right == null)
            {
                right.Append(newVal);
                return;
            }
        }
    }
}