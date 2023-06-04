# Chapter 07. 코틀린에서 예외를 다루는 방법 
- try catch finally 구문은 문법적으로 완전히 동일하다.
  - Kotlin에서는 try catch가 expression이다.
- Kotlin에서 모든 예외는 Unchecked Exception이다.
- Kotlin에서는 try with resources 구문이 없다. 대신 코틀린의 언어적 특징을 활용해 close를 호출해준다.