package com.gigshield.backend.dto.request;

import com.gigshield.backend.model.enums.Platform;
import lombok.Data;

@Data
public class RegisterRequest {

    private String mobileNumber;
    private String fullName;
    private String city;
    private Long zoneId;
    private Platform platform;
    private String upiId;

    private double avgDailyHours;
    private double avgHourlyIncome;
}