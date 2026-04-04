package com.gigshield.backend.model;

import com.gigshield.backend.model.enums.PolicyStatus;
import com.gigshield.backend.model.enums.PolicyTier;
import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDate;

@Entity
@Table(name = "policies")
@Data
public class Policy {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "worker_id")
    private User worker;

    @Enumerated(EnumType.STRING)
    private PolicyTier tier;

    private double basePremium;
    private double actualPremium;

    private double maxDailyPayout;
    private double maxWeeklyPayout;

    private LocalDate coverageStart;
    private LocalDate coverageEnd;

    @Enumerated(EnumType.STRING)
    private PolicyStatus status = PolicyStatus.ACTIVE;

    private boolean autoRenew = true;
}