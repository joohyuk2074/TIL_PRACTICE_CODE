package me.joohyuk.springsecurityoauth2client.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.web.SecurityFilterChain;

@EnableWebSecurity
@Configuration
public class OAuth2Config {
//
//    @Bean
//    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
//        http.authorizeHttpRequests(authRequest -> authRequest
//            .requestMatchers("/", "oauth2Login", "logout", "client").permitAll()
//            .anyRequest().authenticated());
//
//        http
//            .oauth2Client();
//
//        return http.build();
//    }
}
