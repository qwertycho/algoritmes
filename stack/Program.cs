Console.WriteLine("starting program");

Stack stack = new Stack();
stack.Append("one");
stack.Append("two");
stack.Append("three");
stack.Append("four");

stack.DoWork(); //four
stack.Pop(1); // 0 = three, 1 = two
stack.DoWork(); // three
stack.DoWork(); //one
stack.DoWork(); //none