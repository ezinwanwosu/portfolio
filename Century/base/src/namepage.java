
import java.awt.event.KeyListener;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextArea;

public class namepage extends JFrame implements KeyListener {
    JPanel boardpanel = new JPanel();
    JTextArea questions = new JTextArea(20,50);
    JTextArea input = new JTextArea(1,50);

    public static void main(String[] args) {
        new namepage();
    }
    public namepage(){
        super("name page");

    }
}
