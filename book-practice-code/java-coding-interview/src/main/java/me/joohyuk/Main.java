package me.joohyuk;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        String[] input1 = {"img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"};
        String[] input2 = {"F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"};

        String[] results1 = solution(input1);
        String[] results2 = solution(input2);
    }


    public static String[] solution(String[] files) {
        String[] answer = {};

        List<File> results = new ArrayList<>();
        for (String fileName : files) {
            results.add(new File(fileName));
        }

        Collections.sort(results);

        answer = new String[files.length];
        for (int i = 0; i < files.length; i++) {
            File file = results.get(i);
            String text = file.getHeader().toString() + file.getNumbers().toString() + file.getTail().toString();
            answer[i] = text;
        }

        return answer;
    }
}

class File implements Comparable<File> {

    private final StringBuilder header;

    private final StringBuilder numbers;

    private final StringBuilder tail;

    public File(String fileName) {
        this.header = new StringBuilder();
        this.numbers = new StringBuilder();
        this.tail = new StringBuilder();

        boolean headerStartFlag = true;
        boolean numberStartFlag = false;
        for (int i = 0; i < fileName.length(); i++) {
            char c = fileName.charAt(i);
            if (headerStartFlag) {
                if ('0' <= c && c <= '9') {
                    headerStartFlag = false;
                    numberStartFlag = true;
                    this.numbers.append(c);
                } else {
                    this.header.append(c);
                }
            } else if (numberStartFlag) {
                if (('0' <= c && c <= '9') && numbers.length() < 5) {
                    this.numbers.append(c);
                } else {
                    numberStartFlag = false;
                    this.tail.append(c);
                }
            } else {
                this.tail.append(c);
            }
        }
    }

    public StringBuilder getHeader() {
        return header;
    }

    public StringBuilder getNumbers() {
        return numbers;
    }

    public StringBuilder getTail() {
        return tail;
    }

    @Override
    public int compareTo(File file) {
        String thisHeader = this.header.substring(0).toLowerCase();
        String otherHeader = file.numbers.substring(0).toLowerCase();

        if (thisHeader.equals(otherHeader)) {
            int thisNumber = Integer.parseInt(this.numbers.toString());
            int otherNumber = Integer.parseInt(file.numbers.toString());
            int result = thisNumber - otherNumber;
            return Integer.compare(result, 0);
        } else {
            return thisHeader.compareTo(otherHeader);
        }
    }
}