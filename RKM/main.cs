using System;

class main
{
    public static String Encrypt(String key, String message)
    {
        // Create Variables
        String fin = "";
        int i = 0;
        int salt = 0;

        // Get salt to make a single character change in key affect the entire message
        foreach (Char l in key) 
        {
            salt += (int)l;
        }

        //Loop through each letter in the message
        foreach (Char l in message)
        {
            int keyi = key[i % key.Length]; // Get character in key by index

            /*  
                Multiply intiger representation of the 
                current character in the message 
                by the intiger representation of the 
                current character in the key, 
                and add x for spliting
            */
            fin += (int)l * (int)keyi * salt + "x";
            i++; // Increase index
        }

        return fin[..^1]; // remove trailing x
    }

    public static String Decrypt(String key, String EncryptedMessage)
    {
        // Create Variables
        String fin = "";
        int i = 0;
        int salt = 0;

        // Get salt
        foreach (Char l in key)
        {
            salt += (int)l;
        }

        // Split encrypted message into chunks
        String[] mes = EncryptedMessage.Split("x");

        // loop through each chunk
        foreach (String l in mes)
        {
            // same as encryption, just dividing instead of multiplying. 
            int keyi = key[i % key.Length];
            fin += (char)(int)(int.Parse(l) / keyi / salt);
            i++;
        }

        return fin;
    }
}