Node root = new Node(10);
root.Append(5);
root.Append(15);

root.Append(20);
root.Append(16);
root.Append(6);
root.Append(77);
root.Append(66);
root.Append(7);
root.Append(8);

root.Traverse();
Console.WriteLine(root.Find(66));