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
        int[] m = new int[2];
        int t = rnd.nextInt(-1000, 1000);
        int i = t;
        int n = Integer.highestOneBit(i);
        while (i < Short.MAX_VALUE) {
            if (i%n == 0){
                System.out.println(i);
            }
            i++;
        }
        System.out.println(t + " " + n);
        System.out.println(m[0]);
    }
}
