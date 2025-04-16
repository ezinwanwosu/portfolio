
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class encrpytion {
    static String alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    static String[] myArray = alphabet.split("");
    static String encrpyTion(int key, String plaintext) {
        String[] text = plaintext.split("");
        String ciphertext = "";
        for (String myChar : text) {
            ciphertext = ciphertext + myChar;
            for (int j = 0; j < key; j++) {
                Random random = new Random();
                String randomChar = myArray[random.nextInt(myArray.length)];
                ciphertext = ciphertext + randomChar;
                        
            }
        }
        return ciphertext;
    }
    static String decrypt(String ciphertext, int key) {
        String[] myList = ciphertext.split("");
        ArrayList<String> decryptedtext = new ArrayList<String>();
        for (int idx = 0; idx < myList.length; idx+= key+1) {
            decryptedtext.add(myList[idx]);
            System.out.println(decryptedtext);
      
            
        }
        String decrypted = String.join(", ",decryptedtext);

        return decrypted;
    }

    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner myObj = new Scanner(System.in);
        System.out.println("ENTER TEXT: ");

        String plaintext = myObj.nextLine();

        System.out.println("Input key (between 1 and 10): ");
        int key = myObj.nextInt();
        while (key < 1 || key > 10) {
            System.out.println("Input key (between 1 and 10): ");
            key = myObj.nextInt();
        }
        String ciphertext = encrpyTion(key,plaintext);
        System.out.println(ciphertext);

        System.out.println("orginal was: "+ decrypt(ciphertext, key));
    




    }
}
