package com.gigshield.backend.service;

import com.gigshield.backend.dto.request.ClaimRequest;
import com.gigshield.backend.integration.MLClient;
import com.gigshield.backend.repository.ClaimRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.Map;

@Service
public class ClaimService {

    @Autowired
    private MLClient mlClient;

    @Autowired
    private ClaimRepository claimRepository;

    public Map<String, Object> processClaim(ClaimRequest request) {

        Map<String, Object> disruptionResult = new HashMap<>();
        if(request.getDisruptionPayload() != null) {
            disruptionResult = mlClient.getDisruption(request.getDisruptionPayload());
        }

        Map<String, Object> fraudResult = new HashMap<>();
        if(request.getFraudPayload() != null) {
            fraudResult = mlClient.getFraud(request.getFraudPayload());
        }

        Map<String, Object> result = new HashMap<>();
        result.put("disruption", disruptionResult);
        result.put("fraud", fraudResult);

        if ("high".equals(fraudResult.get("risk_level"))) {
            result.put("status", "PENDING_REVIEW");
        } else {
            result.put("status", "APPROVED");
        }

        return result;
    }
}