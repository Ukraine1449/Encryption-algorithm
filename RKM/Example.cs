using System;

class Example
{
    static void Main(string[] args)
    {
        String key = "NzCeMijRlgGa";
        String Message = "Hello World!";

        String EncrptedMessage = main.Encrypt(key, Message);
            
        Console.WriteLine(EncrptedMessage);
        Console.WriteLine( main.Decrypt(key, EncrptedMessage) );
    }
}