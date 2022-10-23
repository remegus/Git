import java.util.ArrayList;
import java.util.Iterator;
import java.util.Random;

public class classRoomWork {
    public static void main(String[] args){
        ArrayList<Integer> low = new ArrayList<>();
        ArrayList<Integer> high = new ArrayList<>();

        for (int i = 0; i< 11;i++){
            low.add(new Random().nextInt(1,100));
            high.add(new Random().nextInt(1,100));
        }
        for (int in:low) {
            if (in>10) {
                System.out.println(in);
            }
        }
        System.out.println();
        low.retainAll(high);
        Iterator<Integer> middle = low.iterator();
        while(middle.hasNext()){
            int j = middle.next();
            if (j>10) {
                System.out.println(j);
            }
        }
    }
//    static double trime() {
//
//    }
}

