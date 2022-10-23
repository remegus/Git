import java.util.*;

import static java.util.Collections.sort;

public class lessonThree {
    public static void main(String[] args) {
//        Создать новый список, добавить несколько строк и вывести коллекцию на экран.
//        Итерация всех элементов списка цветов и добавления к каждому символа '!'.
//        Вставить элемент в список массивов в первой позиции.
//        Извлечь элемент (по указанному индексу) из заданного списка.
//        Обновить определенный элемент списка по заданному индексу.
//        Удалить третий элемент из списка.
//        Поиска элемента в списке по строке.
//       *Сортировка заданного списка массивов.
//       *Копирования одного списка массивов в другой.
        ArrayList<String> first = new ArrayList<>();
        ArrayList<String> colors = new ArrayList<>();
        colors.add("yellow");
        colors.add("black");
        colors.add("white");
        colors.add("green");
        colors.add("blue");
        colors.add("brown");
        colors.add("red");
        colors.add("pink");

        for (int i = 0;i<colors.size();++i){
            first.add(colors.get(i));
        }
        System.out.println(first);
        for (int i = 0;i<first.size();++i){
            String muv = first.get(i)+"!";
            first.set(i,muv);
        }
        for (String in : first) {
            System.out.println(in);
        }
        first.add(1,"kolos");
        first.remove(3);
        first.get(0);
        first.set(4,(first.get(4)+" phh!"));
        System.out.println(first);
        int i = 0;
        while(i < first.size()){
            if (first.get(i)=="kolos"){
                System.out.println("kolos is here -> index " + i);
                break;
            }
            i++;
        }
        colors.addAll(0,first);
        System.out.println(colors);
        sort(colors);
        System.out.println(colors);
    }
}

