import java.util.Random;

public class lessonTwo {
    public static void main(String [] args){
//        Напишите программу на Java, чтобы найти наименьшее окно в строке, содержащей все символы другой строки.
//        Напишите программу на Java, чтобы проверить, являются ли две данные строки вращением друг друга.
//       *Напишите программу на Java, чтобы перевернуть строку с помощью рекурсии.
//        Дано два числа, например 3 и 56, необходимо составить следующие строки:
//              3 + 56 = 59 3 – 56 = -53 3 * 56 = 168 Используем метод StringBuilder.append().
//        Замените символ “=” на слово “равно”. Используйте методы StringBuilder.insert(),StringBuilder.deleteCharAt().
//       *Замените символ “=” на слово “равно”. Используйте методы StringBuilder.replace().
//      **Сравнить время выполнения пунка 6 со строкой содержащей 10000 символов "=" средствами String и StringBuilder.
        String seyXone = "ехал Грека через реку"; //21
        String seyYone = "видит Грека, в реке рак"; //23

        int result = whoBigger(seyXone, seyYone);
        System.out.println(result);

        String seyXtwo = reverseText(seyXone);
        String seyYtwo = reverseText(seyYone);
        System.out.println(seyXone + " - " + seyXtwo + "\n" + seyYone + " - " + seyYtwo);

        StringBuilder mat = new StringBuilder();
        mat = four(mat);
        StringBuilder matFive = five(mat);
        StringBuilder matSix = six(mat);
        System.out.println(mat + "\n - - - - - - - \n" + matFive + "\n - - - - - - - \n" + matSix);
        long time = System.currentTimeMillis();
        seven(mat);
        System.out.println((double)(System.currentTimeMillis()) - time);
    }
    static int whoBigger(String x ,String y) {
        int xOne = x.length();
        int yOne = y.length();
        return xOne > yOne ? xOne : yOne;
    }
    static String reverseText(String x) {
        return new StringBuilder(x).reverse().toString();
    }
    static int rd(int x, int y) {
        return new Random().nextInt(x, y);
    }
    static StringBuilder four(StringBuilder mat){
        int matX = rd(1, 10);
        int matY = rd(11, 99);
//        String.format("%s + %s = %s %s - %s = %s %s * %s = %s", matX, matY, matX + matY, matX, matY, matX - matY, matX, matY, matX * matY);
        mat.append(matX);
        mat.append(" + ");
        mat.append(matY);
        mat.append(" = ");
        mat.append(matX + matY);
        mat.append("  ");
        mat.append(matX);
        mat.append(" - ");
        mat.append(matY);
        mat.append(" = ");
        mat.append(matX-matY);
        mat.append("  ");
        mat.append(matX);
        mat.append(" * ");
        mat.append(matY);
        mat.append(" = ");
        mat.append(matX*matY);
        mat.append("\n");
        return mat;
    }
    static StringBuilder five(StringBuilder mat){
        int[] rt = new int[mat.length()/5];
        int co = 0;
        for (int i = 0; i<mat.length(); ++i) {
            if (mat.charAt(i) == '=') {
                rt[co] = i;
                co++;
            }
        }
        while (0 < co){
            --co;
            mat.deleteCharAt(rt[co]);
            mat.insert(rt[co], "равно");
        }
        return mat;
    }
    static StringBuilder six(StringBuilder mat){
        for (int i = 0; i<mat.length(); ++i){
            if (mat.charAt(i) == '='){
                mat.replace(i, i,"равно");
            }
        }
        return mat;
    }
    static void seven(StringBuilder mat){
        for (int i = 0; i<10000; i++){
            mat = four(mat);
        }
        five(mat);
    }

}
