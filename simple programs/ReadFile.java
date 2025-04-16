import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFile{
    public static void main(String[] args) {
        try {
            File myObj = new File("textfile.txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNext()){
                String data = myReader.nextLine();
                System.out.println(data);
            }
            myReader.close();
        } catch (FileNotFoundException e) {
            System.out.println("File not found");
            e.printStackTrace();
        }
    }
}


    
}