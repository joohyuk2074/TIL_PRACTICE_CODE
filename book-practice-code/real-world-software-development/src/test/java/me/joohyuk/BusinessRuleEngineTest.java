package me.joohyuk;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class BusinessRuleEngineTest {

    @Test
    void shouldHaveNoRulesInitially() {
        final BusinessRuleEngine businessRuleEngine = new BusinessRuleEngine();

        assertThat(businessRuleEngine.count()).isEqualTo(0);
    }

    @Test
    void shouldAddTwoActions() {
       final BusinessRuleEngine businessRuleEngine = new BusinessRuleEngine();

       businessRuleEngine.addAction(() -> {});
        businessRuleEngine.addAction(() -> {});

        assertThat(businessRuleEngine.count()).isEqualTo(2);
    }

    @Test
    void shouldExecuteOneAction() {
        final BusinessRuleEngine businessRuleEngine = new BusinessRuleEngine();
        final Action mockAction = mock(Action.class);

        businessRuleEngine.addAction(mockAction);
        businessRuleEngine.run();

        verify(mockAction).perform();
    }
}