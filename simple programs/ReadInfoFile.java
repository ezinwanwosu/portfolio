import java.io.File;

public class ReadInfoFile {
    public static void main(String[] args) {
        File myFile = new File("textfile.txt");
        if (myFile.exists()) { // if the file does not exist then it will go to the else statment
            System.out.println("File name : "+ myFile.getName());
            System.out.println("Absolute path: "+ myFile.getAbsolutePath());
            System.out.println("Writeable : "+ myFile.canWrite());
            System.out.println("Readable : "+ myFile.canRead());
            System.out.println("File size (bytes): "+ myFile.length());
        }else{
            System.out.println("File does not exist");
        }
    }
}
