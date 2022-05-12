using Xunit;
using System;
using System.Linq;
using System.Collections;
using System.Text;

namespace Cryptography_ROT13;

public class CryptographyROT13
{
    //Rot number is the number in letters to replace
    public string Decipher(string textToDecode, int rotNumber)
    {
        char startA = 'a';
        
        int startNumSmallA = (int)startA; // = a
        
        int endNum = startNumSmallA + 26; // = z

        char startBigA = 'A';
        int startNumBigA = (int)startBigA; // = A
        int endNumBigZ = startNumBigA + 26;
        
        var smallLetters = new Hashtable();
        var bigLetters = new Hashtable();
        var result = new StringBuilder();

        //populate hashtable a-z
        foreach(int charIndex in Enumerable.Range(0, 26)) {
            //a = 97, b = 97 + 1, ...
            int newCharNum = startNumSmallA + charIndex;
            smallLetters.Add(newCharNum, (char)newCharNum);
        }

        foreach(int charIndex in Enumerable.Range(0, 26)) {
            //a = 97, b = 97 + 1, ...
            int newCharNum = startNumBigA + charIndex;
            bigLetters.Add(newCharNum, (char)newCharNum);
        }

        int letterIndex = startA;

        foreach(char c in textToDecode) {

            if (!Char.IsLetter(c)) {
                result.Append(c);
                continue;
            }

            int toAscii = (int)c;

            int rotIndex = toAscii + rotNumber;

            if(Char.IsLower(c)) {

                if(rotIndex == endNum) {
                    letterIndex = startNumSmallA;
                    result.Append(smallLetters[letterIndex]);
                    continue;
                }

                //is rotIndex > z
                if(rotIndex > endNum) {
                    letterIndex = (rotIndex - endNum) + startNumSmallA;
                    result.Append(smallLetters[letterIndex]);
                    continue;
                }

                if(rotIndex <= endNum) {
                    letterIndex = rotIndex;
                    result.Append(smallLetters[letterIndex]);
                    continue;
                }
            }

            if(Char.IsUpper(c)) {

                if(rotIndex == endNumBigZ) {
                    letterIndex = startNumBigA;
                    result.Append(smallLetters[letterIndex]);
                    continue;
                }

                //is rotIndex > Z
                if(rotIndex > endNumBigZ) {
                    letterIndex = (rotIndex - endNumBigZ) + startNumBigA;
                    result.Append(bigLetters[letterIndex]);
                    continue;
                }

                if(rotIndex <= endNumBigZ) {
                    letterIndex = rotIndex;
                    result.Append(bigLetters[letterIndex]);
                    continue;
                }
            }

            

        }

        Console.WriteLine(result.ToString()); 

        return result.ToString();
    }
}

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var rot13 = new CryptographyROT13();

        rot13.Decipher("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}", 13);
    }
}