# Chapter 02. 코틀린에서 null을 다루는 방법

- 코틀린에서 null이 들어갈 수 있는 타입은 완전히 다르게 간주된다.
    - 한 번 null 검사를 하면 non-null임을 컴파일러가 알 수 있다.
- null이 아닌 경우에만 호출되는 Safe Call (?.)이 있다.
- null이 절대 아닐때 사용할 수 있는 널 아님 단언 (!!)이 있다
- Kotlin에서 Java 코드를 사용할 때 플랫폼 타입 사용에 유의해야 한다
    - Java 코드를 읽으며 널 가능성 확인 / Kotlin으로 wrapping