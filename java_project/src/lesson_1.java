import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;

public class lesson_1 {
    public static void main(String[] args) throws IOException, IOException {
//        Первый семинар.
//        1. Выбросить случайное целое число в диапазоне от -1000 до 1000 и сохранить в i
//        2. Посчитать и сохранить в n номер старшего значащего бита выпавшего числа
//        3. Найти все кратные n числа в диапазоне от i до Short.MAX_VALUE сохранить в массив m1
//        4. Найти все некратные n числа в диапазоне от Short.MIN_VALUE до i и сохранить в массив m2
//        5. Сохранить оба массива в файлы с именами m1 и m2 соответственно.
//                Пункты реализовать в методе main
//*Пункты реализовать в разных методах
        Random rnd = new Random();
        int i = rnd.nextInt(-1000, 1000);
        int n = hightbit(i);
        int[] m1 = ma_v(i, n);
        int[] m2 = mi_v(i, n);

        System.out.println("Случайное число:" + i + " ->  Номер старшего значащего бита:" + n);
        String mf1 = fin(m1);
        String mf2 = fin(m2);
        w_one(mf1);
        w_two(mf2);
    }

    public static int hightbit(int x) {
        int y = Integer.highestOneBit(x);
        return y;
    }

    public static int[] ma_v(int i, int n) {
        int m = 0;
        int s = 0;
        int t = i;
        while (i < Short.MAX_VALUE) {
            if (i % n == 0) {
                m++;
            }
            i++;
        }
        int[] m1 = new int[m];
        while (t < Short.MAX_VALUE) {
            if (t % n == 0) {
                m1[s] = t;
                s++;
            }
            t++;
        }
        return m1;
    }

    public static int[] mi_v(int i, int n) {
        int m = 0;
        int s = 0;
        int t = i;
        while (Short.MIN_VALUE < i) {
            if (i % n != 0) {
                m++;
            }
            i--;
        }
        int[] m2 = new int[m];
        while (Short.MIN_VALUE < t) {
            if (t % n != 0) {
                m2[s] = t;
                s++;
            }
            t--;
        }
        return m2;
    }

    public static String fin(int[] x) {
        String red = Arrays.toString(x);
        return red;
    }

    public static void w_one(String x) {
        try (FileWriter writer = new FileWriter("mf_one.txt", false)) {
            writer.write(x);
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public static void w_two(String x) {
        try (FileWriter writer = new FileWriter("mf_two.txt", false)) {
            writer.write(x);
            writer.flush();
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }
}