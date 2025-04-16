
import java.awt.Color;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

/**
 * Chatbot
 */
public class Chatbot extends JFrame implements KeyListener {

    JPanel p = new JPanel();
    JTextArea dialog = new JTextArea(20,50);
    JTextArea input = new JTextArea(1,50);
    JScrollPane scroll = new JScrollPane(
        dialog,
        JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED,
        JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);


    public static void main(String[] args) {
        new Chatbot();
    }


    public Chatbot() {
        super("Century");
        setSize(600,400);
        setResizable(false);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        // the defualt of 'setEditable' is true so, input text area will remain true
        dialog.setEditable(false);
        p.add(scroll);
        p.add(input);
        p.setBackground(new Color(255,200,0));
        add(p);
        setVisible(true);
    }

    @Override
    public void keyTyped(KeyEvent e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'keyTyped'");
    }

    @Override
    public void keyPressed(KeyEvent e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'keyPressed'");
    }

    @Override
    public void keyReleased(KeyEvent e) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'keyReleased'");
    }

    
}