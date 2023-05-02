package me.joohyuk.tokenizer.application.dto.docmeta;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@JsonIgnoreProperties(ignoreUnknown = true)
@JsonInclude(JsonInclude.Include.NON_NULL)
@NoArgsConstructor(access = AccessLevel.PRIVATE)
public class DocMetaDto {

    @JsonProperty("group_id")
    private String groupId;

    @JsonProperty("group_uuid")
    private String groupUuid;

    @JsonProperty("collection_name")
    private String collectionName;

    @JsonProperty("collection_uuid")
    private String collectionUuid;

    @JsonProperty("document_id")
    private String documentId;

    @JsonProperty("document_uuid")
    private String documentUuid;

    @JsonProperty("document_title")
    private String documentTitle;

    @JsonProperty("document_uri")
    private String documentUri;

    @JsonProperty("language")
    private String language;

    @JsonProperty("created_at")
    private String createdAt;

    @JsonProperty("updated_at")
    private String updatedAt;


    // test용
    public static DocMetaDto createDefaultDocMetaDto() {
        DocMetaDto docMetaDto = new DocMetaDto();
        docMetaDto.language = "ko";
        docMetaDto.documentUuid = "5aa5d5c5-5c5d-4e5f-8b5a-6d5e3f2c1g1h";
        docMetaDto.documentUri = "/Users/joohyuk/Documents/JAVAWORKSPACE/posicube/gpt-data-backend/src/main/resources/file/sample.json";
        return docMetaDto;
    }
}
