package com.gigshield.backend.controller;

import com.gigshield.backend.dto.request.SendOtpRequest;
import com.gigshield.backend.dto.request.SignupRequest;
import com.gigshield.backend.dto.request.VerifyOtpRequest;
import com.gigshield.backend.model.User;
import com.gigshield.backend.repository.UserRepository;
import com.gigshield.backend.util.JwtUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/api/auth")
@CrossOrigin(origins = "*")
public class AuthController {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private JwtUtil jwtUtil;

    @PostMapping("/send-otp")
    public ResponseEntity<?> sendOtp(@RequestBody SendOtpRequest request) {
        if (request.getPhone() == null || request.getPhone().isEmpty()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Phone number required"));
        }
        return ResponseEntity.ok(Map.of("success", true, "message", "OTP sent successfully"));
    }

    @PostMapping("/verify-otp")
    public ResponseEntity<?> verifyOtp(@RequestBody VerifyOtpRequest request) {
        if (!"1234".equals(request.getOtp())) {
            return ResponseEntity.badRequest().body(Map.of("error", "Invalid OTP. Use 1234."));
        }

        Optional<User> optionalUser = userRepository.findByMobileNumber(request.getPhone());
        if (optionalUser.isEmpty()) {
            return ResponseEntity.ok(Map.of("isNewUser", true, "message", "User not found. Please sign up."));
        }

        User user = optionalUser.get();
        String token = jwtUtil.generateToken(user.getId(), user.getMobileNumber());

        Map<String, Object> userData = new HashMap<>();
        userData.put("id", user.getId());
        userData.put("name", user.getFullName());
        userData.put("phone", user.getMobileNumber());
        userData.put("createdAt", user.getCreatedAt());

        return ResponseEntity.ok(Map.of("token", token, "isNewUser", false, "user", userData));
    }

    @PostMapping("/signup")
    public ResponseEntity<?> signup(@RequestBody SignupRequest request) {
        if (!"1234".equals(request.getOtp())) {
            return ResponseEntity.badRequest().body(Map.of("error", "Invalid OTP. Use 1234."));
        }
        if (request.getName() == null || request.getPhone() == null) {
            return ResponseEntity.badRequest().body(Map.of("error", "Name and phone are required."));
        }

        Optional<User> optionalUser = userRepository.findByMobileNumber(request.getPhone());
        if (optionalUser.isPresent()) {
            return ResponseEntity.badRequest().body(Map.of("error", "User already exists. Please log in."));
        }

        User newUser = new User();
        newUser.setFullName(request.getName());
        newUser.setMobileNumber(request.getPhone());
        
        User savedUser = userRepository.save(newUser);
        String token = jwtUtil.generateToken(savedUser.getId(), savedUser.getMobileNumber());

        Map<String, Object> userData = new HashMap<>();
        userData.put("id", savedUser.getId());
        userData.put("name", savedUser.getFullName());
        userData.put("phone", savedUser.getMobileNumber());

        return ResponseEntity.ok(Map.of("token", token, "user", userData, "message", "Signup successful"));
    }
}