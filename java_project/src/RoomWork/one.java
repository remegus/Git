package RoomWork;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class one {
    public static void main(String[] args) {
        boolean bul = true;

        ArrayList<String> fname = new ArrayList();
        ArrayList<String> lname = new ArrayList();
        ArrayList<String> sname = new ArrayList();
        ArrayList<Integer> agename = new ArrayList();
        LinkedList<Integer> key = new LinkedList<>();

        Scanner scanner = new Scanner(System.in);
        Scanner scanner_age = new Scanner(System.in);
        while (bul) {
            System.out.println("Введите фамилию, имя и отчество :");
            String red = scanner.nextLine();
            System.out.println("Введите возраст :");
            int age = scanner_age.nextInt();
            System.out.println(red + " " + age);

            red += " - - -";
            String[] red1 = red.split(" ");
            fname.add(red1[0]);
            lname.add(red1[1]);
            sname.add(red1[2]);
            agename.add(age);
            key.add(fname.size()-1);

            System.out.println("Хотите добавить еще сотрудника? y/n");
            String ot = scanner.nextLine();
            if (ot.toLowerCase().equals("n")){
                bul = false;
            }
        }
//        for (int u = 0; u < fname.size(); ++u) {
//            System.out.println(fname.get(u) + ' ' + lname.get(u) + ' ' + sname.get(u) + ' ' + agename.get(u));
//        }

        int count = key.size()-1;
        while (count > -1) {
            int max_age = agename.get(key.get(count));
            int index = count;
            for (int i = 0; i < count; i++) {
                if (max_age < agename.get(key.get(i))) {
                    max_age = agename.get(key.get(i));
                    index = i;
                }
            }

            int tmp = key.get(count);
            key.set(count, key.get(index));
            key.set(index, tmp);
            count--;
        }
        key.forEach(n -> System.out.println(fname.get(n) + " " + lname.get(n) + " " + sname.get(n) + " " + agename.get(n)));

    }
}
