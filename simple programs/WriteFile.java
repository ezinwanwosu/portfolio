
import java.io.FileWriter;
import java.io.IOException;

public class WriteFile {
    public static void main(String[] args) {
        try{
            FileWriter myWriter = new FileWriter("textFile.txt");
            myWriter.write("Files in Java might be tricky but they are fun");
            myWriter.close();
            System.out.println("Successfully wrote to file");
        } catch (IOException e){
            System.out.println("Error occured");
            e.printStackTrace();
        }
    }
}
