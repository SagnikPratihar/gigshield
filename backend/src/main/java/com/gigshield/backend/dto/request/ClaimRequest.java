package com.gigshield.backend.dto.request;

import lombok.Data;
import java.util.Map;

@Data
public class ClaimRequest {
    private Map<String, Object> disruptionPayload;
    private Map<String, Object> fraudPayload;
}