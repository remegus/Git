import java.util.Random;

public class lesson_1 {
    public static void main(String[] args) {
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
        int m1 = ma_v(i, n);
        int m2 = mi_v(i, n);

        System.out.println("Случайное число:" + i + " ->  Номер старшего значащего бита:" + n);
        System.out.println("Количество кратных старшего значащего бита в максимум:" + m1 +
                "\nКоличество некратных старшего значащего бита в минимум " + m2);
    }
    public static int hightbit(int x){
        int y = Integer.highestOneBit(x);
        return y;
    }
    public static int ma_v (int i, int n){
        int m = 0;
        while (i < Short.MAX_VALUE) {
            if (i%n == 0){
                m++;
            }
            i++;
        }
        return m;
    }
    public static int mi_v(int i, int n){
        int m = 0;
        while (Short.MIN_VALUE < i) {
            if (i%n != 0){
                m++;
            }
            i--;
        }
        return m;
    }
}
