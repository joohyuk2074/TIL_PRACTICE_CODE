# Chapter 17. 코틀린에서 람다를 다루는 방법
- 함수는 Java에서 2급시민이지만, 코틀린에서는 1급 시민이다. 때문에, 함수 자체를 변수에 넣을 수도 있고 파라미터로 전달할 수도 있다.
- 코틀린에서 함수 타입은 (파라미터 타입, ...) -> 반환타입 이었다.
- 코틀린에서 람다는 두 가지 방버으로 만들 수 있고, {} 방법이 더 많이 사용된다.
    ```kotlin
    // 람다를 만드는 방법 1
    val isApple = fun(fruit: Fruit): Boolean {
        return fruit.name == "사과" 
    }
  
    // 람다를 만드는 방법 2
    val isApple2 = { fruit: Fruit -> fruit.name == "사과"}
    ```
- 함수를 호출하며, 마지막 파라미터인 람다를 쓸 때는 소괄호 밖으로 람다를 뺄 수 있다.
  ```kotlin
  filterFruits(fruits) { fruit -> fruit.name == "사과" }  // 이 경우를 더 선호
  filterFruits(fruits) { it.name == "사과" }
  ```
- 람다의 마지막 expression 결과는 람다의 반환 값이다.
- 코틀린에서는 Closure를 사용하여 non-final 변수도 람다에서 사용할 수 있다.