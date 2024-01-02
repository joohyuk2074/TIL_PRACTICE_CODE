package me.joohyuk.leetcode.medium;

import java.util.ArrayList;
import java.util.List;

public class Palindrome_Partitioning {
    public List<List<String>> partition(String s) {
        if (s == null || s.isEmpty()) {
            return new ArrayList<>();
        }

        List<List<String>> result = new ArrayList<>();
        helper(s, new ArrayList<>(), result);
        return result;
    }

    public void helper(String s, List<String> step, List<List<String>> result) {
        // Base case
        if (s == null || s.isEmpty()) {
            result.add(new ArrayList<>(step));
            return;
        }

        for (int i = 1; i <= s.length(); i++) {
            String temp = s.substring(0, i);

            if (!isPalindrome(temp)) {
                continue;       // only do backtracking when current string is palindrome
            }

            step.add(temp);
            helper(s.substring(i), step, result);
            step.remove(step.size() - 1);
        }
    }

    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;
        while (left <= right) {
            if (s.charAt(left) != s.charAt(right))
                return false;
            left++;
            right--;
        }
        return true;
    }
}
