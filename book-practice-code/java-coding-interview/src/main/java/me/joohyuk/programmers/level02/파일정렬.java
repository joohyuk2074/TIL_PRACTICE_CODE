package me.joohyuk.programmers.level02;

import java.util.Arrays;
import java.util.Comparator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class 파일정렬 {
    public static void main(String[] args) {
        String[] input1 = {"img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"};
        String[] input2 = {"F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"};

        String[] results1 = solution(input1);
//        for (String s : results1) {
//            System.out.print(s + " ");
//        }

//        System.out.println();

//        String[] results2 = solution(input2);
//        for (String s : results2) {
//            System.out.print(s + " ");
//        }
    }

    public static String[] solution(String[] files) {
        Pattern p = Pattern.compile("([a-z\\s.-]+)([0-9]{1,5})");

        Arrays.sort(files, (s1, s2) -> {
            Matcher m1 = p.matcher(s1.toLowerCase());
            Matcher m2 = p.matcher(s2.toLowerCase());
            m1.find();
            m2.find();

            if(!m1.group(1).equals(m2.group(1))) {
                return m1.group(1).compareTo(m2.group(1));
            } else {
                return Integer.parseInt(m1.group(2)) - Integer.parseInt(m2.group(2));
            }
        });

        return files;
    }
}
