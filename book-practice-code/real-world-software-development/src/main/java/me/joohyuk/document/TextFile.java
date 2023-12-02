package me.joohyuk.document;

import java.util.List;
import java.util.Map;
import java.util.function.Predicate;

public class TextFile {

    private final Map<String, String> attributes;
    private final List<String> lines;

    public TextFile(Map<String, String> attributes, List<String> lines) {
        this.attributes = attributes;
        this.lines = lines;
    }

    int addLines(
        final int start,
        final Predicate<String> isEnd,
        final String attributeName
    ) {

        final StringBuilder accumulator = new StringBuilder();
        int lineNumber;
        for (lineNumber = start; lineNumber < lines.size(); lineNumber++) {
            final String line = lines.get(lineNumber);
            if (isEnd.test(line)) {
                break;
            }

            accumulator.append(line);
            accumulator.append("\n");
        }

        attributes.put(attributeName, accumulator.toString().trim());
        return lineNumber;
    }

    public Map<String, String> getAttributes() {
        return null;
    }
}
