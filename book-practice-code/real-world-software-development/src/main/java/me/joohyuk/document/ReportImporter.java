package me.joohyuk.document;

import java.io.File;
import java.io.IOException;
import java.util.Map;

import static me.joohyuk.document.Attributes.*;

class ReportImporter implements Importer {
    private static final String NAME_PREFIX = "Patient: ";

    @Override
    public Document importFile(final File file) throws IOException {
//        final TextFile textFile = new TextFile(file);
//
//        textFile.addLines(NAME_PREFIX, );
//        textFile.addLines(2, line -> false, BODY);
//
//        final Map<String, String> attributes = textFile.getAttributes();
//        attributes.put(TYPE, "REPORT");
//        return new Document(attributes);
        return null;
    }
}
