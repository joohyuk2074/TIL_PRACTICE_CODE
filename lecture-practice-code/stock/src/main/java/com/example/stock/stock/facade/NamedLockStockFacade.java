package com.example.stock.stock.facade;

import com.example.stock.stock.repository.LockRepository;
import com.example.stock.stock.service.StockService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

@RequiredArgsConstructor
@Component
public class NamedLockStockFacade {

    private final LockRepository lockRepository;

    private final StockService stockService;

    @Transactional
    public void decrease(Long id, Long quantity) {
        while (true) {
            try {
                lockRepository.getLock(id.toString());
                stockService.decrease(id, quantity);
            } finally {
                lockRepository.releaseLock(id.toString());
            }
        }
    }
}
