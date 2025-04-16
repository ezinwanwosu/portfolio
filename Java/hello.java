
import java.util.Scanner;

/* class */
/**
 * hello
 */
public class hello {

    public static void main(String[] args) {
        System.out.println("Hello world");
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter your name:");
        String name = scan.nextLine();
        System.out.println("Hello "+name);
        scan.close();
    }
}