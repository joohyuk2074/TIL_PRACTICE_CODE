package me.joohyuk.chapter10.part1;

import java.util.HashMap;
import java.util.Map;

public class Test1 {
    private static final int MAX_CODE = 65535;

    private Test1() {
        throw new AssertionError("Cannot be instantiated");
    }

    public static boolean isUnique(String str) {
        if (str == null || str.isBlank()) {
            // Exception을 발생시킬 수도 있다.
            return false;
        }

        Map<Character, Boolean> chars = new HashMap<>();

        for (int i = 0; i < str.length(); i++) {
            if (str.codePointAt(i) <= MAX_CODE) {
                char ch = str.charAt(i);
                if (!Character.isWhitespace(ch)) {
                    if (chars.put(ch, true) != null) {
                        return false;
                    }
                }
            } else {
                System.out.println("The given string contains unallowed characters");
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {

    }
}
