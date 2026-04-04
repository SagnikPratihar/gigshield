package com.gigshield.backend.integration;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Map;

@Service
public class MLClient {

    @Autowired
    private RestTemplate restTemplate;

    private final String BASE_URL = "http://localhost:5000/api/ml";

    public Map<String, Object> getDisruption(Map<String, Object> payload) {
        return restTemplate.postForObject(BASE_URL + "/disruption", payload, Map.class);
    }

    public Map<String, Object> getFraud(Map<String, Object> payload) {
        return restTemplate.postForObject(BASE_URL + "/fraud", payload, Map.class);
    }
}