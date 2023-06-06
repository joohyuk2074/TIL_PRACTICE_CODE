# Chapter 09. 코틀린에서 클래스를 다루는 방법

- 코틀린에서는 필드를 만들면 getter와 (필요에 따라) setter가 자동으로 생긴다. 때문에 이를 프로퍼티 라고 부른다.
  ```kotlin
    class Person(
        val name: String = "김주혁",
        val age: Int = 1
    )
   ```
- 코틀린에서는 주생성자가 필수이다.
- 코틀린에서는 constructor 키워드를 사용해 부생성자를 추가호 만들 수 있다.
- 단, default parameter나 정적 팩토리 메서드를 추천한다.
- 실제 메모리에 존재하는 것과 무고나하게 custom getter와 custom setter를 만들 수 있다.
  - 함수로도 만들 수 있지만 객체의 프로퍼티인 것처럼 구현할 수도 있다.
- custom getter, custom setter에서 무한루프를 막기 위해 field라는 키워드를 사용한다. 이를 backing field라고 부른다.