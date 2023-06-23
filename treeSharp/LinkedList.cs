public class Linked : LinkedList
{
    public int? val;
    public Linked? next;

    public Linked(int newVal)
    {
        val = newVal;
        next = null;
    }

    public void Append(int newVal)
    {
        if (val == null)
        {
            val = newVal;
            return;
        }
        if (next != null)
        {
            next.Append(newVal);
            return;
        }

        next = new Linked(newVal);
    }

    public int Find(int toFInd)
    {
        if (val == toFInd)
        {
            return 0;
        }

        if (next != null)
        {
            int index = next.Find(toFInd);
            if (index != -1)
            {
                return index + 1;
            }
        }
        return -1;
    }

    public void Remove(int toRemove)
    {
        int index = Find(toRemove);
        if (index != -1)
        {
            if (index > 0)
            {
                if (index == 1)
                {
                    if (next.next != null)
                    {
                        next = next.next;
                        return;
                    }
                    else
                    {
                        next = null;
                        return;
                    }
                }
                else if (index == 0)
                {
                    Console.WriteLine("0");
                    val = null;
                    return;
                }
                else
                {
                    next.Remove(toRemove);
                    return;
                }
            }
        }
    }
}

interface LinkedList
{
    public void Append(int newVal);
    public int Find(int find);
    public void Remove(int toRemove);
}