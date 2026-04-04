package com.gigshield.backend.dto.response;

import lombok.Data;

@Data
public class SeverityResponse {
    private String severity_class;
    private double payout_modifier;
    private double confidence;
}