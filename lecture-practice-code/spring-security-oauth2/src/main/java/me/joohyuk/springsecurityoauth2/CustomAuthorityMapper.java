package me.joohyuk.springsecurityoauth2;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.authority.mapping.GrantedAuthoritiesMapper;

import java.util.Collection;
import java.util.HashSet;
import java.util.Set;

public class CustomAuthorityMapper implements GrantedAuthoritiesMapper {

    private static final String PREFIX = "ROLE_";

    @Override
    public Set<GrantedAuthority> mapAuthorities(Collection<? extends GrantedAuthority> authorities) {
        HashSet<GrantedAuthority> mapped = new HashSet<>(authorities.size());
        for (GrantedAuthority authority : authorities) {
            mapped.add(mapAuthority(authority.getAuthority()));
        }
        return mapped;
    }


    private GrantedAuthority mapAuthority(String name) {

        int index = name.lastIndexOf(".");
        if (index > 0) {
            name = "SCOPE_" + name.substring(index + 1);
        }

        if (!name.startsWith(PREFIX)) {
            name = PREFIX + name;
        }

        return new SimpleGrantedAuthority(name);
    }
}
