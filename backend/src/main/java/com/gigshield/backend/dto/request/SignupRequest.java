package com.gigshield.backend.dto.request;

import lombok.Data;

@Data
public class SignupRequest {
    private String name;
    private String phone;
    private String otp;
}
