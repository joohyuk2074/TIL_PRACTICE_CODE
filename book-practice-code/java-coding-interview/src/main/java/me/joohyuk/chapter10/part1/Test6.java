package me.joohyuk.chapter10.part1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Test6 {
    public static List<Integer> extract(String str) {
        if (str == null || str.isBlank()) {
            return Collections.emptyList();
        }

        List<Integer> result = new ArrayList<>();
        StringBuilder temp = new StringBuilder(String.valueOf(Integer.MAX_VALUE).length());

        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
            if (Character.isDigit(ch)) {
                temp.append(ch);
            } else {
                if (!temp.isEmpty()) {
                    result.add(Integer.parseInt(temp.toString()));
                    temp.delete(0, temp.length());
                }
            }
        }

        return result;
    }
}
