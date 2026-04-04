package com.gigshield.backend.model;

import com.gigshield.backend.model.enums.EventType;
import jakarta.persistence.*;
import lombok.Data;

import java.time.LocalDateTime;

@Entity
@Table(name = "disruption_events")
@Data
public class DisruptionEvent {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Enumerated(EnumType.STRING)
    private EventType eventType;

    @ManyToOne
    @JoinColumn(name = "zone_id")
    private Zone zone;

    private LocalDateTime triggeredAt;
    private LocalDateTime endedAt;

    private double severityValue;
    private String dataSource;

    private boolean isVerified = true;
}