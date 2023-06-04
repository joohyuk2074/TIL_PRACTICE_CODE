# Chapter 08. 코틀린에서 함수를 다루는 방법

- 함수의 문법은 Java와 다르다!
  ```kotlin
  접근지시어 fun 함수이름(파라미터): 반환타입 {
  }
  ```
- body가 하나의 값으로 간주되는 경우 block을 없앨 수도있고, block이 없다면 반환 타입을 없앨 수도 있다.
  ```kotlin
  fun max(a: Int, b: Int): Int = if (a > b) a else b
  fun max(a: Int, b: Int) = if (a > b) a else b
  ```
- 함수 파라미터에 기본값을 설정해줄 수 있다.
- 함수를 호출할때 특정 파라미터를 지정해 넣어줄 수 있다.
- 가변인자에는 vararg 키워드를 사용하며, 가변인자 함수를 배열과 호출할 때는 *를 붙여주어야 한다.