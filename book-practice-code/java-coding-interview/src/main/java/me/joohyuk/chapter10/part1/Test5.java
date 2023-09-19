package me.joohyuk.chapter10.part1;

public class Test5 {
    public static String shrink(String str) {

        StringBuilder result = new StringBuilder();

        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            count++;

            // 공백은 개수를 세지 않고 그대로 복사합니다.
            if (!Character.isWhitespace(str.charAt(i))) {
                // 더 이상 처리할 문자가 없거나, 다음 문자가 현재 개수를 세고있는 문자와 다를 때
                if ((i + 1) >= str.length() || str.charAt(i) != str.charAt(i + 1)) {
                    result.append(str.charAt(i)).append(count);
                    count = 0;
                }
            } else {
                result.append(str.charAt(i));
                count = 0;
            }
        }

        return result.length() > str.length() ? str : result.toString();
    }
}
