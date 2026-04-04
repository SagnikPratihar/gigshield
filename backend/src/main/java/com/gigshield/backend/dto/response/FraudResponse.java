package com.gigshield.backend.dto.response;

import lombok.Data;

@Data
public class FraudResponse {
    private double fraud_score;
    private String decision;
}