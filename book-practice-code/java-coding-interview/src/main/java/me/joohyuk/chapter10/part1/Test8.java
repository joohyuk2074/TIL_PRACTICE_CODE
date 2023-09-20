package me.joohyuk.chapter10.part1;

import java.util.regex.Pattern;

public class Test8 {
    public static boolean isRotation(String str1, String str2) {
        return (str1 + str1).matches("(?i).*" + Pattern.quote(str2) + ".*");
    }
}
