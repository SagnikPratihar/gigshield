package com.gigshield.backend.controller;

import com.gigshield.backend.dto.request.ClaimRequest;
import com.gigshield.backend.service.ClaimService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/api/claims")
@CrossOrigin(origins = "*")
public class ClaimController {

    @Autowired
    private ClaimService claimService;

    @PostMapping("/process")
    public Map<String, Object> processClaim(@RequestBody ClaimRequest request) {
        return claimService.processClaim(request);
    }
}