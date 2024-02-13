using IdMinter;

Console.WriteLine("Identifiable.Generate()");
for (int i = 0; i < 10; i++)
{
    Console.WriteLine(Identifiable.Generate());
}
Console.WriteLine();

Console.WriteLine("Identifiable.Generate(length:16)");
for (int i = 0; i < 10; i++)
{
    Console.WriteLine(Identifiable.Generate(length: 16));
}
Console.WriteLine();

Console.WriteLine("Identifiable.Generate(letterFirst:false)");
for (int i = 0; i < 10; i++)
{
    Console.WriteLine(Identifiable.Generate(letterFirst: false));
}
Console.WriteLine();

