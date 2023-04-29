package me.joohyuk.tokenizer.application.dto.inner;

import com.fasterxml.jackson.annotation.JsonProperty;

public class InputRetrieverDto {
    @JsonProperty("embedding_type")
    private String embeddingType;

    @JsonProperty("embedding_model_version")
    private String embeddingModelVersion;

    @JsonProperty("embedding_top_k")
    private String embeddingTopK;

    @JsonProperty("embedding_vector_db_type")
    private String embeddingVectorDbType;

    @JsonProperty("similarity_algorithm")
    private String similarityAlgorithm;
}
