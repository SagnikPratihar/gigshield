package com.gigshield.backend.model;

import com.gigshield.backend.model.enums.ClaimStatus;
import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDateTime;

@Entity
@Table(name = "claims")
@Data
public class Claim {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "worker_id")
    private User worker;

    @ManyToOne
    @JoinColumn(name = "policy_id")
    private Policy policy;

    @ManyToOne
    @JoinColumn(name = "disruption_event_id")
    private DisruptionEvent disruptionEvent;

    private double payoutAmount;
    private double fraudScore;

    @Enumerated(EnumType.STRING)
    private ClaimStatus status;

    private String rejectionReason;

    private LocalDateTime createdAt = LocalDateTime.now();
}